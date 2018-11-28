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


const int N = 1 << 15;
char t[N];
char x[] = { 'S', 'P', 'R' };
int ts, tp, tr;

void f(char c) {
    if (c == 'S') --ts;
    if (c == 'R') --tr;
    if (c == 'P') --tp;
}

void resort(string &s, int l, int r) {
    if (l == r) return;
    int m = (r + l) >> 1;
    int len = (r - l + 1) / 2;
    resort(s, l, m);
    resort(s, m+1, r);
    string a = s.substr(l, len);
    string b = s.substr(m + 1, len);
    if (a > b)
        for (int i = 0; i < len; ++i)
            swap(s[l + i], s[m + 1 + i]);
    
}

void Tcase(int test) {
    int n;
    int s, p, r;
    cin >> n >> r >> p >> s;
    int nn = (1 << n);
    string ans = "Z";
    for (int ptr = 0; ptr < 3; ++ptr) {
        t[1] = x[ptr];
        ts = s, tp = p, tr = r;
        for (int i = 1; i < nn; ++i) {
            if (t[i] == 'S') {
                t[i << 1] = 'P';
                t[i << 1 | 1] = 'S';
            }
            if (t[i] == 'R') {
                t[i << 1] = 'R';
                t[i << 1 | 1] = 'S';
            }
            if (t[i] == 'P') {
                t[i << 1] = 'P';
                t[i << 1 | 1] = 'R';
            }
        }
        for (int i = nn; i < (nn << 1); ++i) {
            f(t[i]);
            //cout << t[i];
        }
        //cout << '\n';
        if (!ts && !tp && !tr) {
            string cur = "";
            for (int i = nn; i < (nn << 1); ++i)
                cur += t[i];
            resort(cur, 0, sz(cur) - 1);
            ans = min(ans, cur);
        }
    }
    if (ans == "Z") ans = "IMPOSSIBLE";
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
    cout.precision(10);
    
    
    
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