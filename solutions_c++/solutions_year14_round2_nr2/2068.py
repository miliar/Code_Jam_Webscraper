#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

#define ll long long

ll t,a,b,c,d;

void init()
{
    ll i,j,k,l;
    d=0;
    for(i=0;i<a;i++)
        for(j=0;j<b;j++)
            if((i&j)<c)
                d++;
}

void solve()
{
    printf("Case #%lld: %lld\n",++t,d);
}

int main()
{
    scanf("%*d");
    while(~scanf("%lld%lld%lld",&a,&b,&c))
    {
        init();
        solve();
    }
    return 0;
}
