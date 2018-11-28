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
const int N = 30;
int A[N] , B[N] ;
int n;
int Case;
int lis[N];
bool use[N];
int dpa[N] , dpb[N];
FILE *out , *in;
bool check(){
    for (int i = n - 1 ; i >= 0 ; --i){
        dpb[i] = 1;
        for (int j = i + 1 ; j < n ; ++j) if (lis[i] > lis[j])
            checkMax(dpb[i] , dpb[j] + 1);
        if (dpb[i] != B[i]) return false;
    }
    return true;
}
bool dfs(int x){
    if (x >= n){
        if (check()){
            fprintf(out , "Case #%d:" , ++Case);
            for (int i = 0 ; i < n ; ++i) fprintf(out , " %d" , lis[i]);
            fprintf(out , "\n");
            return true;
        }
        return false;
    }
    for (lis[x] = 1 ; lis[x] <= n ; ++lis[x]) if (!use[lis[x]]){
        use[lis[x]] = 1;
        dpa[x] = 1;
        dpb[x] = 1;
        bool ok = true;
        for(int j = 0 ; j < x ; ++j){
            if (lis[j] < lis[x])
                checkMax(dpa[x] , dpa[j] + 1);
        }
        if (dpa[x] == A[x] && ok)
            if(dfs(x + 1)) return true;
        use[lis[x]] = 0;
    }
    return false;
}
void solve(){
    fscanf(in , "%d" , &n);
    for(int i = 0 ; i < n ; ++i) fscanf(in ,"%d" , &A[i]);
    for(int i = 0 ; i < n ; ++i) fscanf(in , "%d" , &B[i]);
    RST(use);
    dfs(0);
    cout << Case << endl;
}
int main(){
    in = fopen("0.in" , "r");
    out = fopen("0.out" , "w");
//    freopen("0.out" , "w" , stdout);
    int _;
    fscanf(in , "%d" , &_);Case = 0;
    while(_--) solve();
}
