#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define MAXN 10010
using namespace std;
int T,n,X,a[MAXN],sum[710];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j;
	scanf("%d",&T);
	for (int ii=1;ii<=T;++ii)
	{
		scanf("%d%d",&n,&X);
		memset(sum,0,sizeof(sum));
		for (i=1;i<=n;++i)
			scanf("%d",&a[i]),sum[a[i]]++;
		int ans=0;
		for (i=X;i>=1;--i)
		{
			while (sum[i])
			{
				--sum[i];
				for (j=X-i;j;--j)
				{
					if (sum[j])
					{
						--sum[j];
						break;
					}
				}
				++ans;
			}
		}
		printf("Case #%d: %d\n",ii,ans);
	}
	
	//system("pause");
	return 0;
}
