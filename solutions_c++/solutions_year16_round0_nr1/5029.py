//OM
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <algorithm>
using  namespace  std;

#define  x first
#define  y second
#define  pb push_back
#define  mp make_pair
#define  PI (acos(-1.0))
#define  mem(a,b) memset(a,b,sizeof(a))
#define  Sort(x) sort(x.begin(),x.end())
#define  FOR(i, b, e) for(int i = b; i <= (int)(e); i++)
#define  FORR(i, b, e) for(int i = b; i >=(int)(e); i--)
#define  FORI(i, s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
#define  pr(x) cout<<x<<"\n"
#define  prs(x) cout<<x<<" "
#define  pr2(x,y) cout<<x<<" "<<y<<"\n"
#define  pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
#define  ppr(a) cout<<a.x<<" "<<a.y<<"\n"

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double , double> pdd;
typedef  vector <int> vi;
typedef  vector <pii> vpii;

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction

#define  EPS 1e-9
#define  MAX 1000007
int ache[11];
bool cover(ll n)
{
    while(n>0)
    {
        ache[n%10]=1;
        n/=10;
    }
    FOR(i,0,9)if(!ache[i])return false;
    return true;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outl.txt", "w", stdout);
    int T,n;
    scanf("%d",&T);
    FOR(cs,1,T)
    {
        scanf("%d",&n);
        mem(ache,0);
        ll ans=0;
        FOR(i,1,MAX)
        {
            ll now=1LL*i*n;
            if(cover(now)){
                ans=now;
                break;
            }
        }
        if(!ans)printf("Case #%d: INSOMNIA\n",cs);
        else printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}

