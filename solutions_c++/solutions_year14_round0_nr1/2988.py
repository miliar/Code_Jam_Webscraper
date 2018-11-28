#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

#define N 600
#define inf 0x3f3f3f3f
#define eps 1e-8
#define ll long long

int cnt[17];
int main()
{
	freopen("a.out","w",stdout);
	int T,cas=0,a,x;
	cin>>T;
	while (T--)
	{
		memset(cnt,0,sizeof(cnt));
		cin>>a;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				cin>>x;
				if (i==a) cnt[x]++;
			}
		cin>>a;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
			{
				cin>>x;
				if (i==a) cnt[x]++;
			}
		int pp=0,ans;
		for (int i=1;i<=16;i++) if (cnt[i]==2) pp++,ans=i;
		printf("Case #%d: ",++cas);
		if (pp==1) printf("%d\n",ans);
		else if (pp>1)
			printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
}