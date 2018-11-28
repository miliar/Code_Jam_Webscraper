#include<cstdio>
typedef long long LL;
LL mustwin(LL who,int n)
{
    LL ret=0;
    for(int i=0;i<n;i++)
    {
        ret<<=1;
        if(who)
        {
            who--;
            who>>=1;
            ret|=1;
        }
    }
    return ret;
}
LL canwin(LL who,int n)
{
    LL ret=0;
    //printf("ccc%I64d ",who);
    who=(1LL<<n)-who-1;
    //printf("%I64d",who);
    for(int i=0;i<n;i++)
    {
        ret<<=1;
        if(who)
        {
            who--;
            who>>=1;
        }
        else ret|=1;
    }
    //printf(" %I64d\n",ret);
    return ret;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int n;
        LL p;
        scanf("%d%I64d",&n,&p);
        p--;
        LL r1,r2;
        LL l,r;
        l=0,r=(1LL<<n);
        while(l+1<r)
        {
            LL mid=(l+r)>>1;
            if(mustwin(mid,n)<=p)
            {
                l=mid;
            }
            else r=mid;
        }
        r1=l;
        l=0,r=(1LL<<n);
        while(l+1<r)
        {
            LL mid=(l+r)>>1;
                    //printf("%I64d %I64d %I64d\n",l,r,mid);
            if(canwin(mid,n)<=p)
            {
                l=mid;
            }
            else r=mid;
        }
        r2=l;
        printf("Case #%d: %I64d %I64d\n",ca,r1,r2);
    }
}
