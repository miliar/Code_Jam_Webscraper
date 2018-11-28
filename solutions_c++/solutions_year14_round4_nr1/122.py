#include<cstdio>
#include<algorithm>

int a[10000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		int i,j,n,m;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		std::sort(a,a+n);
		for(i=n-1,j=0;i>=j;i--)if(i>j&&a[i]+a[j]<=m)j++;
		printf("Case #%d: %d\n",tc,n-j);
	}
	return 0;
}