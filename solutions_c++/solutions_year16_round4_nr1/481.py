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

const int N = 100 + 7;
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

int n;
int R, P, S;
char c[3];

void DFS(int val, int n) {
    
    //cout << val << ' ' << c[val] << " " << n << "\n";
    if (n == 0) {
        printf("%c", c[val]);
        return;
    }
    if (val == 0) { //
        DFS(0, n - 1);
        DFS(2, n - 1);
    } else {
        if (val == 1) {
            DFS(1, n - 1);
            DFS(0, n - 1);
        } else {
            DFS(1, n - 1);
            DFS(2, n - 1);
        }
    }
}

string dp[4][13];

void solve() {
    c[0] = 'R';
    c[1] = 'P';
    c[2] = 'S';
    cin >> n >> R >> P >> S;
    int sl = 1 << n;
    
    bool ok = true;
    while(sl > 1) {
        if (R > sl / 2) {
            ok = false;
            break;
        }
        int d = sl / 2 - R;
        if (P < d || S < d) {
            ok = false;
            break;
        }
        int nR = S - d, nP = P - d, nS = d;
        R = nR; P = nP; S = nS;
        
        //cout << R << " " << P << " " << S << "\n";
        
        sl /= 2;
    }
    
    //cout << R << " " << P << " " << S << "\n";
    
    if (ok) {
        if (R > 0) cout << dp[0][n] << "\n";
        else if (P > 0) cout << dp[1][n] << "\n";
        else cout << dp[2][n] << "\n";
        //puts("");
    } else {
        puts("IMPOSSIBLE");
    }
    
    
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
#endif
    //init();
    //freopen("landscape.in", "r", stdin); freopen("landscape.out", "w", stdout);
    
    dp[0][0] = 'R';
    dp[1][0] = 'P';
    dp[2][0] = 'S';
    for(int i = 1; i <= 12; i++) {
        dp[0][i] = min(dp[0][i-1] + dp[2][i-1], dp[2][i-1] + dp[0][i-1]);
        dp[1][i] = min(dp[1][i-1] + dp[0][i-1], dp[0][i-1] + dp[1][i-1]);
        dp[2][i] = min(dp[1][i-1] + dp[2][i-1], dp[2][i-1] + dp[1][i-1]);
    }
    int T = 1;
    cin >> T;
    rep(i, 1, T + 1) {
        printf("Case #%d: ", i);
        solve();
    }
    
}