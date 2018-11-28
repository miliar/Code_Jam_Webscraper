#include <cstdio>
#include <cstring>
int a[4][4];
bool u[17];

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, p, i, j, ans;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d", &p);
		--p;
		for (i=0; i<4; ++i)
			for (j=0; j<4; ++j) scanf("%d", a[i]+j);
		memset(u, 0, sizeof u);
		for (i=0; i<4; ++i) u[a[p][i]]=true;
		scanf("%d", &p);
		--p;
		for (i=0; i<4; ++i)
			for (j=0; j<4; ++j) scanf("%d", a[i]+j);
		ans=0;
		for (i=0; i<4; ++i)
			if (u[a[p][i]])
			{
				if (ans) ans=-1; else ans=a[p][i];
			}
		printf("Case #%d: ", tt);
		switch (ans)
		{
			case -1: puts("Bad magician!"); break;
			case 0: puts("Volunteer cheated!"); break;
			default: printf("%d\n", ans); break;
		}
	}
}
