//BISMILLAHIRRAMANIRRAHIM

/*
USER: mostafiz13
TASK: A. Standing Ovation
ALGO:
*/

//#pragma warning (disable: 4786)
//#pragma comment(linker, "/STACK:16777216")
//#define _CRT_SECURE_NO_WARNINGS 1

#include <bits/stdc++.h>
/*
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <stack>
#include <time.h>
#include <vector>
#include <utility>
*/

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define STR string
#define LF double
#define LL long long
#define LLU long long unsigned
#define LLF long long double
#define HD short int
#define HU short unsigned
#define UI unsigned

#define SD(a) scanf("%d", &a)
#define SU(a) scanf("%u", &a)
#define SHD(a) scanf("%hd", &a)
#define SHU(a) scanf("%hu", &a)
#define SLLD(a) scanf("%lld", &a)
#define SLLU(a) scanf("%llu", &a)
#define SF(a) scanf("%f", &a)
#define SLF(a) scanf("%lf", &a)
#define SC(a) scanf("%c", &a)
#define SS(a) scanf("%s", a)
#define PCASE printf("Case %d: ", ++Case)
#define NL printf("\n")

#define rep(i, a, b) for(LL i = a ; i < b ; i++)
#define rev(i, b, a) for(LL i = b ; i > a ; i--)
#define foreach(i, n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)

#define CLR(a) memset(a, 0, sizeof(a))
#define SET(a) memset(a, -1, sizeof(a))
#define MEM(a, v) memset(a, v, sizeof(a))
#define CPY(d, s) memcpy(d, s, sizeof(s))

#define PII pair< int, int >
#define PPI pair< int, PII >
#define PSI pair< string, int >
#define PIS pair< int, string >
#define VI vector< int >
#define VI2D vector< VI >
#define VS vector< string >
#define VPII vector< PII >
#define MII map< int, int >
#define MSI map< string, int >
#define MIS map< int, string >
#define MSS map< string, string >
#define M2dII map<int, map<int, int> >
#define QI queue< int >
#define SI stack< int >

#define ff first
#define ss second
#define ALL(a) a.begin(), a.end()
#define SZ(a) (int)a.size()
#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define EPS 1e-9
#define INF (1<<29)
#define inf 0x7f7f7f7f
#define MAX int(1e6)

#define isEqual(a, b) fabs(a-b) < EPS
#define log(N, B) (log10l(N))/(log10l(B))
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )

#define BCHK(a,k) ((bool)(a&(1<<(k))))
#define BSET0(a,k) (a&(~(1<<(k))))
#define BSET1(a,k) (a|(1<<(k)))

using namespace std;

template < class T> T _abs(T n) { return (n < 0 ? -n : n); }
template < class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template < class T > T _min(T a, T b) { return (a < b ? a : b); }
template < class T > T sq(T n) { return n * n ; }
template < class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template < class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template < class T > T power(T N,T P){ if(P==0) return 1; return (P==1)?  N: N*power(N,P-1); }
template < class T > double dist(T a, T b) { return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));}
template < class T > string tostring(T n) { stringstream ss; ss << n; return ss.str();}
template < class T > string itoa(T a) { if(!a) return "0"; string ret; for(T i=a; i>0; i=i/10) ret.PB((i%10)+48); reverse(ALL(ret));return ret;}
template < class T > inline T mod(T n,T m) { return (n%m+m)%m;} /// mod Positive-Negative No

// int dr[] = {0,0,+1,-1}; int dc[] = {+1,-1,0,0}; ///4 Adjacent
// int dr[] = {0,0,+1,-1,-1,-1,+1,+1}; int dc[] = {+1,-1,0,0,-1,+1,-1,+1}; ///8 Adjacent
// int dr[] = {2,1,-1,-2,-2,-1,1,2}; int dc[] = {1,2,2,1,-1,-2,-2,-1}; ///Knight Moves
// int dr[] = {2,1,-1,-2,-1,1}; int dc[] = {0,1,1,0,-1,-1}; ///Hexagonal Direction

int test, Case;
#define debug
#ifdef debug
#define d(a) cout << #a << " := " << a << endl
template<class T1> void D(T1 e){cout<<e<<endl;}
template<class T1,class T2> void D(T1 e1,T2 e2){cout<<e1<<" "<<e2<<endl;}
template<class T1,class T2,class T3> void D(T1 e1,T2 e2,T3 e3){cout<<e1<<" "<<e2<<" "<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void D(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;}
#else
#define d(a)
template<class T1> void D(T1 e){}
template<class T1,class T2> void D(T1 e1,T2 e2){}
template<class T1,class T2,class T3> void D(T1 e1,T2 e2,T3 e3){}
template<class T1,class T2,class T3,class T4> void D(T1 e1,T2 e2,T3 e3,T4 e4){}
#endif // debug
#define _fileinout

int S;
char st[MAX + 7];

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);
  #ifdef _fileinout
    READ("A-large.in");
    WRITE("out.txt");
  #endif // _fileinout
  scanf("%d",&test);
  for(int tc=1; tc<=test; tc++) {
    SD(S); SS(st);
    int cnt=0, cs=0;
    if(st[0]-'0'>0) cs=st[0]-'0';
    else cnt=1, cs=1;
    for(int i=1; i<=S; i++) {
        if(i<=cs) cs+=st[i]-'0';
        else{int x = i-cs; cs += x; cnt+=x; cs+=st[i]-'0';}
    }
    printf("Case #%d: %d\n", ++Case, cnt);
  }
  //while(scanf("%d",&n)==1) {}

  return 0;
}
