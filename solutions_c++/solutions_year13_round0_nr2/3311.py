#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <bitset>
#include <functional>
#include <map>

#define LL(a) (a<<1)
#define RR(a) (a<<1|1)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FOE(i,a,b) for(i=a;i<=b;i++)
#define FOD(i,a,b) for(i=a;i>=b;i--)
#define foreach(it,v) for (__typeof((v).begin()) it = (v).begin();it != (v).end();++it)
#define iter(c) __typeof((c).begin())
#define Clr(a,b) memset(a,b,sizeof(a))
#define Cpy(a,b) memcpy(a,b,sizeof(a))
#define TTI template <class T> inline
#define MP(a,b) make_pair(a,b)
#define fi first
#define se second

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<double,int> pdi;
typedef pair<int,double> pid;

const double eps = 1e-8;
const double pi  = acos(-1.0);
const double inf = 1e20;
const int INF = (~0u)>>2;
const i64 INF64 = (~0uLL)>>2;

inline bool eq(double x, double y) { return (x-y<-eps)?0:x-y<eps; }
TTI T sqr(T x) { return x * x; }
TTI T gcd(T a, T b) { return (b)?gcd(b, a%b): a; }
u64 rand64(){
	return u64(rand()) ^ (u64(rand())<<15) ^ (u64(rand())<<30) ^ (u64(rand())<<45) ^ (u64(rand())<<60);
}
inline bool isAlphabet(char a) {
    return ('a' <= a && a <= 'z') || ('A' <= a && a <= 'Z');
}
inline bool isDigit(char a) {
    return '0' <= a && a <= '9';
}

int mm[140][140];
int hh[140];
int ss[140];

int n, m;

bool solve()
{
    for(int i=0; i<n; i++)
    {
        hh[i] = mm[i][0];
        for(int j=1; j<m; j++)
            hh[i] = max(hh[i], mm[i][j]);
    }
    for(int j=0; j<m; j++)
    {
        ss[j] = mm[0][j];
        for(int i=1; i<n; i++)
            ss[j] = max(ss[j], mm[i][j]);
    }
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            if(mm[i][j] < hh[i] && mm[i][j] < ss[j])
                return false;
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas)
    {
        scanf("%d%d", &n, &m);
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                scanf("%d", &mm[i][j]);
        printf("Case #%d: %s\n", cas, solve() ? "YES":"NO");
    }

    return 0;
}

