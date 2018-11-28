
#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <functional>
#include <cctype>
#include <climits>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <deque>
#include <stack>
#include <utility>
#include <string>
using namespace std;

vector<string> v(123);

const char dot = '.';

int solve(int a, int b) {
	bool flag;
	for (int i = 0; i < a; ++i) {
		for (int j = 0; j < b; ++j) {
			if (v[i][j] != dot) {
				flag = false;
				for (int t = 1; ; ++t) {
					if (i - t < 0 && i + t >= a && j - t < 0 && j + t >= b) {
						break;
					}
					if (i - t >= 0 && v[i-t][j] != dot) {
						flag = true; break;
					}
					if (i + t < a && v[i+t][j] != dot) {
						flag = true; break;
					}
					if (j - t >= 0 && v[i][j-t] != dot ){
						flag = true; break;
					}
					if (j + t < b  && v[i][j+t] != dot){
						flag = true; break;
					}
				}
				if (!flag) return -1;
			}
		}
	}
	int ret = 0;
	for (int i = 0; i < a; ++i) {
		for (int j = 0; j < b; ++j) {
			if (v[i][j] != dot) {
				if (v[i][j] == '<') ++ret;
				break;
			}
		}
		for (int j = b - 1; j >= 0; --j) {
			if (v[i][j] != dot) {
				if (v[i][j] == '>') ++ret;
				break;
			}
		}
	}
	for (int j = 0; j < b; ++j) {
		for (int i = 0; i < a; ++i) {
			if (v[i][j] != dot) {
				if (v[i][j] == '^') ++ret;
				break;
			}
		}
		for (int i = a - 1; i >= 0; --i) {
			if (v[i][j] != dot) {
				if (v[i][j] == 'v') ++ret;
				break;
			}
		}
	}
	return ret;
}

void prn(int t, int ans) {
	cout << "Case #" << t << ": ";
	if (ans < 0) 
		cout << "IMPOSSIBLE";
	else 
		cout << ans;
	cout << "\n";
}

int main () {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t ) {
		int a, b;
		cin >> a >> b;
		for (int i = 0; i < a; ++i) {
			cin >> ws >> v[i];
		}
		int ans = solve(a, b);
		prn(t, ans);
	}

	return 0;
}
