#include <cstdio>
#include <iostream>
#include <set>
#define repn(i, a, b) for(int i = a; i < b; i++)
#define rep(i, a) repn(i, 0, a)

using namespace std;

int table1[4][4];
int table2[4][4];

void solve() {
	int row_1, row_2;
	cin >> row_1;
	rep (i, 4) rep (j, 4) cin >> table1[i][j];
	cin >> row_2;
	rep (i, 4) rep (j, 4) cin >> table2[i][j];
	row_1--;
	row_2--;
	set<int> cand_1;
	rep (i, 4) cand_1.insert(table1[row_1][i]);
	set<int> cand;
	rep (i, 4) if (cand_1.count(table2[row_2][i])) {
		cand.insert(table2[row_2][i]);
	}
	if (cand.size() == 1) {
		cout << *cand.begin() << endl;
	} else if (cand.empty()) {
		cout << "Volunteer cheated!"<< endl;
	} else {
		cout << "Bad magician!" << endl;
	}
}

int main() {
	int test = 0;
	cin >> test;
	rep (i, test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
