#include <cstdio>
#include <cstring>
#define MAXN 1010
typedef long long Lint;
using namespace std;
Lint N;
Lint res1,res2,res;
Lint K;
Lint t;
Lint ar[MAXN],p[MAXN];
int main()
{
	int Test,tt;
	scanf(" %d",&Test);
	for(tt=1;tt<=Test;tt++)
	{
		printf("Case #%d: ",tt);
		memset(ar,0,sizeof ar);
		memset(p,0,sizeof p);
		
		res=0;
		t=0;
		int k=0;
		scanf(" %lld %lld",&N,&K);
		t=1LL <<  (N-1);
		ar[++k]=1;
		for(;++k;)
		{
			ar[k]=ar[k-1] * 2;
			p[k]=p[k-1]+t;
			t/=2;
			if(ar[k] == (1LL<<N))
			{
				ar[k]=1;
				break;
			}
		}
		for(int i=1;i<=k;i++)
		{
			if(p[i] < K) res+=ar[i];
			else break;
		}
		printf("%lld ",res-1);
		t=1LL <<  (N-1);
		ar[1]=1; p[1]=t*2-1;
		for(int i=2;i<=k;i++)
		{
			ar[i]=ar[i-1] * 2;
			p[i]=p[i-1]-t;
			t/=2;
		}
		ar[k]=1;
		res=1LL << N;
		for(int i=1;i<=k;i++)
		{
			if(p[i] >= K) res-=ar[i];
		}
		printf("%lld\n",res-1);
	}
	return 0;
}
