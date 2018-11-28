#pragma warning (disable:4786)
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<list>
#include<utility>
#include<algorithm>
#include<cstdlib>
#include<sstream>
#include<string>
using namespace  std;
//typedef int LL;
typedef __int64 LL;

#define INF 999999999

LL MX(LL a,LL b){return (a>b)?a:b;}
LL MN(LL a,LL b){return (a<b)?a:b;}
LL ABS(LL a){return (a<0)?-1*a:a;}
LL SQ(LL a){return a*a;}
LL POW[45];

LL gcd(LL a,LL b)
{
	if(a==0) return b;
	if(b==0) return a;
	return gcd(b%a,a);
}
int main()
{
	LL t,cas=0,p,q,i,j;
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	POW[0]=1;
	for(i=1;i<=40;i++)POW[i]=POW[i-1]*2;
	scanf("%I64d",&t);
	while(t--)
	{
		scanf("%I64d/%I64d",&p,&q);
		LL Gcd=gcd(p,q);
		p/=Gcd;q/=Gcd;
		LL gen=0;
		while(!(q&1)&& gen<40)
		{
			q/=2;
			gen++;
		}
		j=0;
		while(POW[j]<=p)
		{
			j++;
		}
		gen=gen-j+1;
		if(q!=1|| !(p&1) || gen<0) {printf("Case #%I64d: impossible\n",++cas);continue;}
	    printf("Case #%I64d: %I64d\n",++cas,gen);
	}
	return 0;
}