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
int a[1010];

int main(){
	for (scanf("%d", &T), test = 1; test <= T; ++test) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%d", a + i);
		int ans = 0;
		const int MAX = 0x7FFFFFFF;
		for (int k = 0; k < n; ++k) {
			int p = 0;
			for (int i = 1; i < n; ++i)
				if (a[i] < a[p]) p = i;
			int u = 0, v = 0;
			for (int i = 0; i < p; ++i)
				if (a[i] != MAX && a[i] > a[p]) ++u;
			for (int i = p + 1; i < n; ++i)
				if (a[i] != MAX && a[i] > a[p]) ++v;
			ans += min(u, v);
			a[p] = MAX;
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
