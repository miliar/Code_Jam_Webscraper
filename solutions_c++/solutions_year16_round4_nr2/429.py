#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
double a[10001];
double b[10001];
double f[201][201];
int main()
{
//	freopen("B-small-attempt1.in","r",stdin);
//	freopen("B-small-attempt1.out","w",stdout);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,kk=0;
	scanf("%d",&T);
	while(T>0)
	{
		T--;
		kk++;
		int n,k;
		scanf("%d%d",&n,&k);
		int i,j;
		for(i=1;i<=n;i++)
			scanf("%lf",&a[i]);
		sort(a+1,a+1+n);
		printf("Case #%d: ",kk);
		int l=k,r=n+1,d=k+1;
		for(i=1;i<=k;i++)
			b[i]=a[i];
		double ans=0;
		while(l>=0)
		{
			memset(f,0,sizeof(f));
			f[1][1]=b[1];
			f[1][0]=((double)1-b[1]);
			for(i=2;i<=k;i++)
			{
				for(j=0;j<=k;j++)
				{
					if(j!=0)
						f[i][j]+=f[i-1][j-1]*b[i];
					f[i][j]+=f[i-1][j]*((double)1-b[i]);
				}
			}
			ans=max(ans,f[k][k/2]);
			l--;
			r--;
			d--;
			b[d]=a[r];
		}
		printf("%.9lf\n",ans);
	}
	return 0;
}
