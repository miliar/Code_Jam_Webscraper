#include<cstdio>
#include<cstring>
const int N = 105;
int a[N][N];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		int n,m,k,i,j;
		scanf("%d%d",&m,&n);
		int flag=0;
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)scanf("%d",&a[i][j]);
		}
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				int f1=0,f2=0;
				for(k=0;k<m;k++)if(a[k][j]>a[i][j])f1=1;
				for(k=0;k<n;k++)if(a[i][k]>a[i][j])f2=1;
				if(f1&&f2)flag=1;
			}
		}
		printf("Case #%d: ",ca++);
		if(!flag)puts("YES");
		else puts("NO");
	}
}