#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>
//#include "sdf.hpp"

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ft(a) __typeof((a).begin())
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)

typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 1000 + 7;
const int M = 42;
const int mid = M / 2;
const int mod = 1e9 + 9;
const int inf = 1e9 + 7;
const ll linf = 1ll * inf * inf;
const double pi = acos(-1);
const double eps = 1e-7;
const double ep = 1e-5;
const int maxn = 1e5 + 7;
const double PI = acos(-1);

double p[N];
int n, k;
double dp[N][N];

void solve() {
    cin >> n >> k;
    rep(i, 0, n) scanf("%lf", &p[i]);
    sort(p, p + n);
    double ans = 0;
    vi list;
    
    for(int first = 0; first < k; first ++) {
        list.clear();
        rep(i, 0, first + 1) list.push_back(i);
        rep(i, 0, k - first - 1) list.push_back(n - i - 1);
        //cout << list.size() << " " << k << "\n";
        dp[0][0] = 1;
        for(int i = 1; i <= k; i++) {

            double cur = p[list[i - 1]];
            dp[i][0] = dp[i-1][0] * (1 - cur);
            for(int j = 1; j <= k / 2; j++) {
                dp[i][j] = dp[i-1][j-1] * cur + dp[i-1][j] * (1 - cur);
            }
        }
        ans = max(ans, dp[k][k / 2]);
    }
    list.clear();
    rep(i, 0, k) list.push_back(n - i - 1);
    dp[0][0] = 1;
    for(int i = 1; i <= k; i++) {
        double cur = p[list[i - 1]];
        dp[i][0] = dp[i-1][0] * (1 - cur);
        for(int j = 1; j <= k / 2; j++) {
            dp[i][j] = dp[i-1][j-1] * cur + dp[i-1][j] * (1 - cur);
        }
    }
    ans = max(ans, dp[k][k / 2]);
    
//    rep(mask, 0, 1 << n) {
//        if (__builtin_popcount(mask) == k) {
//            list.clear();
//            rep(i, 0, n) if (mask & (1 << i))
//                list.push_back(i);
//            for(int i = 0; i <= k; i++)
//                for(int j = 0; j <= k / 2; j++) dp[i][j] = 0;
//            
//            dp[0][0] = 1;
//            for(int i = 1; i <= k; i++) {
//                
//                double cur = p[list[i - 1]];
//                dp[i][0] = dp[i-1][0] * (1 - cur);
//                for(int j = 1; j <= k / 2; j++) {
//                    dp[i][j] = dp[i-1][j-1] * cur + dp[i-1][j] * (1 - cur);
//                }
//            }
//            ans = max(ans, dp[k][k / 2]);
//        }
//    }
//    
//    rep(mask, 0, 1 << n) {
//        if (__builtin_popcount(mask) == k) {
//            list.clear();
//            rep(i, 0, n) if (mask & (1 << i))
//                list.push_back(i);
//            for(int i = 0; i <= k; i++)
//                for(int j = 0; j <= k / 2; j++) dp[i][j] = 0;
//            
//            dp[0][0] = 1;
//            for(int i = 1; i <= k; i++) {
//                
//                double cur = p[list[i - 1]];
//                dp[i][0] = dp[i-1][0] * (1 - cur);
//                for(int j = 1; j <= k / 2; j++) {
//                    dp[i][j] = dp[i-1][j-1] * cur + dp[i-1][j] * (1 - cur);
//                }
//            }
//            //ans = max(ans, dp[k][k / 2]);
//            if (abs(ans - dp[k][k / 2]) < eps) {
//                rep(i, 0, list.size()) {
//                    cout << list[i] << " ";
//                }
//                puts("");
//            }
//        }
//    }
    
    
    printf("%.6lf\n", ans);
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
#endif
    //init();
    //freopen("landscape.in", "r", stdin); freopen("landscape.out", "w", stdout);
    
    
    int T = 1;
    cin >> T;
    rep(i, 1, T + 1) {
        printf("Case #%d: ", i);
        solve();
    }
    
}