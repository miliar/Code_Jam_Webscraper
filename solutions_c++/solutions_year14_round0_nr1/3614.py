#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <windows.h>
#include <string>
#include <cctype>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <initializer_list>
#include <exception>
#include <time.h>

typedef long long ll;

using namespace std;


//#define ONLINE_JUDGE
int main(int argc, char **argv) {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	vector <bool> cur(16, false);
	vector <int> row(4, 0);
	int rowIdx = 0;
	for (int tt = 1; tt <= t; ++tt) {
		int same = 0, ans = -1;
		cur.assign(16, false);
		cin >> rowIdx;
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> row[j];
				--row[j];
			}
			if (i == rowIdx) {
				for (int j = 0; j < 4; ++j) {
					cur[row[j]] = true;
				}
			}
		}
		cin >> rowIdx;
		for (int i = 1; i <= 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> row[j];
				--row[j];
			}
			if (i == rowIdx) {
				for (int j = 0; j < 4; ++j) {
					if (cur[row[j]] == true) {
						++same;
						ans = row[j] + 1;
					}
				}
			}
		}
		cout << "Case #" << tt << ": ";
		if (same == 0) {
			cout << "Volunteer cheated!" << endl;
		}
		else if (same > 1) {
			cout << "Bad magician!" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
	//system("pause");
	return 0;
}
