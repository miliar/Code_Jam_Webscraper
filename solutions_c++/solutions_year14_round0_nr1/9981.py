#include <iostream>
#include <iomanip>
#include <string>

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>

#include <cmath>
#include <cfloat>
#include <cstring>
#include <cctype>

using namespace std;

typedef double dbl;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

const dbl EPS = DBL_EPSILON;
const dbl INF = DBL_MAX;

int cmp(double x, double y, double tol = EPS) {
	if (x > y + tol) return 1;
	if (x + tol < y) return -1;
	return 0;
}

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0);
	// cout.setf(ios::fixed);
	// cout.precision(?);

	int t;
	cin >> t;

	for (int test = 1; test <= t; ++test) {
		int n1;
		vector< vector<int> > table1(4, vector<int>(4, 0));

		cin >> n1;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> table1[i][j];
			}
		}

		int n2;
		vector< vector<int> > table2(4, vector<int>(4, 0));

		cin >> n2;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> table2[i][j];
			}
		}

		--n1;
		--n2;

		sort(table1[n1].begin(), table1[n1].end());
		sort(table2[n2].begin(), table2[n2].end());

		int count = 0;
		int kkk = 0;
		for (int i = 0; i < 4; ++i) {
			if (binary_search(table1[n1].begin(), table1[n1].end(), table2[n2][i])) {
				++count;
				kkk = table2[n2][i];
			}
		}

		cout << "Case #" << test << ": ";
		if (count == 0) {
			cout << "Volunteer cheated!\n";
		}
		else
		if (count == 1) {
			cout << kkk << '\n';
		}
		else {
			cout << "Bad magician!\n";
		}
	}

	return 0;
}

