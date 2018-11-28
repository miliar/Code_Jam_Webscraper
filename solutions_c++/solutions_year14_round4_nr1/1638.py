#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int n, sz[10001], x, ans;
bool used[10001];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tcase = 1; tcase <= t; tcase++)
	{
		printf("Case #%d: ", tcase);
		scanf("%d%d", &n, &x);
		ans = 0;
		for (int i = 0; i < n; i++) {
			used[i] = false;
			scanf("%d", &sz[i]);
		}
		sort(sz, sz + n);
		for (int i = n - 1; i >= 0; i--) {
			if (used[i])
				continue;
			used[i] = true;
			int j;
			for (j = i - 1; j >= 0; j--)
				if (sz[j] + sz[i] <= x && !used[j])
					break;
			if (j >= 0)
				used[j] = true;
			ans++;
		}
		printf("%d\n", ans);
	}
}