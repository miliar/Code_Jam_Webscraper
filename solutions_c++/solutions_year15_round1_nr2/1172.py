#include<cstdio>
#include<algorithm>

using namespace std;

void bs(long long,long long);

int t,b,m[1005],n,mn=2e9,id,c,g[1005];
long long s,a,d;

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B_out_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        mn=2e9;
        scanf("%d%d",&b,&n);
        for(int i=0;i<b;i++)
        {
            scanf("%d",&m[i]);
            mn=min(mn,m[i]);
        }
        bs(0,(long long)mn*n);
        d=a-n;
        c=0;
        for(int i=0;i<b;i++)
        {
            if(s%m[i]==0)
            {
                g[c++]=i+1;
            }
        }
        for(int i=c-1;i>=0;i--)
        {
            if(d>0)
            {
                d--;
                continue;
            }
            id=g[i];
            break;
        }
        printf("Case #%d: %d\n",z,id);
    }
    return 0;
}

void bs(long long l,long long r)
{
    if(l>r)     return;
    long long x=(l+r)/2,ab=0;
    for(int i=0;i<b;i++)    ab+=(x/m[i]+1);
    if(ab>=n)
    {
        s=x;
        a=ab;
        bs(l,x-1);
    }
    else    bs(x+1,r);
}
