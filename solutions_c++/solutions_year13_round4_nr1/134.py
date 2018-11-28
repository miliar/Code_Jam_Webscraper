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

const LL MOD = 1000002013LL;
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
LL n;
LL g(LL x){
    if (x == 0) return 0;
    LL P = (2ll * n + 1 - x) * x / 2ll;
    return P % MOD;
}
const int N = 3e3 + 9;

int m;
struct Station{
    LL x , y , p;
    void input(){
        scanf("%lld%lld%lld" , &x , &y , &p);
    }
}A[N];
bool isin(LL x , LL l , LL r){
    return l <= x && x <= r;
}
bool inter(Station P , Station Q){
    return isin(P.x , Q.x , Q.y) || isin(P.y , Q.x , Q.y) || isin(Q.x , P.x , P.y) || isin(Q.y , P.x , P.y);
}
bool use[N];
void ADD(LL &x , LL y){
    x += y;
    x %= MOD;
}
vector< PLL > st , en;
LL hash[N << 3];
int tot;
void dfs(int x){
    use[x] = 1;
    st.PB(MP(A[x].x , A[x].p));
    en.PB(MP(A[x].y , A[x].p));
    for (int i = 0 ; i < m ; ++i) if (!use[i]){
        if (inter(A[x] , A[i])) dfs(i);
    }
}
void solve(){
    scanf("%lld%d" , &n , &m);
    LL oans = 0;
    tot = 0;
    for(int i = 0 ; i < m ; ++i){
        A[i].input();
        oans += g(A[i].y - A[i].x) * A[i].p % MOD;
//        hash[tot++] = A[i].x;
//        hash[tot++] = A[i].y;
    }
//    cout << oans << endl;
//    sort(hash , hash + tot);
//    tot = unique(hash , hash + tot) - hash;
    LL ans = 0;
    RST(use);
    for (int i = 0 ; i < m ; ++i) if (!use[i]){
        st.resize(0);
        en.resize(0);
        dfs(i);
        sort(ALL(st));sort(ALL(en));

//for (int t = 0 ; t < st.size() ; ++t) printf("ST %lld %lld\n" , st[t].fi , st[t].se);
//for (int t = 0 ; t < en.size() ; ++t) printf("EN %lld %lld\n" , en[t].fi , en[t].se);
        int tail = en.size() - 1;
        for(int j = st.size() - 1 ; j >= 0 ; --j){
            while(tail > 0 && en[tail - 1].fi >= st[j].fi) -- tail;
            int k = tail;
            while(st[j].se){
                LL go = min(st[j].se , en[k].se);
                ADD(ans , g(en[k].fi - st[j].fi) * go % MOD);
                en[k].se -= go;
                k++;
                st[j].se -= go;
            }
        }
    }
//    cout << ans << endl;
    ans = oans - ans;
    ans = (ans % MOD + MOD) % MOD;
    printf("Case #%d: %lld\n" , ++Case , ans);
}
int main(){
    freopen("A-large.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    Case = 0;
    st.reserve(10000);
    en.reserve(10000);
    cin >> _;
    while(_--) solve();
}
