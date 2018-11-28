#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1005;
int p[N];

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T --)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) scanf("%d", &p[i]);
		sort(p, p+n);
		int ans = N;
		for (int i = 1; i <= p[n-1]; i ++)
		{
			int tmp = i;
			for (int j = 0; j < n; j ++)
			{
				tmp += (p[j]+i-1)/i-1;
			}
			ans = min(tmp, ans);
		}
		printf("Case #%d: %d\n", ++ cas, ans);
	}
	return 0;
}
