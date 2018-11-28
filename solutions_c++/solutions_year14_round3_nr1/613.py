#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

long long f[50];
int T;
long long p,q,pp;

long long gcd(long long a, long long b){ return a == 0 ? b : gcd(b % a, a); } 

int main()
{
	f[1]=2;
	for (int i=2;i<=40;i++) f[i]=f[i-1]<<1;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++)
	{
		scanf("%lld/%lld",&p,&q);
		pp=gcd(p,q);
		p=p/pp;
		q=q/pp;
		int k=0,k2=0;
		for (int i=1;i<=40;i++)
		{
			if (f[i]==q) {k=i; break;}
		}
		if (k==0) { printf("Case #%d: impossible\n",TT); continue;}

		for (int i=1;i<=42;i++)
		{
			if (p>=q) {k2=i-1; break;}
			p<<=1;
		}
		printf("Case #%d: %d\n",TT,k2);
		
	}
	return 0;
}