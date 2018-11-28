#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <limits>
#include <set>
#include <algorithm>
#include <iterator> 

using namespace std;

const int Max = 4;

int a[Max][Max];
int t, first, second;
set<int> firstSet;
set<int> secondSet;
std::vector<int> commonSet;

int main() {
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	for (int test = 1; test <= t; test++) {
		cin >> first;

		for (int i = 0; i < Max; i++) {
			for (int j = 0; j < Max; j++) {
				cin >> a[i][j];
			}
		}

		firstSet.clear();
		for (int i = 0; i < Max; i++) {
			firstSet.insert(a[first - 1][i]);
		}

		cin >> second;

		for (int i = 0; i < Max; i++) {
			for (int j = 0; j < Max; j++) {
				cin >> a[i][j];
			}
		}

		secondSet.clear();
		for (int i = 0; i < Max; i++) {
			secondSet.insert(a[second - 1][i]);
		}

		commonSet.clear();
		set_intersection(
			firstSet.begin(),
			firstSet.end(),
			secondSet.begin(),
			secondSet.end(),
			std::back_inserter(commonSet));

		if (commonSet.size() == 1) {
			cout << "Case #" << test << ": " << commonSet[0] << endl;
		} else if (commonSet.size() > 1) {
			cout << "Case #" << test << ": " << "Bad magician!" << endl;
		} else {
			cout << "Case #" << test << ": " << "Volunteer cheated!" << endl;
		}
		 
	}

	return 0;
}