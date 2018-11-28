#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

#define ll long long
#define INF 0x3f3f3f3f
#define LL_INF 0x3f3f3f3f3f3f3f3f
#define MAX

bool vis[11];

bool judge()
{
	for (int i = 0; i <= 9; ++i)
		if (!vis[i])
			return true;
	return false;
}

int main()
{
	//freopen("debug\\in.txt", "r", stdin);
	//freopen("CON", "w", stdout);
	int i, j, k;
	int test, n, kase = 1;
	scanf("%d", &test);
	while (test--) {
		scanf("%d", &n);
		memset(vis, 0, sizeof(vis));
		int ans = 0, res = n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", kase++);
			continue;
		}
		while (judge()) {
			int t = res;
			while (t >= 10) {
				int tmp = t % 10;
				t /= 10;
				vis[tmp] = 1;
			}
			vis[t] = 1;
			res += n;
			ans++;
		}
		printf("Case #%d: %d\n", kase++, res - n);
	}
	return 0;
}