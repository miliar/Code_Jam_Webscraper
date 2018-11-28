#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <ctype.h>

using namespace std;

#define print(a) cout<< a <<endl
#define print2(a,b) cout<< a <<" "<< b <<endl
#define print3(a,b,c) cout<< a <<" "<< b <<" "<< c <<endl
#define pb push_back
#define popb pop_back
#define mem(name, x) memset(name, x, sizeof(name))
#define rep(i,n) for(i=0;i<(int)(n);i++)
#define rep2(i,n) for(i=1; i<=(int)(n); i++)
#define SZ(x) (int)x.size()
#define PI (2*acos(0))
#define ERR 1e-7
#define EQ(a,b)(fabs(a-b)<ERR)
#define lookalike scanf("%*d")
#define fst first
#define snd second
#define PQ priority_queue
#define LOG(x,BASE) (log10(x)/log10(BASE))
#define INFI 1<<30
#define makep(x, y) make_pair(x, y)
#define LOJ(a, b) printf("Case %d: %d\n", a, b)
#define popcount __builtin_popcount
#define All(a) (a.begin(), b.end())
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Reverse(x) reverse(x.begin(),x.end())


typedef unsigned long long ULL;
typedef long long ll;
typedef pair<int,int> paii;
typedef pair<int, string> pais;

template<class T> inline T lcm(T a,T b)
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/(gcd(a,b)));}
template<class T> inline T gcd(T a,T b)
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

template<class T1> void deb(T1 e){cout<<e<<endl;}
template<class T1,class T2> void deb(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;}

int bigmod(ll b, ll p, ll m){ ll r=1;while(p>0){if(p%2==1)r=(r * b ) % m;p/=2;b = ( b * b) % m;}return r; }

void BINARY(int n){cout<<"Mask: ";for(int i=10;i>=0;i--) if(n&(1<<i))cout<<1;else cout<<0;cout<<endl;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

#define MAX 1000005

vector <int> v;
int maximum;
int dp[102][MAX], N, visit[102][MAX], loop=0;

int rec(int cur, int a)
{
    if(cur==N) return 0;
    if(a>maximum) return 0;
    int &ret = dp[cur][a]; int &vis = visit[cur][a];
    if(vis == loop) return ret;
    ret = INFI; vis = loop;
    if(v[cur]<a) ret = min(ret, rec(cur+1, a+v[cur]));
    else
    {
        ret = min(ret, rec(cur, a+a-1)+1);
        ret = min(ret, rec(cur+1, a)+1);
    }
    return ret;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k, kase=0, t, a, n, x;
    scanf("%d", &t);
    while(t--)
    {
        loop++;
        scanf("%d %d", &a, &N);
        v.clear();
        for(i=0; i<N; i++) { scanf("%d", &x); v.pb(x); }
        sort(v.begin(), v.end());
        maximum = v[N-1];
//        mem(dp, -1);
        int result = rec(0, a);
        printf("Case #%d: %d\n", ++kase, result);
    }
    return 0;
}
