#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define debug 01
#define openfile freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;

int s[2000];
int res = 10000000;
int test;

int main() {
	if (debug) openfile;			
	cin >> test;
	int n;
	for (int ii=0; ii<test; ii++) {

		cin >> n;
		int maxValue = 0;
		for (int i = 0; i < n; i++) {
			int tmp;
			cin >> s[i];
			if (maxValue < s[i]) maxValue = s[i];
		}
		res = 10000000; 

		for (int minLimit = maxValue; minLimit > 0; minLimit--) {
			int minute = 0;
			
			for (int i = 0; i < n; ++i) {
				int waitTime = s[i] / minLimit;
				if (s[i] % minLimit == 0) waitTime--;
				minute += waitTime;
			}
			if (minute + minLimit < res) res = minLimit + minute;
		}
		cout << "Case #" << ii + 1 << ": " << res << endl;
	}
}
