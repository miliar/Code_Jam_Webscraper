#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int a[10009];

int main() {
	freopen("A-large (3).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int testCase;
	cin >> testCase;
	int caseNumber = 0;
	while (testCase--) {
		int n, x;
		cin >> n >> x;
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
		}
		sort(a, a + n);
		int res = 0;
		for (int i = n - 1; i >= 0; --i) {
			if (a[i] == -1) continue;
			int left = x - a[i];
			for (int j = 0; j < i; ++j) {
				if (a[j] != -1 && a[j] <= left) {
					a[j] = -1;
					break;
				}
			}
			++res;
		}
		printf("Case #%d: %d\n", ++caseNumber, res);
	}
} 
