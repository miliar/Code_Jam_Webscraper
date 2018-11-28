#include <bits/stdc++.h>
using namespace std;

using pii = pair<int,int>;
using ll = long long;
#define rep(i, j) for(int i=0; i < (int)(j); i++)
#define repeat(i, j, k) for(int i = (j); i < (int)(k); i++)
#define all(v) v.begin(),v.end()
#define debug(x) cerr << #x << " : " << x << endl

template<class T> bool set_min(T &a, const T &b) { return a > b  ? a = b, true : false; }
template<class T> bool set_max(T &a, const T &b) { return a < b  ? a = b, true : false; }
// vector
template<class T> istream& operator >> (istream &is , vector<T> &v) { for(T &a : v) is >> a; return is; }
template<class T> ostream& operator << (ostream &os , const vector<T> &v) { for(const T &t : v) os << "\t" << t; return os << endl; }
// pair
template<class T, class U> ostream& operator << (ostream &os , const pair<T, U> &v) { return os << "<" << v.first << ", " << v.second << ">"; }

const int INF = 1 << 30;
const ll INFL = 1LL << 60;


class Solver {
  public:
    bool solve(int C) {
        string S; cin >> S;
        int K; cin >> K;

        auto f = [](string S, int K) {
            int cnt = 0;
            rep(i, S.size() - K + 1) {
                if(S[i] == '-') {
                    rep(k, K) {
                        assert(i + k < S.size());
                        S[i + k] = S[i + k] == '+' ? '-' : '+';
                    }
                    cnt++;
                }
            }
            bool fail = false;
            rep(i, K) fail |= S[S.size() - i - 1] == '-';
            return fail ? INF : cnt;
        };        
        int ans = INF;
        set_min(ans, f(S, K));
        reverse(all(S));
        set_min(ans, f(S, K));
        cout << "Case #" << C << ": ";
        if(ans == INF) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << endl;
        return 0;
    }
};

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    int T; cin >> T;
    rep(i, T) {
        Solver s;   
        s.solve(i + 1);
    }
    return 0;
}
