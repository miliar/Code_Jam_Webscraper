#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;
int findDivisor6(string s) {
	int ret = 0;
	int len = s.size();
	long long n = 0;
	for (int i = 0; i < len; i++) {
		if (s[i] == '1') {
			n += pow(6, len - i - 1);
		}
	}
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, J;
		cin >> n >> J;
		cout << "Case #" << t << ":" << endl;

		vector< vector<int> > bitpos;
		int mx = 1000000;
		for (int x1 = 1; x1 < n - 1 && (int)bitpos.size() < mx; x1++) {
			for (int x2 = x1 + 1; x2 < n - 1 && (int)bitpos.size() < mx; x2++) {
				for (int x3 = x2 + 1; x3 < n - 1 && (int)bitpos.size() < mx; x3++) {
					for (int x4 = x3 + 1; x4 < n - 1 && (int)bitpos.size() < mx; x4++) {
						int tmparr[] = {0, x1, x2, x3, x4, n - 1};
						vector<int> tmp(tmparr, tmparr + 6);
						bitpos.push_back(tmp);
					}
				}
			}
		}
		int count = 0;
		for (int k = 0; k < (int)bitpos.size() && count < J; k++) {
			string s;
			int idx = 0;
			int mod = 0;
			for (int j = 0; j < n; j++) {
				if (idx >= n || j < bitpos[k][idx]) {
					s += "0";
				} else {
					s += "1";
					idx++;
					mod += pow(-1, j + 1);
				}
			}
			int divisor6 = findDivisor6(s);
			if (mod % 3 == 0 && divisor6 > 0) {
				count++;
				cout << s << " ";
				for (int j = 2; j <= 10; j++) {
					int divisor = j % 2 ? 2 : 3;
					if (j == 6) {
						divisor = divisor6;
					}
					cout << divisor;
					if (j < 10) {
						cout << " ";
					}
				}
				cout << endl;
			}
		}
	}
}

