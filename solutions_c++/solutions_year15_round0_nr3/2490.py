#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

enum qi {
	O = 0,
	I = 1,
	J = 2,
	K = 3,
};

struct quat {
	int sign;		// +1 or -1
	qi  v;		// 1, i, j, k

	string str() {
		return string(sign == 1 ? "" : "-") +
			(v == O ? "1" : (v == I ? "I" : (v == J ? "J" : "K")));
	}
};

const quat q1 = { 1, O };
const quat qi = { 1, I };
const quat qj = { 1, J };
const quat qk = { 1, K };

const quat mt[4][4] = {
	{ { 1, O }, { 1, I }, { 1, J }, { 1, K } },
	{ { 1, I }, {-1, O }, { 1, K }, {-1, J } },
	{ { 1, J }, {-1, K }, {-1, O }, { 1, I } },
	{ { 1, K }, { 1, J }, {-1, I }, {-1, O } },
};

quat mul(quat a, quat b) {
	quat r = mt[a.v][b.v];
	r.sign *= a.sign * b.sign;
	// fprintf(stderr, "%s * %s = %s\n", a.str().c_str(), b.str().c_str(), r.str().c_str());
	return r;
}

quat pow(quat a, int x) {
	if (x == 0) return q1;
	if (x == 1) return a;
	if (x == 2) return mul(a, a);

	quat b = pow(a, x / 2);
	if (x % 2 == 1) {
		return mul(a, mul(b, b));
	} else {
		return mul(b, b);
	}
}

struct testcase {
	int l;
	int x;
	vector<quat> s;

	static testcase* read() {
		return new testcase();
	}

	testcase() {
		// Read input
		scanf("%d %d ", &l, &x);
		for (int i = 0; i < l; i++) {
			char c;
			scanf("%c", &c);
			if (c == 'i') s.push_back(qi);
			if (c == 'j') s.push_back(qj);
			if (c == 'k') s.push_back(qk);
		}
	}

	bool ok() {
		if (l * x < 3) return false;

		quat prod = q1;
		for (int i = 0; i < s.size(); i++) {
			prod = mul(prod, s[i]);
		}

		quat ppw = pow(prod, x);
		if (ppw.v != O || ppw.sign != -1) return false;		// total product = ijk = -1

		bool has_jk = false;
		for (int i = 0; i < s.size(); i++) {
			if (s[i].v == J || s[i].v == K) {
				has_jk = true;
				break;
			}
		}
		if (!has_jk) return false;

		quat u = q1;
		for (int i = 0; i < l * x - 2; i++) {
			u = mul(u, s[i % l]);
			if (u.v == I && u.sign == 1) {
				quat v = q1;
				for (int j = i+1; j < l*x - 1; j++) {
					v = mul(v, s[j % l]);
					if (v.v == J && v.sign == 1) {
						return true;
					}
				}
			}
		}

		return false;
	}

	void solve() {
		printf("%s\n", (ok() ? "YES" : "NO"));
	}
};

struct problem {
	int ncases;
	vector<testcase*> cases;

	void read() {
		cases.clear();
		scanf("%d", &ncases);
		for (int i = 0; i < ncases; i++) {
			cases.push_back(testcase::read());
		}
	}
	void solve() {
		for (int i = 0; i < ncases; i++) {
			printf("Case #%d: ", i+1);
			cases[i]->solve();
		}
	}
};

int main() {
	problem p;
	p.read();
	p.solve();

	return 0;
}
