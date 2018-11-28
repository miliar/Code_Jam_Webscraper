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

const int N = 1000 + 10;

int a[N];
int n, testCases;

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d", &n);
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			ans = max(ans, a[i]);
		}
		for (int i = 1; i < ans; ++i) {
			int cnt = 0;
			for (int j = 0; j < n; ++j) {
				cnt += (a[j] - 1) / i;
			}
			ans = min(ans, cnt + i);
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}