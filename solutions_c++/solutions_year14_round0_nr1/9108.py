#include <map>
#include <iterator>
#include <set>
#include <deque>
#include <list>
#include <stack>
#include <cmath>
#include <queue>
#include <ctime>
#include <cfloat>
#include <vector>
#include <string>
#include <cstdio>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <tr1/unordered_map>
  
using namespace std;
using namespace tr1;
 
  
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 1; --i)
#define FORIT(i, a) for( TI(a) i = a.begin(); i != a.end(); i++ )
#define MAXN 1200001
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define FILL(X, V) memset( X, V, sizeof(X) )
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())
#define pb push_back
#define mk make_pair
typedef long long int64;
typedef unsigned long long uint64;
 
struct tri{
    int u, v, a;
    tri ( int u = 0, int v = 0, int a = 0) : u(u), v(v), a(a) { }
    bool operator < (const tri &w) const{
        if( u != w.u ) return u < w.u;
        if( v != w.v ) return v < w.v;
        return a < w.a;
    }
};
  
const  double pi = acos(-1.0);
const  double EPS = 1e-15;
int x[] = {-1,1,0,0};
int y[] = {0,0,-1,1};
  
int cmp(double a, double b = 0.0){ if(fabs(a-b) < EPS) return 0; return a > b ? 1 : -1; }
  
  
#ifdef _WIN32 
    #define getchar_unlocked getchar
    #define putchar_unlocked putchar
#endif
   
bool read( int &n ) {
    n = 0;
    register bool neg = false;
    register char c = getchar_unlocked();
    if( c == EOF) { n = -1; return false; }
    while (!('0' <= c && c <= '9')) {
        if( c == '-' ) neg = true;
        c = getchar_unlocked();
    }
    while ('0' <= c && c <= '9') {
        n = n * 10 + c - '0';
        c = getchar_unlocked();
    }
    n = (neg ? (-n) : (n));
    return true;
}
 
inline void writeInt(int64 n){
    register int idx = 25;
    if( n < 0LL ) putchar_unlocked('-');
    n = abs(n);
    char out[26];
    out[25] = ' ';
    do{
        idx--;
        out[idx] = n % 10 + '0';
        n/= 10;
    }while(n);
    do{ putchar_unlocked(out[idx++]); } while (out[idx] != ' ');
}

vector < int > v1, v2;

int main(){
    ios::sync_with_stdio(false);
    int t, p1, p2, v, c = 1;
    cin >> t;
    while( t-- ){
        cin >> p1; p1--;
        REP(i,4){
            REP(j,4){
                cin >> v;
                if( i == p1 ) v1.pb(v);
            }
        }
        cin >> p2; p2--;
        int ans = -1;
        int qt = 0;
        REP(i,4){
            REP(j,4){
                cin >> v;
                if( i == p2 )  v2.pb(v);
            }
        }
        REP(i,4){
            REP(j,4){
                if( v1[i] == v2[j] ){
                    ans = v1[i];
                    qt++;
                }
            }
        }
        if( qt > 1 ) cout << "Case #" << c++ << ": Bad magician!\n";
        else if( qt == 0 ) cout << "Case #" << c++ << ": Volunteer cheated!\n";
        else cout << "Case #" << c++ << ": " << ans << "\n";
        v1.clear();
        v2.clear();
    }
    return 0;
}    