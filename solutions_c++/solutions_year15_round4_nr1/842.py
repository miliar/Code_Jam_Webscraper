
#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;
template<class T> inline bool amax (T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool amin (T &a, const T &b) { if (a > b) { a = b; return 1; } return 0; }
template<class T> ostream& operator << (ostream &os, const vector<T> &v) { os << "["; for (typename vector<T>::const_iterator it = v.begin(); it != v.end(); it++) { os << (it != v.begin() ? ", " : "") << *it; } os << "]"; return os; }
template<class T> ostream& operator << (ostream &os, const set<T> &s) { os << "["; for (typename set<T>::const_iterator it = s.begin(); it != s.end(); it++) { os << (it != s.begin() ? ", " : "") << *it; } os << "]"; return os; }
template<class Key, class Val> ostream& operator << (ostream &os, const map<Key, Val> &m) { os << "{"; for (typename map<Key, Val>::const_iterator it = m.begin(); it != m.end(); it++) { os << (it != m.begin() ? ", " : "") << it->first << ":" << it->second; } os << "}"; return os; }
template<class T, class S> ostream& operator << (ostream &os, const pair<T, S> &p) { os << "(" << p.first << ", " << p.second << ")"; return os; }
template <class T> istream& operator >> (istream &is, vector<T> &v) { for (size_t i = 0; i < v.size(); i++) is >> v[i]; return is; }
template <class Target, class Source> inline Target lexical_cast (const Source &s) { Target t; stringstream ss; ss << s; ss >> t; return t; }

//> v < ^ (clock wise)
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
const int INFI = 1<<28;
const long long int INFL = 1LL<<60;
const double INFD = 1e+300;
const float INFF = 1e+100;
const double EPS = 1e-8;
const long long int MOD = 1000000007;
string dirs = ">v<^";

int solve ();
int main () {
    cout.setf(ios::fixed); cout.precision(10);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}

int solve () {
    int T;
    cin >> T;
    int caseNum = 1;
    while (T--) {
        int ans = 0;
        int R, C;
        cin >> R >> C;
        vector<string> F(R);
        vector<vector<int>> num(R, vector<int>(C));
        int V = 0;
        for (int i = 0; i < R; i++) {
            cin >> F[i];
        }
        bool possible = true;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (F[i][j] != '.') {
                    int d = dirs.find(F[i][j]);
                    int y = i, x = j;
                    while (1) {
                        y += dy[d];
                        x += dx[d];
                        if (y < 0 || y >= R || x < 0 || x >= C) {
                            ans++;
                            break;
                        }
                        if (F[y][x] != '.') {
                            break;
                        }
                    }
                    bool ok = false;
                    for (int k = 0; k < 4; k++) {
                        y = i;
                        x = j;
                        while (1) {
                            y += dy[k];
                            x += dx[k];
                            if (y < 0 || y >= R || x < 0 || x >= C) {
                                break;
                            }
                            if (F[y][x] != '.') {
                                ok = true;
                                break;
                            }
                        }
                    }
                    if (!ok) possible = false;
                }
            }
        }
        if (!possible) {
            cout << "Case #" << caseNum++ << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << caseNum++ << ": " << ans << endl;
        }
    }
    return 0;
}
