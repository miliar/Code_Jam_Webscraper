#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%lld",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
int main()
{
    freopen("codejamfractilesin.txt","r",stdin);
    freopen("codejamfractilesout.txt","w",stdout);
    ll t,k,c,s,i,j,x;
    sd(t);
    for(x=1;x<=t;x++)
    {
        sd(k);
        sd(c);
        sd(s);
        j=k;
        for(i=1;i<c;i++)
            j=j*k;
        if(k==1)
            j=1;
        else
            j=(j-1)/(k-1);
        printf("Case #%lld: ",x);
        for(i=0;i<k;i++)
            printf("%lld ",j*i+1);
        printf("\n");
    }
    return 0;
}
