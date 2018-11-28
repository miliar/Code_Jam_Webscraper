#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m,a[200][200];
bool check()
{
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			if(a[i][0]>a[i][j]&&a[0][j]>a[i][j])return 0;
	return 1;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			{
				scanf("%d",&a[i][j]);
				a[i][0]=max(a[i][0],a[i][j]);
				a[0][j]=max(a[0][j],a[i][j]);
			}
		printf("Case #%d: ",tt);
		if(check())printf("YES\n");
		else printf("NO\n");
	}
}

