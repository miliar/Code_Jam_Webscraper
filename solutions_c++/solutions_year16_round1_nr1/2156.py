#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<queue>
#define maxn 1070000
#define MAXN 1200
#define inf (1<<30)
#define modp 1000000007
#define maxLL 100000000000LL
#define mmodp 1000000000000007LL
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pa;
int n,m,tot;
int a,b,T;
LL K;

typedef struct Ed{
    int a,c,nxt;
    friend int operator < (struct Ed x,struct Ed y)
    {
        return x.c>y.c||x.c==y.c&&x.a>y.a;
    }
}E;

const double pi=4*atan(1);

LL mpow(LL x, LL y, LL p)
{
	LL res=1;
	while(y)
    {
        if (y&1) res=res*x%p;
		y=y>>1;
		x=x*x%p;
    }
	return res;
}

LL qpow(LL x, int y)
{
	LL res=1;
	int i=0;
	while(y)
    {
        if (y&1) res=res*x;
		y=y>>1;
		x=x*x;
    }
	return res;
}

LL gcd(LL x, LL y)
{
    while (y)
    {
        int r=x%y;
        x=y;
        y=r;
    }
    return x;
}

double mabs(double x)
{
    if (x<0) return -x;
    return x;
}

int q[2000];
int v[2000];

char s[2000];

void dp(int l, int r)
{
    if (l>r) return;
    char c='0';
    int j;
    for (int i=l;i<=r;++i)
    {
        if (s[i]>=c)
        {
            c=s[i];
            j=i;
        }
    }
    printf("%c",c);
    dp(l,j-1);
    for (int i=j+1;i<=r;++i) printf("%c",s[i]);
}



int main(void)
{
    //freopen("0.in","r",stdin);
    //freopen("1.out","w",stdout);
    scanf("%d",&T);
    for (int ci=1;ci<=T;++ci)
    {
        scanf("%s",s);
        n=strlen(s);
        printf("Case #%d: ",ci);
        dp(0,n-1);
        printf("\n");
    }
    return 0;
}
