/***************************************
    codeforces = topcoder = sahedsohel
    IIT,Jahangirnagar University(42)
****************************************/
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

#define ll long long int
#define ull unsigned long long int
#define inf (INT_MAX/10)
#define linf (LLONG_MAX/10LL)
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define fl(c,i,n) for(i=c;i<n;i++)
#define f(i,n) for(i=0;i<n;i++)
#define mem(a) memset(a,0,sizeof(a))
#define memn(a) memset(a,-1,sizeof(a))
#define pb push_back
#define pp pop_back()
#define aov(a) a.begin(),a.end()
#define mpr make_pair
#define PI (2.0*acos(0.0)) //#define PI acos(-1.0)
#define xx first
#define yy second
#define mxv(a) *max_element(aov(a))
#define mnv(a) *min_element(aov(a))
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define to_c_string(a) a.c_str()
#define strtoint(c) atoi(&c[0])
#define pii pair< int , int >
#define pll pair< ll , ll >
#define pcs(a) printf("Case %d: ", a)
#define nl puts("")
#define dbg(x) cout<<#x<<" : "<<x<<endl

template <class T> inline T bigmod(T p,T e,T M){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p) % M;p = (p * p) % M;}return (T)ret;}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}   // M is prime}
template <class T> inline T bpow(T p,T e){ll ret = 1;for(; e > 0; e >>= 1){if(e & 1) ret = (ret * p);p = (p * p);}return (T)ret;}

int toInt(string s){int sm;stringstream ss(s);ss>>sm;return sm;}
int toLlint(string s){long long int sm;stringstream ss(s);ss>>sm;return sm;}


///int mnth[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int dx[]={-1,-1,+0,+1,+1,+0};int dy[]={-1,+1,+2,+1,-1,-2}; //Hexagonal Direction
///const double eps=1e-6;
///int dx[]={0,1,0,-1};
///int dy[]={1,0,-1,0}; //4 Direction

/*****************************************************************/
///////////////////////   GET SET GO    ///////////////////////////
/*****************************************************************/

#define M 100005
#define MX 100005
#define MD 1000000007LL

///  0 1 2 3   4  5  6  7
///  1 i j k  -1 -i -j -k


char tl[8][8]={ 0,1,2,3, 4,5,6,7,
                1,4,3,6, 5,0,7,2,
                2,7,4,1, 6,3,0,5,
                3,2,5,4, 7,6,1,0,

                4,5,6,7, 0,1,2,3,
                5,0,7,2, 1,4,3,6,
                6,3,0,5, 2,7,4,1,
                7,6,1,0, 3,2,5,4
                };

int bl[3][9][10009],cs;
int ln,n;
char s[10009];

bool dp(char fl,char ls,int i)
{
    if(i==n)
    {
        if(fl==2&&ls==3)
            return 1;
        return 0;
    }

    if(bl[fl][ls][i]==cs)
        return 0;
    bl[fl][ls][i]=cs;

    if(fl==0&&(ls==1||ls==5))
    {
        if(dp(1,(ls==5)?4:0,i))
            return 1;
    }
    if(fl==1&&(ls==2||ls==6))
    {
        if(dp(2,(ls==6)?4:0,i))
            return 1;
    }

    if(dp(fl,tl[ls][ s[(i%ln)]-'i'+1 ],i+1))
        return 1;
    return 0;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,i,j,k;
    cs=1;
    sc(t);
    while(t--)
    {
        scanf("%d %d %s",&ln,&n,s);
        n*=ln;
        if(dp(0,0,0))
            printf("Case #%d: YES\n",cs++);
        else
            printf("Case #%d: NO\n",cs++);
    }

    return 0;
}



