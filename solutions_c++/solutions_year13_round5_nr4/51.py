#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define DO(n) for ( int ____n ## __line__ = n; ____n ## __line__ -- ; )

#define ALL(A) A.begin(), A.end()
#define BSC(A, x) (lower_bound(ALL(A), x) - A.begin())
#define CTN(T, x) (T.find(x) != T.end())
#define SZ(A) int(A.size())
#define PB push_back
#define MP(A, B) make_pair(A, B)
#define fi first
#define se second

typedef long long LL;


typedef vector<int> VI;
typedef map<int, int> MII;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;



template<class T> inline void RST(T &A){memset(A, 0, sizeof(A));}
template<class T> inline void FLC(T &A, int x){memset(A, x, sizeof(A));}
template<class T> inline void CLR(T &A){A.clear();}

//}

/** Constant List .. **/ //{

const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};

const int dx8[] = {-1, 0, 1, 0 , -1 , -1 , 1 , 1};
const int dy8[] = {0, 1, 0, -1 , -1 , 1 , -1 , 1};

const int dxhorse[] = {-2 , -2 , -1 , -1 , 1 , 1 , 2 , 2};
const int dyhorse[] = {1 ,  -1 , 2  , -2 , 2 ,-2 , 1 ,-1};

const int MOD = 1000000007;
//int MOD = 99990001;
const int INF = 0x3f3f3f3f;
const LL INFF = 1LL << 60;
const double EPS = 1e-9;
const double OO = 1e15;
const double PI = acos(-1.0); //M_PI;

//}

template<class T> inline void checkMin(T &a,const T b){if (b<a) a=b;}
template<class T> inline void checkMax(T &a,const T b){if (a<b) a=b;}
//}
template<class T> inline T low_bit(T x) {return x & -x;}
/*****************************************************************/
char A[2000];
int Case;
const int N = 1 << 21;
long double dp[N];
int n;
long double gao(int st){
    if (dp[st] > -EPS) return dp[st];
    if (st == (1 << n) - 1) return 0;
    dp[st] = 0;
    for (int i = 0 ; i < n ; ++i){
        int next = -1;
        int cost = 0;
        for (int j = i ; j < n ; ++j) if (!(st & (1 << (n - j - 1)))){
            next = j ; break;
        }
        if (next == -1){
            for (int j = 0 ; j < i ; ++j)if (!(st & (1 << (n - j - 1)))){
                next = j ; break;
            }
            cost = i - next;
        }
        else cost = n - next + i;
        dp[st] += 1. / n * (cost + gao(st | (1 << (n - 1 - next))));
    }
    return dp[st];
}
void solve(){
    scanf("%s" , A);
    n = strlen(A);
    int s = 0;
    for (int i = 0 ; i < n ; ++i) if (A[i] == 'X')
        s |= 1 << (n - 1 - i);
    for (int i = 0 ; i < N ; ++i) dp[i] = -1;
    double ans = gao(s);
    printf("Case #%d: %.14lf\n",++Case,ans);
}
int main(){
    freopen("D-small-attempt0.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    Case = 0;
    int _;
    cin >> _;
    while(_--) solve();
}
