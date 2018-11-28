#include <cstdio>
#include <cmath>
using namespace std;
int n;
int round_up(double x)
{
    int y=lround(x);
    if (abs(x-y)<1e-7) return y+1;
    if (x-y>1e-7) return y+1;
    return y;
}
long long min(long long x,long long y)
{
    return x>y?y:x;
}
long long max(long long x,long long y)
{
    return x<y?y:x;
}
long long exgcd(long long a,long long b,long long &x,long long &y)
{
    if(a==0)
    {
        x=0;y=1;
        return b;
    }
    else
    {
        long long tx,ty;
        long long d=exgcd(b%a,a,tx,ty);
        x=ty-(b/a)*tx;
        y=tx;
        return d;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int testcase;
    scanf("%d",&testcase);
    for (int ii=1;ii<=testcase;++ii)
    {
        scanf("%d",&n);
        if (!n)
        {
            printf("Case #%d: INSOMNIA",ii);
            if (ii<testcase) printf("\n");
            continue;
        }
        long long ans=0;
        for (int digit=0;digit<=9;++digit)
        {
            long long toUp=1LL<<62;
            for (int p=0;p<=6;++p)
            {
                long long pp=1;  // pow(10,p)
                for (int i=1;i<=p;++i)
                    pp*=10;
                /*if (pp>n)
                {
                    // shortcut
                    if (digit>0)
                    {
                        double val=pow(10,p)*digit/n;
                        if (val-llround(val)<1e-7) toUp=min(toUp,llround(val)*n);
                        else toUp=min(toUp,ceil(val)*n);
                    }
                    else
                    {
                        toUp=min(toUp,n);
                    }
                    continue;
                }*/
                for (long long q=0;q<=n;++q)
                {
                    double left=pow(10,p)*(10*q+digit)/n,right=pow(10,p)*(10*q+digit+1)/n;
                    if (abs(left-llround(left))<1e-8)
                    {
                        if (llround(left)==0)
                        {
                            // [0,1)
                            continue;
                        }
                        else
                        {
                            toUp=min(toUp,llround(left)*n);
                            break;
                        }
                    }
                    else if (abs(right-llround(right))<1e-8)
                    {
                        long long k=(long long)ceil(left);
                        if (k==llround(right))
                        {
                            continue;
                        }
                        else
                        {
                            toUp=min(toUp,k*n);
                            break;
                        }
                    }
                    else
                    {
                        long long k=(long long)ceil(left);
                        if (k<right || abs(k-right)<1e-8)
                        {
                            toUp=min(toUp,k*n);
                            break;
                        }
                        else continue;
                    }
                }
            }
            ans=max(ans,toUp);
        }
        printf("Case #%d: %lld",ii,ans);
        if (ii<testcase) printf("\n");
    }
    return 0;
}
