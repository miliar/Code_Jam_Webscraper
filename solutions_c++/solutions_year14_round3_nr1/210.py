#include<cstdio>
#include<algorithm>
using namespace std;

long long gcd(long long a,long long b)
{
	return b?gcd(b,a%b):a;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,i;
	long long n,m,g,k;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%I64d%*c%I64d",&n,&m);
		printf("Case #%d: ",t);
		g=gcd(n,m);
		n/=g;
		m/=g;
		for(k=m;k>1;k/=2)
			if(k&1)
				break;
		if(k>1)
		{
			puts("impossible");
			continue;
		}
		for(i=0;n<m;n*=2,i++);
		printf("%d\n",i);
	}
	return 0;
}
