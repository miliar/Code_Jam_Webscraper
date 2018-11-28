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

int q[300][300];
int v[3000][5];
int u[1000];

int mcmp(int*x,int*y)
{
    return (*x)<(*y);
}

int main(void)
{
    //freopen("0.in","r",stdin);
    //freopen("1.out","w",stdout);
    scanf("%d",&T);
    for (int ci=1;ci<=T;++ci)
    {
        scanf("%d",&n);
        for (int i=0;i<n*2-1;++i)
        {
            for (int j=0;j<n;++j) scanf("%d",q[i]+j);
        }
        int flag=1;
        printf("Case #%d:",ci);
        for (int i=0;i<n&&flag;++i)
        {
            for (int j=0;j<2*n-1;++j) u[j]=q[j][i];
            sort(u,u+(2*n-1));
            if (i*2+1==2*n-1||u[i*2]!=u[i*2+1])
            {
                flag=0;
                u[2*n-1]=u[i*2];
                sort(u,u+(2*n));
                for (int j=0;j<2*n-1;++j)
                if (q[j][i]==u[2*i])
                {
                    int k1=0;
                    int k2=0;
                    while (k1<2*n||k2<n)
                    {
                        if (k2<n&&u[k1]==q[j][k2]) ++k1,++k2;
                        else {
                            printf(" %d",u[k1]);
                            ++k1;
                        }
                    }
                    break;
                }
            }
        }
        printf("\n");
    }
    return 0;
}
