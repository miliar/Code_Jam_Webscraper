#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

typedef long double T;

struct testcase {
	T c, f, x;
	static testcase* read() {
		testcase *c = new testcase();

		scanf("%Lf %Lf %Lf ", &c->c, &c->f, &c->x);

		return c;
	}
	void solve() {

		T best;

		T start = 0, rate = 2;
		best = x / rate;

		while (true) {
			T timeFarm = start + c / rate;
			start = timeFarm;
			rate = rate + f;
			
			T p = start + x / rate;
			if (p > best) break;
			best = p;
		}

		printf("%.7Lf\n", best);
	}
};

struct problem {
	int ncases;
	vector<testcase*> cases;

	void read() {
		cases.clear();
		scanf("%d ", &ncases);
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
