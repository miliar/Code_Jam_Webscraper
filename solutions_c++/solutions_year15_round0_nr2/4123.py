//Abinash Ghosh(Om)
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <sstream>
#include <algorithm>
#include <ctime>
#include <cassert>
using  namespace  std;

#define PI acos(-1.0)
#define MAX 10000007
#define EPS 1e-9
#define mem(a,b) memset(a,b,sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define Sort(x) sort(x.begin(),x.end())
#define FOR(i, b, e) for(int i = b; i <= e; i++)
#define FORR(i, b, e) for(int i = b; i >= e; i--)
#define pr(x) cout<<x<<"\n"
#define pr2(x,y) cout<<x<<" "<<y<<"\n"
#define pr3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n";
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

typedef  long long ll;
typedef  pair <int, int> pii;
typedef  pair <double , double> pdd;
typedef  pair <ll , ll > pll;
typedef  vector <int> vi;
typedef  vector <pii> vpii;
typedef  vector <ll > vl;
//ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
//ll powmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};
//int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};
//int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction


void show(vi x)
{
    FOR(i,0,x.size()-1)
    printf("%d ",x[i]);
    printf("\n");
}
int mincal(vi a)
{
    //show(a);
    vi b=a,e=a;
    int SZ=a.size();
    //pr(SZ);
    int ans1=a[SZ-1];
    int ans2=0;
    int cnt=0;
    vi c,d;
    if(ans1>3)
    {
        FORR(i,SZ-1,0)
        {
            if(ans1==a[i])
            {
                b.erase(b.begin()+i);
                cnt++;
                if(ans1%2==0)
                {
                    c.pb(ans1/2);
                    c.pb(ans1/2);
                   // pr2("aa=",ans1/2);
                }
                else
                {
                    c.pb(ans1/2);
                    c.pb((ans1/2)+1);
                   // pr2("a=",ans1/2);
                }
            }
            else break;
        }
        FOR(i,0,c.size()-1)
        b.push_back(c[i]);
    }
    int cnt2=0;
    if(ans1==9)
    {
        FORR(i,SZ-1,0)
        {
            if(ans1==a[i])
            {
                cnt2++;
                e.erase(e.begin()+i);
                d.pb(6);
                d.pb(3);
                //pr3("aaa=",6,3);
            }
            else break;
        }
        FOR(i,0,d.size()-1)
        e.push_back(d[i]);
        Sort(e);
    }
    //pr2(c[0],c[1]);
    ans2+=cnt;
    Sort(b);
    //ans2+=b[b.size()-1];
    //pr2("ans2",ans2);

    int res=ans1;
    if(res>3&&ans2<res)res=min(res,ans2+mincal(b));
    //pr("..........................\n");
    if(res>3&&cnt2<res&&ans1==9){res=min(res,cnt2+mincal(e)); }

    return res;
}
int main()
{
    READ("B-small-attempt4.in");
    WRITE("out.out");
    int T,d,P;
    vi a;
    scanf("%d",&T);
    FOR(t,1,T)
    {
        scanf("%d",&d);
        FOR(i,1,d)
        {
            scanf("%d",&P);
            a.pb(P);
        }
        Sort(a);
        int res=mincal(a);
        printf("Case #%d: %d\n",t,res);
        a.clear();
    }
    return 0;
}


