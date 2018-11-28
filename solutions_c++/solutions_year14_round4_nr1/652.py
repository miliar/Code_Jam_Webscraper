#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, m, T, test;
int s[101010];

int main(){
	for (scanf("%d", &T), test = 1; test <= T; test++) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) scanf("%d", s + i);
		sort(s, s + n);
		int ans = 0, l = 0;
		for (int r = n - 1; r >= l; r--) {
			if (s[l] + s[r] <= m) ++l;
			++ans;
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
