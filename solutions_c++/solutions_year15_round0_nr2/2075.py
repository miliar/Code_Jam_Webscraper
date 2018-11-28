#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for(int i = 0; i < (int)n; ++i)
#define repf(i, f, l) for(int i = f; i < (int)l; ++i)

#ifdef ONLINE_JUDGE
#define DEBUG false
#else
#define DEBUG true
#endif

#define pb emplace_back
#define lb lower_bound
#define ul unsigned long
#define ull unsigned long long
#define ll long long
#define INF 1000000007
#define MOD 1000000007
#define fs first
#define sd second

#define ALL(c) (c).begin(),(c).end()

#define DBG0(x)    {if(DEBUG){ cout << #x << ": " << x << "\t"; }}
#define DBG(x)     {if(DEBUG){DBG0(x); cout << endl;}}
#define DBG2(x, y) {if(DEBUG){DBG0(x); DBG(y);}}
#define DBG3(x, y, z) {if(DEBUG){DBG0(x); DBG2(y, z);}}
#define DBG4(w, x, y, z) {if(DEBUG){DBG0(w); DBG3(x, y, z);}}

template <class T>
ostream& operator<<(ostream& os, vector<T> xs){ for(T x: xs) os << x << ' '; return os; }
template <class S, class T>
ostream& operator<<(ostream& os, pair<S,T> st){ os << "(" << st.first << "," << st.second <<")"; return os; }

typedef vector<int> vint;
typedef vector<ll> vll;
typedef vector<ul> vul;
typedef vector<ull> vull;
typedef vector<bool> vbl;
typedef pair<int, int> pii;

int main(void){
    int T;
    cin >> T;
    repf(ccc, 1, T + 1){
        int n;
        cin >> n;
        vector<int> vs(n);
        rep(i, n) cin >> vs[i];
        sort(ALL(vs));
        int ans = INF;
        repf(mxx, 1, vs[n - 1] + 1){
            int mx = 0;
            int sp = 0;
            rep(i, n){
                mx = max(mx, min(vs[i], mxx));
                sp += max((vs[i] + mxx - 1) / mxx - 1, 0);
            }
            ans = min(mx + sp, ans);
            DBG3(mxx, mx, sp);
        }
        cout << "Case #" << ccc << ": " << ans << endl;
    }
    return 0;
}
