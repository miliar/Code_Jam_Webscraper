#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T,n,m;
int a[128][128];
int h[128];
int l[128];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int ww=1;ww<=T;ww++)
    {
    	printf("Case #%d: ",ww);
    	scanf("%d%d",&n,&m);
    	memset(h,255,sizeof(h));
    	memset(l,255,sizeof(l));
    	for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
			{
				scanf("%d",a[i]+j);
				h[i]=max(h[i],a[i][j]);
				l[j]=max(l[j],a[i][j]);
			}
		bool flag=true;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				if (a[i][j]!=h[i] && a[i][j]!=l[j]) flag=false;
		if (flag) printf("YES\n");
		else printf("NO\n");
    }
    return 0;
}
