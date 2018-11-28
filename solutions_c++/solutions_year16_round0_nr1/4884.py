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

typedef long long LL;
typedef pair<int,int> pa;
int n,m,tot;
int a,b,T;
LL K;

LL mpow(LL x, LL y)
{
    if (y==0) return 1;
    LL res=mpow(x,y>>1);
    res*=res;
    res%=modp;
    if (y&1) res*=x;
    return res%modp;
}

typedef struct Ed{
    int a,c,nxt;
    friend int operator < (struct Ed x,struct Ed y)
    {
        return x.c>y.c;
    }
}E;

const double pi=4*atan(1);

double mabs(double x)
{
    if (x<0) return -x;
    return x;
}

int v[10];

int check(LL x)
{
    while (x)
    {
        int u=x%10;
        if (!v[u])
        {
            ++n;
            v[u]=1;
        }
        if (n==10) return 1;
        x/=10;
    }
    return 0;
}

int main(void)
{
    //freopen("1.in","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    //T=1000001;
    for (int i=1;i<=T;++i)
    {
        m=0;
        scanf("%d",&a);
        //a=i-1;
        K=a;
        memset(v,0,sizeof(v));
        n=0;
        if (K==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        while (1)
        {
            if (check(K))
            {
                printf("Case #%d: %lld\n",i,K);
                break;
            }
            ++m;
            if (m>1000000)
            {
                printf("Case #%d: INSOMNIA\n",i);
                break;
            }
            K+=a;
        }
    }

    return 0;
}
