#include <iostream>
#include <vector>

using namespace std;

struct testcase {
	int t1[4][4];
	int l1;
	int t2[4][4];
	int l2;

	static testcase* read() {
		testcase *c = new testcase();

		cin >> c->l1; c->l1--;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++)
				cin >> c->t1[i][j];

		cin >> c->l2; c->l2--;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++)
				cin >> c->t2[i][j];

		return c;
	}
	void solve() {
		vector<int> poss;
		for (int i = 0; i < 4; i++) poss.push_back(t1[l1][i]);

		for (unsigned i = 0; i < poss.size(); i++) {
			bool present = false;
			for (unsigned j = 0; j < 4; j++) {
				if (poss[i] == t2[l2][j]) present = true;
			}
			if (!present) {
				poss[i] = poss.back();
				poss.pop_back();
				i--;
			}
		}

		if (poss.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		} else if (poss.size() == 1) {
			cout << poss[0] << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
};

struct problem {
	int ncases;
	vector<testcase*> cases;

	void read() {
		cases.clear();
		cin >> ncases;
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
