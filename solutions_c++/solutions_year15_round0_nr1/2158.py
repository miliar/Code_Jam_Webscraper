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

const int L = 10000 + 10;

char s[L];
int n, testCases;

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d %s", &n, &s);
		int cnt = 0, ans = 0;
		for (int i = 0; i <= n; ++i) {
			int x = s[i] - '0';
			if (i > cnt) {
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += x;
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}