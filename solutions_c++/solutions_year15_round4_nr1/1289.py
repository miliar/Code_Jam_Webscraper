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
    int TT;
    cin >> TT;
//#pragma omp parallel for
    repf(tt, 1, TT + 1){
        int r, c;
        cin >> r >> c;
        vector<string> vs(r);
        rep(i, r) cin >> vs[i];

        int ans = 0;
        bool ok = true;
        rep(i0, r) rep(j0, c) if(vs[i0][j0] != '.') {
            // <^v>
            vector<bool> flgs(4, false);
            bool flg = false;
            rep(j, j0) {
                flg |= (vs[i0][j] != '.');
                if(flg) break;
            }
            flgs[0] = flg;

            flg = false;
            rep(i, i0) {
                flg |= (vs[i][j0] != '.');
                if(flg) break;
            }
            flgs[1] = flg;

            flg = false;
            repf(i, i0 + 1, r) {
                flg |= (vs[i][j0] != '.');
                if(flg) break;
            }
            flgs[2] = flg;

            flg = false;
            repf(j, j0 + 1, c) {
                flg |= (vs[i0][j] != '.');
                if(flg) break;
            }
            flgs[3] = flg;
            char cur = vs[i0][j0];
            ok &= any_of(ALL(flgs), [](bool b){ return b; });

            if ((cur == '<' && flgs[0]) ||
                (cur == '^' && flgs[1]) ||
                (cur == 'v' && flgs[2]) ||
                (cur == '>' && flgs[3]));
            else ans++;
        }

        if (ok) 
            cout << "Case #" << tt << ": " << ans << endl;
        else
            cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
