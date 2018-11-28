#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <deque>
#include <functional>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <assert.h>
#include <iomanip>
#include <unordered_map>

using namespace std;
long long pw[11][40];

int main() {
	ios::sync_with_stdio(false);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	int n, k;
	cin >> n >> k;
	cout << "Case #1:" << endl;
	for (int i = 2; i <= 10; i++) {
		pw[i][0] = 1;
		for (int j = 1; j <= 16; j++)
			pw[i][j] = pw[i][j - 1] * i;
	}
	vector<string> res;
	vector<vector<int> > aa;
	for (int mask = 0; mask < (1 << (n - 2)) && (int)res.size() < k; mask++) {
		int cnt = 0;
		vector<int> rr;
		for (int base = 2; base <= 10; base++) {
			long long cur = pw[base][n - 1] + 1;
			for (int i = 0; i < n - 2; i++) {
				if ((1 << i) & mask) {
					cur += pw[base][i + 1];
				}
			}
			for (int i = 2; 1LL * i * i <= cur; i++) {
				if (cur % i == 0) {
					cnt++;
					rr.push_back(i);
					break;
				}
			}
		}
		if (cnt == 9) {
			string temp = "1";
			for (int i = 0; i < n - 2; i++)
				if (mask & (1 << i))
					temp += "1";
				else
					temp += "0";
			temp += "1";
			reverse(temp.begin(), temp.end());
			res.push_back(temp);
			aa.push_back(rr);
		}
	}
	for (int i = 0; i < k; i++) {
		cout << res[i] << " ";
		for (int j = 0; j < 9; j++)
			cout << aa[i][j] << " ";
		cout << endl;
	}
	return 0;
}