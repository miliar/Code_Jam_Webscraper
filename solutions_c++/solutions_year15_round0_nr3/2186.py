/*
 * Problem : 
 * Author : Hwhitetooth
 * Date : 
 * Result :
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int C[4][4] = {{1, 2, 3, 4},
					 {2, -1, 4, -3},
					 {3, -4, -1, 2},
					 {4, 3, -2, -1}};
const int L = 60000 + 10;

char a[L];
int sum[L];
string s, ss;
int testCases, n, t;

int trans(char c) {
	switch (c) {
		case 'i':
			return 2;
		case 'j':
			return 3;
		case 'k':
			return 4;
	}
}

int calc(int a, int b) {
	int sgn = a * b < 0 ? -1 : 1;
	a = abs(a);
	b = abs(b);
	return sgn * C[a - 1][b - 1];
}

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &t);
		cin >> s;
/*
		if (t & 1) {
			t = min(t, 5);
		}
		else {
			t = min(t, 6);
		}
*/
		n *= t;
		for (ss.clear(); t; --t) {
			ss = ss + s;
		}
		memcpy(a, ss.c_str(), n);
/*		
		printf("%s\n", a);
*/		
		sum[0] = trans(a[0]);
		for (int i = 1; i < n; ++i) {
			sum[i] = calc(sum[i - 1], trans(a[i]));
		}
/*
		for (int i = 0; i < n; ++i) {
			printf("%d ", sum[i]);
		}
		printf("\n");
*/
		if (sum[n - 1] != -1) {
			printf("Case #%d: NO\n", _);
			continue;
		}
		int flag = 0;
		for (int i = n - 2; i > 0; --i) {
			if (sum[i] == 4) {
				for (int j = i - 1; j >= 0; --j) {
					if (sum[j] == 2) {
						flag = 1;
						break;
					}
				}
				break;
			}
		}
		printf("Case #%d: %s\n", _, flag ? "YES" : "NO");
	}
	return 0;
}