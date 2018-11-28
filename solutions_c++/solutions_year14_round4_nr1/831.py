#include<cstdio>
#include<algorithm>
using namespace std;

int a[10005];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,n,m,i,j,s;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		for(scanf("%d%d",&n,&m),i=0;i<n;i++)
			scanf("%d",a+i);
		sort(a,a+n);
		for(i=0,j=n-1,s=0;i<=j;j--,s++)
		{
			if(a[i]+a[j]<=m)
				i++;
		}
		printf("Case #%d: %d\n",t,s);
	}
	return 0;
}
