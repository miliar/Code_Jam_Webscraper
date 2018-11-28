#include<bits/stdc++.h>
#define lli long long int
using namespace std;
lli st[1000005];
lli rev(lli n)
{
    lli b,c=0;
    while(n>0)
    {
        b=n%10;
        c=c*10+b;
        n/=10;
    }

return c;
}
lli pre()
{
    lli r;
    int i;
    st[0]=0;
    for(i=1;i<=10;i++)
        st[i]=st[i-1]+1;

    for(int i=11;i<=1000000;i++)
    {
        r=rev(i);
        if(i%10!=0 && r!=i && st[r]!=-1)
            st[i]=min(st[i-1]+1,st[r]+1);
        else
            st[i]=st[i-1]+1;
    }
}
int main()
{
    int T,i;
    lli n;
    for(i=1;i<=1000005;i++)
        st[i]=-1;

    pre();
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%lld",&n);
        printf("Case #%d: %lld\n",i,st[n]);
    }
    return 0;
}
