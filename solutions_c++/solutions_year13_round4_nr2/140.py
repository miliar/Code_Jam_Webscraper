#include <cstdio>
#include <algorithm>
#include <cstring>
#define int64 long long

int N;
int64 P,tot;

bool Can1(int64 x)
{
	int64 num=x,sum=tot,rank=0;
	for (int i=0;i<N;++i)
	{
		if (num==0) return rank<=P-1;
		num=(num-1)/2;
		sum/=2;
		rank+=sum;
	}
	return rank<=P-1;
}

bool Can2(int64 x)
{
	int64 num=tot-x-1,sum=tot;
	for (int i=0;i<N;++i)
	{
		if (num==0) return sum<=P;
		num=(num-1)/2;
		sum/=2;
	}
	return sum<=P;
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int ii=0;ii<Test;++ii)
	{
		printf("Case #%d: ",ii+1);
		
		scanf("%d%lld\n",&N,&P);
		tot=1;
		for (int i=0;i<N;++i) tot=tot*2;
		
		int64 l=0,r=tot-1;
		for (;l<r;)
		{
			int64 mid=(l+r)/2+1;
			if (Can1(mid)) l=mid;
			else r=mid-1;
		}
		printf("%lld ",l);
		
		l=0,r=tot-1;
		for (;l<r;)
		{
			int64 mid=(l+r)/2+1;
			if (Can2(mid)) l=mid;
			else r=mid-1;
		}
		printf("%lld\n",l);
	}
	
	return 0;
}
		
	