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
int _ , Case;
LL n , p;
LL gao(){
    LL low = 1 , high = 1ll << n , mid;
    while(low < high){
        mid = (low + high + 1) >> 1;
        LL res = 0 , b = mid - 1;
        for (LL i = 1 ; i <= n; ++i)
            if (b == 0) res <<= 1;
            else{
                res = res << 1 | 1;
                b--;
                b >>= 1;
            }
        if (res + 1 <= p) low = mid;
        else high = mid - 1;
    }
    return low - 1;
}
LL gaogao(){
    LL low = 1 , high = 1ll << n , mid;
    while(low < high){
        mid = (low + high + 1) >> 1;
        LL res = 0 , b = (1ll << n) - mid;
        for (LL i = 1 ; i <= n; ++i)
            if (b == 0) res = res << 1 | 1;
            else{
                res = res << 1;
                b--;
                b >>= 1;
            }
        if (res + 1 <= p) low = mid;
        else high = mid - 1;
    }
    return low - 1;
}
void solve(){
    scanf("%lld %lld", &n , &p);
    printf("Case #%d: %lld %lld\n" , ++Case , gao() , gaogao());
}
int main(){
    freopen("B-large.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    cin >> _; Case = 0;
    while(_--) solve();
}
