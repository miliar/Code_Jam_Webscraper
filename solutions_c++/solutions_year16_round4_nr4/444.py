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

int a[N][N];
int n;
string s[10];
bool kt[10];

bool check() {
    vi has;
    
    rep(i, 0, n) {
        has.clear();
        rep(j, 0, n) if (s[i][j] == '1') has.push_back(j);
        //cout << "this " << has.size() << "\n";
        if (has.size() == n) continue;
        if (has.empty()) return false;
        if (has.size() == 1) {
            rep(t, 0, n) if (t != i && s[t][has[0]] == '1') {
                return false;
            }
            continue;
        }
        if (has.size() == 2) {
            rep(u, 0, n) if (u != i)
                rep(v, 0, n) if (v != i && v != u) {
                    if (s[u][has[0]] == '1' && s[v][has[1]] == '1') {
                        return false;
                    }
                }
        }
        if (has.size() == 3) {
            rep(u, 0, n) if (u != i)
                rep(v, 0, n) if (v != i && v != u){
                    int r = 6 - i - u - v;
                    if (s[u][has[0]] == '1' && s[v][has[1]] == '1' && s[r][has[2]] == '1') {
                        return false;
                    }
                }
        }
        
    }
    
    return true;
}

void solve() {
    cin >> n;
    rep(i, 0, n) cin >> s[i];
    vii list;
    list.clear();
    rep(i, 0, n) rep(j, 0, n) if (s[i][j] == '0')
        list.push_back(mk(i, j));
    int ans = inf;
    int sl = list.size();
    rep(mask, 0, 1 << sl) {
        rep(j, 0, sl) {
            if (mask & ( 1 << j)) {
                int u = list[j].first;
                int v = list[j].second;
                s[u][v] = '1';
                //cout << u << " " << v << "\n";
            }
        }
        
        
        
        if (check()) {
            ans = min(ans, __builtin_popcount(mask));
//            if (__builtin_popcount(mask) == 6) {
//                puts("");
//                cout << s[0] << "\n" << s[1] << "\n" << s[2] << "\n" << s[3] << "\n";
//                
//                puts("");
//            }
        }
        
        rep(j, 0, sl) {
            if (mask & ( 1 << j)) {
                int u = list[j].first;
                int v = list[j].second;
                s[u][v] = '0';
            }
        }
    }
    
    cout << ans << "\n";
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