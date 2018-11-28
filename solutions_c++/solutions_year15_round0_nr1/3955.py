#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

struct testcase {
	int smax;
	vector<int> pws;

	static testcase* read() {
		testcase *c = new testcase();

		scanf("%d ", &c->smax);
		for (int i = 0; i <= c->smax; i++) {
			char n;
			scanf("%c", &n);
			c->pws.push_back(n - '0');
		}

		return c;
	}
	void solve() {
		int n = 0;

		int k = 0;
		for (int i = 0; i <= smax; i++) {
			if (k < i) {
				int d = i - k;
				n += d;
				k += d;
			}
			k += pws[i];
		}
		cout << n << endl;
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
			cout << "Case #" << (i+1) << ": ";
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
