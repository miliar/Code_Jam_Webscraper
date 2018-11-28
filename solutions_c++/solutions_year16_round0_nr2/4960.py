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

char s[1000];

int main(void)
{
    //freopen("1.in","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;++i)
    {
        m=1;
        scanf("%s",s);
        n=strlen(s);
        char pre=s[0];
        for (int i=0;i<n;++i)
        {
            if (s[i]!=pre)
            {
                ++m;
            }
            pre=s[i];
        }
        if (s[n-1]=='+') --m;
        printf("Case #%d: %d\n",i,m);
    }
    return 0;
}
