#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<functional>
#include<iostream>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define MP(a,b) make_pair(a,b)
#define clr(x,y) memset(x,y,sizeof x)
#define fi first
#define se second
#define sqr(z) ((z)*(z))
using namespace std;
typedef pair<int,int> PII;
const int oo=1047483647,maxn=110000;
int tt,n,i,j,k,m,q,T;
double C,X,tmp,Time,F;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	fo(tt,1,T)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double now=0;
		double last=X/2.0;
		double money=0,per=2;
		while (1)
		{
		    Time=C/per;
			tmp=now+Time+X/(per+F);
			if (tmp>last) break;
			per=per+F;
			now=now+Time;
			last=tmp;
		}
		printf("Case #%d: ",tt);
		printf(" %.7f\n",last);
	}
	return 0;
}
