#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <iterator>
#include <numeric>
#include <utility>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define DEBUG if(0)
#define PAUSE system("pause")
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define ALL(c) c.begin(), c.end()
#define PB(x) push_back(x)
#define UB(s, e, x) upper_bound(s, e, x)
#define LB(s, e, x) lower_bound(s, e, x)
#define REV(s, e) reverse(s, e);
#define SZ(c) c.size()
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define LAST(a) (int(a.size()) - 1)
#define PN(n)   printf("%d",n)
#define PDN(n)  printf("%lf",n)
#define PLN(n)  printf("%lld",n)
#define PS(n)   printf("%s",n)
#define PL()    printf("\n")
#define PSP()    printf(" ");
#define SN(n)   scanf("%d",&n)
#define SDN(n)  scanf("%lf",&n)
#define SLN(n)  scanf("%lld",&n)
#define SS(n)   scanf("%s",n)
#define i64 long long
#define ff first
#define ss second

template< class T > T sq(T &x) { return x * x; }
template< class T > T abs(T &n) { return (n < 0 ? -n : n); }
template< class T > T max(T &a, T &b) { return (!(a < b) ? a : b); }
template< class T > T min(T &a, T &b) { return (a < b ? a : b); }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > T mod(T &a, T &b) { return (a < b ? a : a % b); }
template< class T > bool inside(T &a, T &b, T &c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }

const double EPS = 1E-9;
//const int INF = 100000000;
const int INF = 0x3f3f3f3f;
const double PI = 3.1415926535897932384626433832795;
const int MAX = 150;
int dx [] = {-1, 0, 1, 0};		// Fourth rotation
int dy [] = {0, 1, 0, -1};		// Fourth rotation
int nx [] = {-2, -1,  1,  2, 2, 1,-1,-2}; 	// Knight   moves
int ny [] = {-1, -2, -2, -1, 1, 2, 2, 1};	// Knight   moves
int dr [] = {-1, -1, -1,  0, 0, 1, 1, 1};  	// Around 8 moves
int dc [] = {-1,  0,  1, -1, 1,-1, 0, 1};	// Around 8 moves
int arr[4][4];
int brr[16];

int main()
{
    freopen("A-small-attempt1.in","r", stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t;
    SN(t);
    forn(tc, t){
        int k, p, count = 0, d;
        SN(k);
        forn(i, 16 ) brr[i]=0;
        forn(i, 4) forn(j, 4) SN(arr[i][j]);
        forn(i, 4) brr[arr[k-1][i]-1]++;
        SN(d);
        forn(i, 4) forn(j, 4) SN(arr[i][j]);
        forn(i, 4){
            if(brr[arr[d-1][i]-1] != 0){
                p = arr[d-1][i];
                count++;
            }
        }
        PS("Case #"); PN(tc+1); PS(": ");
        if(count==1) PN(p);
        else if(count==0) PS("Volunteer cheated!");
        else if(count>1) PS("Bad magician!");
        PL();
    }
    return 0;
}
