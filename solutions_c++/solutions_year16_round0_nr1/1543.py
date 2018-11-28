#include<bits/stdc++.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define sl(n)       scanf("%lld", &n)
#define sll(a,b)    scanf("%lld %lld", &a, &b)
#define slll(a,b,c) scanf("%lld %lld %lld", &a, &b, &c)
#define D(x)        cout<<#x " = "<<(x)<<endl
#define DBG         pf("Hi\n")
#define pf          printf
#define pii         pair <int, int>
#define pll         pair <LL, LL>
#define pb          push_back
#define PI          acos(-1.00)
#define sz          size()
#define xx          first
#define yy          second
#define eps         1e-9

typedef long long int LL;
typedef double db;

bool vis[12];
int cnt;
void go(LL a)
{
    while(a)
    {
        int nw = a%10;
        if(!vis[nw])
            cnt++;
        vis[nw] = true;
        a/=10;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i, j, k, cs, t;
    LL n;
    sf(t);
    FRE(cs,1,t)
    {
        cnt = 0;
        mem(vis,0);
        sl(n);
        pf("Case #%d: ",cs);
        if(!n)
        {
            pf("INSOMNIA\n");
            continue;
        }
        LL a = n;
        while(true)
        {
            go(a);
            if(cnt == 10)
            {
                pf("%lld\n",a);
                break;
            }
            a+=n;
        }
    }
    return 0;
}


