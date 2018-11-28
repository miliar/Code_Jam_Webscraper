#include<cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ret","w",stdout);
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        long long R,T;
        scanf("%I64d%I64d",&R,&T);
        long long l=1,r=((long long)1e18)+100;
        while(l+1<r)
        {
            long long mid=(l+r)/2;
            long long tmp=T/mid;
            if(tmp>=R+R+mid+mid-1)
            {
                l=mid;
            }
            else r=mid;
        }
        printf("Case #%d: %I64d\n",ca,l);
    }
}
