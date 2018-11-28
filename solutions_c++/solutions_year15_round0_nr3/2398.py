#include <cstdio>
#include <vector>

using namespace std;

const int ONE = 0;
const int I = 1;
const int J = 2;
const int K = 3;

int mult_id[4][4] = { 
	{ ONE, I, J, K },
	{ I, ONE, K, J },
	{ J, K, ONE, I },
	{ K, J, I, ONE }
};

int mult_sign[4][4] = {
	{ 1, 1, 1, 1 },
	{ 1, -1, 1, -1 },
	{ 1, -1, -1, 1 },
	{ 1, 1, -1, -1 }
};

struct Quat {
	int sign;
	int id;

	Quat() {
		sign = 1;
		id = ONE;
	}

	Quat(int _id) {
		sign = 1;
		id = _id;
	}

	Quat(int _sign, int _id) {
		sign = _sign;
		id = _id;
	}
};

Quat operator * (const Quat &a, const Quat &b) {
	int sign_pre = a.sign * b.sign;
	int sign_pos = mult_sign[a.id][b.id];
	int id = mult_id[a.id][b.id];

	Quat ans;
	ans.sign = sign_pre * sign_pos;
	ans.id = id;

	return ans;
}

bool operator == (const Quat &a, const Quat &b) {
	return a.sign == b.sign && a.id == b.id;
}

bool operator != (const Quat &a, const Quat &b) {
	return a.sign != b.sign || a.id != b.id;
}

Quat mpow(Quat a, int p) {
	if (p == 0)
		return Quat();
	if (p == 1)
		return a;

	Quat b = mpow(a, p / 2);
	if (p % 2 == 0)
		return b * b;
	return b * b * a;
}

int get_i(vector < Quat > &vals) {
	Quat curr;
	for (int i = 0; i < (int) vals.size(); i++) {
		curr = curr * vals[i];
		if (curr == Quat(I))
			return i + 1;
	}
	return -1;
}

int get_k(vector < Quat > &vals) {
	Quat curr;
	for (int i = (int) vals.size() - 1; i >= 0; i--) {
		curr = vals[i] * curr;
		if (curr == Quat(K))
			return (int) vals.size() - i;
	}
	return -1;
}

int main() {
	int tests; scanf("%d", &tests);
	for (int t = 1; t <= tests; t++) {
		int l;
		long long x;
		scanf("%d %lld", &l, &x);
		
		vector < Quat > vals(l);
		Quat res_all;
		for (int i = 0; i < l; i++) {
			char c;
			scanf(" %c", &c);
			if (c == 'i')
				vals[i] = Quat(I);
			else if (c == 'j')
				vals[i] = Quat(J);
			else
				vals[i] = Quat(K);

			res_all = res_all * vals[i];
		}

		res_all = mpow(res_all, x);

		bool poss = true;

		if (res_all != Quat(-1, ONE))
			poss = false;

		vector < Quat > big;
		for (int i = 0; i < 8; i++)
			big.insert(big.end(), vals.begin(), vals.end());

		int cnt1 = get_i(big);
		int cnt2 = get_k(big);

		if (cnt1 == -1 || cnt2 == -1) {
			poss = false;
		}
		else {
			long long sum = cnt1 + cnt2;
			if (sum >= x * (long long) l)
				poss = false;
		}

		printf("Case #%d: %s\n", t, poss ? "YES" : "NO");
	}

	return 0;
}