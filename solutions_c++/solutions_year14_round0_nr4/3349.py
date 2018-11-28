#include<cstdio>
#include<algorithm>
using namespace std;
double d1[1000],d2[1000];
int main()
{
	freopen("1.in","r",stdin);
	freopen("out.out","w",stdout);
	int t,n,a,b,c,d;
	scanf("%d",&t);
	for(int ca=1;ca<=t;++ca)
	{
		printf("Case #%d: ",ca);
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%lf",d1+i);
		for(int i=0;i<n;++i)
			scanf("%lf",d2+i);
		sort(d1,d1+n);
		sort(d2,d2+n);
		a=b=0;
		c=d=n-1;
		while(d>=0)
		{
			while(~d&&d2[d]>d1[c])
			{--d;++a;}
			--c;--d;
		}
		c=d=0;
		while(d<n)
		{
			while(d<n&&d2[d]<d1[c])
			{++d;++b;}
			++c;++d;
		}
		printf("%d %d\n",n-a,b);
	}
}
