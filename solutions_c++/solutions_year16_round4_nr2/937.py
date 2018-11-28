#include "bits/stdc++.h"


const long double PI(acosl(-1.0));
long double eps = 1e-10;

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)


using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector < ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;


const int N = 402;

ld v[N];
ld x[N];
ld dp[N][N];


void Tcase(int test) {
    int n, k; cin >> n >> k;
    for (int i = 0; i < n; ++i)
        cin >> v[i];
    sort(v, v+n);
    ld ans = -inf;
    for (int hh = 0; hh < (1 << n); ++hh) {
            if (bits(hh) == k) {
                int ptr = 0;
                for (int i = 0; i < n; ++i) {
                    if ((hh & (1 << i)) != 0)
                        x[ptr++] = v[i];
                }
                assert(ptr == k);
                for (int i = 0; i < N; ++i)
                    for (int j = 0; j < N; ++j)
                        dp[i][j] = 0;
                dp[0][0] = 1;
                for (int i = 0; i < ptr; ++i) {
                    for (int j = 0; j < ptr; ++j) {
                        dp[i + 1][j + 1] += dp[i][j] * x[i];
                        dp[i + 1][j] += dp[i][j] * (ld(1) - x[i]);
                    }
                }
                ans = max(ans, dp[ptr][ptr/2]);
            }
        
    }
    cout << "Case #" << test << ": ";
    cout << fixed << ans << '\n';
}


int main() {
#ifndef DEBUG
    //freopen("railroad.in", "r", stdin);
    //freopen("railroad.out", "w", stdout);
#else
    freopen("/Users/rzmn/Documents/acm/acm/input.txt", "r", stdin);
    //freopen("/Users/rzmn/Documents/acm/acm/output.txt", "w", stdout);
#endif
    cout.precision(8);
    
    
    
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    srand(unsigned(time(nullptr)));
    
    
    int T; cin >> T;
    for (int i = 1; i <= T; ++i) {
        Tcase(i);
    }
    
    
    
    
//#ifdef DEBUG
//    cerr << "\n == TIME : " << clock() / ld(CLOCKS_PER_SEC) << " == " << endl;
//#endif
}