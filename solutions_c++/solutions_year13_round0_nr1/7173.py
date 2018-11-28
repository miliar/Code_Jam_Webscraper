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

#define MAX 50

vector <string> v;

bool Check(char ch)
{
    int i,j;
    bool flag;
    for(i=0; i<4; i++)
    {
        flag = true;
        for(j=0; j<4; j++) {
            if(v[i][j]!=ch and v[i][j]!='T') flag = false;
        }
        if(flag) return flag;
        flag = true;
        for(j=0; j<4; j++){
            if(v[j][i]!=ch and v[j][i]!='T') flag = false;
        }
        if(flag) return flag;
    }
    flag = true;
    for(i=0; i<4; i++) if(v[i][i]!=ch and v[i][i]!='T') flag = false;
    if(flag) return flag;
    flag = true;
    for(i=0, j=3; i<4; i++, j--) if(v[i][j]!=ch and v[i][j]!='T') flag = false;
    return flag;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, kase=0, n, t;
    scanf("%d ", &t);
    string s;
    while(t--)
    {
        v.clear();
        for(i=0; i<4; i++) { cin >> s; v.pb(s); }
        if(Check('O')) { printf("Case #%d: O won\n", ++kase); continue; }
        if(Check('X')) { printf("Case #%d: X won\n", ++kase); continue; }
        bool flag = false;
        for(i=0; i<4; i++) for(j=0; j<4; j++) if(v[i][j]=='.') flag = true;
        if(flag) printf("Case #%d: Game has not completed\n", ++kase);
        else printf("Case #%d: Draw\n", ++kase);
    }
    return 0;
}

















