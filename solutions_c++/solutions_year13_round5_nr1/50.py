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
int Case;
LL b;
int n;
LL A[40];
long double gao(LL bet){
    LL lb = b;
    vector<LL> g;
    g.resize(0);
    long double use = 0;
    for (int i = 0 ; i < 37 ; ++i) if (A[i] <= bet){
        lb -= bet - A[i];
        g.PB(bet - A[i]);
    }
    sort(ALL(g));
    long double ans = 0;
//    cout << lb << endl;
    for (int i = g.size() - 1 ; i >=0 ; --i){
//            printf("G %lld\n" , g[i]);
        int has = g.size() - i;
        use += g[i];
//        printf("ENUM %d use %.12lf last %lld  has %d\n" , i , use , b - (lb - i) , has);
//        printf("betlast %lld use %d has %d %.12lf _ %.12lf\n" , lb , i , has , use , use * 36. / has - use - i);
        if (lb >= i){
            checkMax(ans , use * 36. / (long double)has - b + (lb - i));
        }
    }
//    cout << ans << endl;
    return ans;
}
void solve(){
    scanf("%lld %d" , &b , &n);
    RST(A);
    for (int i = 0 ; i < n ; ++i) scanf("%lld" , &A[i]);
    LL low = 0 , high = 1e15 , mid , ret = 0;
    long double ans = 0;
    do{
        mid = low + high >> 1;
        LL use = 0;
        for (int i = 0 ; i < 37 ; ++i) if (A[i] < mid)
            use += mid - A[i];
        if (use <= b){
            checkMax(ret , mid);
            low = mid + 1;
        }
        else high = mid - 1;
    }while(low <= high);

    for (LL i = max(0ll , ret - 10000) ; i <= ret  ; ++i){
//            printf("bet %lld:\n" , i);
        checkMax(ans , gao(i));
    }
    double out = ans;
    printf("Case #%d: %.12lf\n" , ++Case , out);
}
int main(){
    freopen("A-large.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    Case = 0;
    int _;
    cin >> _;
    while(_--) solve();
}
