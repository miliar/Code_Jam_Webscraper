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


const int N = 100;

string v[N];
int g[5][5];
int rb[5];
int wk[5];
int f[5];
int ff[5];
int ued[5];

void Tcase(int test) {
    int n; cin >> n;
    int edcnt = 0;
    int ans = inf;
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
        for (char c : v[i]) edcnt += (c == '1');
    }
    int s = sqr(n);
    for (int i = 0; i < (1 << s); ++i) {
        
        bool fl = false;
        if (i == 15) {
            fl = fl;
        }
        for (int j = 0; j < s; ++j) {
            g[j / n][j % n] = !!(i & (1 << j));
            if (g[j / n][j % n] == 0 && v[j / n][j % n] == '1') {
                fl = true;
                break;
            }
        }
        if (fl) continue;
        fill(rb, rb+5, 0);
        fill(wk, wk+5, 0);
        for (int w = 0; w < n; ++w) {
            fill(f, f+5, 0);
            fill(ff, ff+5, 0);
            int cntr = 0, cntw = 0;
            for (int r = 0; r < n; ++r)
                if (g[r][w] && !f[r]) {
                    rb[cntr++] = r;
                    f[r] = 1;
                }
            for (int r = 0; r < cntr; ++r)
                for (int ww = 0; ww < n; ++ww)
                    if (g[rb[r]][ww] == 1 && !ff[ww]) {
                        ff[ww] = 1;
                        wk[cntw++] = ww;
                    }
            if (cntr != cntw) fl = true;
            for (int r = 0; r < cntr; ++r)
                for (int w = 0; w < cntw; ++w)
                    fl |= (g[rb[r]][wk[w]] == 0);
        }
        if (!fl) {
            set<int> www;
            set<int> rrr;
            for (int j = 0; j < n; ++j)
                for (int k = 0; k < n; ++k) {
                    if (g[j][k]) {
                        www.insert(j);
                        rrr.insert(k);
                    }
                }
            if (sz(www) == n && sz(rrr) == n)
                ans = min(ans, bits(i) - edcnt);
        }
    }
    cout << "Case #" << test << ": " << ans << '\n';
}


int main() {
#ifndef DEBUG
    //freopen("railroad.in", "r", stdin);
    //freopen("railroad.out", "w", stdout);
#else
    freopen("/Users/rzmn/Documents/acm/acm/input.txt", "r", stdin);
    freopen("/Users/rzmn/Documents/acm/acm/output.txt", "w", stdout);
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