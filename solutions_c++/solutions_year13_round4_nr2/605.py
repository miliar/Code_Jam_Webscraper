#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int N;
long long P, ans1, ans2;

bool check1(long long x)
{
	long long rank(x+1), before(0);
	for (int i=N;i;i--)
	{
		if (rank==1) return before<P;
		before+=(1ll<<(i-1));
		rank>>=1;
	}
	return before<P;
}

bool check2(long long x)
{
	long long rank((1<<N)-x), before(0);
	for (int i=N;i;i--)
	{
		if (rank>1) rank>>=1;
		else before+=(1ll<<(i-1));
	}
	return before<P;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T, CNT(0);
	scanf("%d",&T);
	for (;T;T--)
	{
		scanf("%d%I64d",&N,&P);
		ans1=ans2=0;
		for (int i=N-1;i>=0;i--)
		{
			if (check1(ans1+(1ll<<i))) ans1+=(1ll<<i);
			if (check2(ans2+(1ll<<i))) ans2+=(1ll<<i);
		}
		CNT++;
		printf("Case #%d: %I64d %I64d\n",CNT,ans1,ans2);
	}
	return 0;
}

