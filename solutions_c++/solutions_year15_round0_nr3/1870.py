#include <cstdio>
#include <cstring>

#define L 10000

int m[5][5]=
{
	{+0,+0,+0,+0,+0},
	{+0,+1,+2,+3,+4},
	{+0,+2,-1,+4,-3},
	{+0,+3,-4,-1,+2},
	{+0,+4,+3,-2,-1},
};
int T,l,s[L+9],d[L+9],r[L+9];
bool ans;
long long x;
long long ppp[9],*p=ppp+4;
long long pi,pj,ttt;
long long first_i,last_j;

int min(long long a,long long b)
{
	return a<b?a:b;
}
int max(long long a,long long b)
{
	return a>b?a:b;
}
int mul(int a,int b)
{
	int sign=+1;
	if (a<0) sign*=-1,a=-a;
	if (b<0) sign*=-1,b=-b;
	return sign*m[a][b];
}
int div(int a,int b)
{
	int sign=+1;
	if (b<0) sign*=-1,b=-b;
	for (int i=1;i<=4;++i)
	{
		if (m[b][i]==+a) return +sign*i;
		if (m[b][i]==-a) return -sign*i;
	}
	return 0;
}
int pow(int a,int e)
{
	int d=1;
	do
	{
		if (e&1) d=mul(d,a);
		a=mul(a,a);
	}
	while (e>>=1);
	return d;
}
int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
	{
		ans=true;
		scanf("%d%lld%*c",&l,&x);
		d[0]=1;
		for (int i=1;i<=l;++i)
		{
			s[i]=getchar()-'g';
			d[i]=mul(d[i-1],s[i]);
		}
		if (pow(d[l],x)!=-1)
		{
			ans=false;
			goto ANSWER;
		}
		r[0]=d[l];
		for (int i=1;i<l;++i) r[i]=mul(div(r[i-1],s[i]),s[i]);
		r[l]=r[0];
		first_i=x*l+1;
		last_j=0;
		for (int i=1;i<=l;++i)
		{
			pi=pj=0;
			ttt=0XFFFFFFFFFFFF;
			memset(ppp,0,sizeof(ppp));
			int e=d[i];
			p[e]=1;
			if (e==2) pi=i;
			if (e==4) pj=i;
			for (long long j=2;j<=x;++j)
			{
				e=mul(e,r[i]);
				if (e==2) pi=(j-1)*l+i;
				if (e==4) pj=(j-1)*l+i;
				if (p[e])
				{
					ttt=j-p[e];
					break;
				}
				else p[e]=j;
			}
			if (pi) first_i=min(first_i,pi);
			if (pj) last_j=max(last_j,pj+((x-(pj+l-1)/l)/ttt)*ttt*l);
		}
		if (first_i<1 || first_i>=last_j || last_j>=x*l) ans=false;
		ANSWER:printf("Case #%d: %s\n",t,ans?"YES":"NO");
	}
	return 0;
}
