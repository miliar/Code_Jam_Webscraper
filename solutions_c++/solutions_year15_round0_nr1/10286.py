/*
#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:0x800000")
*/
#include <cassert>
#include <cctype>
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

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }


#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define F(i, n) for(int (i)=0;(i)<(n);++(i))
#define rep(i, s, t) for(int (i)=(s);(i)<=(t);++(i))
#define urep(i, s, t) for(int (i)=(s);(i)>=(t);--(i))
#define repok(i, s, t, o) for(int (i)=(s);(i)<=(t) && (o);++(i))
#define MEM0(addr) memset((addr), 0, sizeof((addr)))
#define MP(x, y) make_pair(x, y)
#define REV(s, e) reverse(s, e)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define ll long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define ls u << 1
#define rs u << 1 | 1
#define lson l, mid, u << 1
#define rson mid, r, u << 1 | 1

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
const int MAXN = 5000000;


int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,kase=1;
    string s;
    int ma;
    scanf("%d",&t);
    while(t--){
        cin >> ma >> s;
        int tmp = s[0]-'0';
        int ans = 0;
        rep(i,1,ma){
            int flag = s[i]-'0';
            if(i > tmp&&flag)
            {
                ans+=(i-tmp);
                tmp = i;
            }
            tmp+=flag;
        }
        printf("Case #%d: %d\n",kase++,ans);
    }
    return 0;
}
