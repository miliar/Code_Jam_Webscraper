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
#define mmodp 10000000000000007LL
using namespace std;

typedef unsigned long long LL;
typedef pair<int,int> pa;
int n,m,tot;
int a,b,T;
LL K;

typedef struct Ed{
    int a,c,nxt;
    friend int operator < (struct Ed x,struct Ed y)
    {
        return x.c>y.c;
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


int chk(LL x)
{
	LL k=(rand()*rand()+rand())>>1;
	LL tmp=mpow(k,x-1,x);
	if (tmp!=1) return 1;
	return 0;
}

double mabs(double x)
{
    if (x<0) return -x;
    return x;
}
LL p[11];

int femat(LL n)
{
	if (n<=1) return 0;
	int k=300;
	for (int i=0;i<k;++i)
		if (chk(n)){
			return 0;
		}
	return 1;
}

void pr(int x)
{
    printf("1");
    for (int i=n-3;i>=0;--i)
    {
        if (x&(1<<i)) printf("1");
        else printf("0");
    }
    printf("1");
}

void calc()
{
    for (int j=2;j<=10;++j)
    for (LL i=2;i<=p[j]/i;++i)
    {
        if (p[j]%i==0)
        {
            printf(" %lld",i);
            break;
        }
    }
}


int pretest()
{
    int l=0;
    for (int j=2;j<=10;++j)
    for (LL i=2;i<=100;++i)
    {
        if (p[j]%i==0)
        {
            ++l;
            break;
        }
    }
    if (l==9) return 1;
    return 0;
}


int main(void)
{
    //freopen("1.in","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;++i)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",i);
        LL k=1<<(n-2);
        for (int i=0;i<k;++i)
        {
            int flag=1;
            for (int j=2;j<=10;++j)
            {
                LL b=1;
                p[j]=1;
                for (int l=0;l<n-2;++l)
                {
                    b*=j;
                    if (i&(1<<l)) p[j]+=b;
                }
                p[j]+=b*j;
                if (femat(p[j]))
                {
                    flag=0;
                    break;
                }
            }
            if (flag&&pretest())
            {
                --m;
                pr(i);
                calc();
                printf("\n");
            }
            if (!m) break;
        }
    }
    return 0;
}
