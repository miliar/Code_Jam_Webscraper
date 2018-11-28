#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
int main()
{
    freopen("codejamrevengein.txt","r",stdin);
    freopen("codejamrevengeout1.txt","w",stdout);
    int t,n,i,j,k,x;
    char a[105];
    sd(t);
    for(x=1;x<=t;x++)
    {
        ss(a);
        n=strlen(a);
        j=0;
        for(i=n-2;i>=0;i--)
        {
            if(a[i]!=a[i+1])
                j++;
        }
        if(a[n-1]=='-')
            j++;
        printf("Case #%d: %d\n",x,j);
    }
    return 0;
}
