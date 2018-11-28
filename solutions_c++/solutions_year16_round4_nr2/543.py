#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
struct P
{
	long double c[210];
};
P operator *(const P& a,const P& b)
{
	P ans;
	memset(ans.c,0.0,sizeof(long double)*201);
	int i,j;
	for(i=0;i<=200;++i)
	{
		for(j=0;j<=1;++j)
		{
			if(i+j>=200)
			{
				break;
			}
			ans.c[i+j]+=a.c[i]*b.c[j];
		}
	}
	return ans;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	long double ps[444],ans;
	double dt;
	P pt,p1;
	int cas=0,T,i,j,k,n;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&k);
		for(i=0;i<n;++i)
		{
			scanf("%lf",&dt);
			ps[i]=dt;
		}
		sort(ps,ps+n);
		memcpy(ps+n,ps,sizeof(long double)*n);
		ans=0.0;
		for(i=n-k;i<=n;++i)
		{
			memset(pt.c,0.0,sizeof(long double)*201);
			pt.c[0]=1.0;
			for(j=i;j<i+k;++j)
			{
				memset(p1.c,0.0,sizeof(long double)*201);
				p1.c[0]=1.0-ps[j];
				p1.c[1]=ps[j];
				pt=pt*p1;
			}
			ans=max(ans,pt.c[k>>1]);
		}
		dt=ans;
		printf("Case #%d: %.8f\n",++cas,dt);
	}
	return 0;
}
/*
3
2 2
0.50 0.50
4 2
0.00 0.00 1.00 1.00
3 2
0.75 1.00 0.50
*/

