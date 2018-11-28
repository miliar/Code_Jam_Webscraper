#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T, cases = 0;
int q1, q2, ans;

int vis[17];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &q1);
		memset(vis, 0, sizeof(vis));
		int x;
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				scanf("%d", &x);
				if(i == q1)
					vis[x]++;
			}
		scanf("%d", &q2);
		for(int i = 1; i <= 4; i++)
			for(int j = 1; j <= 4; j++)
			{
				scanf("%d", &x);
				if(i == q2)
					vis[x]++;
			}
		int cnt = 0;
		for(int i = 1; i <= 16; i++)
			if(vis[i] == 2)
			{
				cnt++;
				ans = i;
			}
		printf("Case #%d: ", ++cases);
		if(cnt == 0)
			puts("Volunteer cheated!");
		if(cnt == 1)
			printf("%d\n", ans);
		if(cnt > 1)
			puts("Bad magician!");
	}
	return 0;
}
