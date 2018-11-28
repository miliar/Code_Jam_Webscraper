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

const int L = 100 + 1;

char s[L];
int testCases, n;

int calc(int sgn, int len) {
	if (len == 1) {
		return sgn ^ 1;
	}
	return calc(sgn ^ 1, len - 1) + 1;
}

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%s", s);
		n = strlen(s);
		int sgn = s[0] == '+';
		int l = 0, len = 0;
		for (int r = 1; r <= n; ++r) {
			if (r == n || s[r] != s[l]) {
				++len;
				l = r;
			}
		}
		int ret = calc(sgn, len);
		printf("Case #%d: %d\n", _, ret);
	}
	return 0;
}
