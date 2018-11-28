#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int s[10005];
int u[10005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-l.out", "w", stdout);

	int t, cas = 1;
	int n, i, x, ans;
	
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%d", &n, &x);
		memset(u, 0, sizeof(u));
		for(i=0; i<n; i++)
			scanf("%d", s+i);
		sort(s, s+n);
		ans = 0;
		for(i=n-1; i>=0; i--)
		{
			if(u[i]) continue;
			for(int j=i-1; j>=0; j--)
				if(u[j]==0 && s[j]+s[i]<=x)
				{
					u[j] = 1;
					break;
				}
			ans++;
		}
		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}