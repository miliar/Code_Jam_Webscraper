

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
const double EPS = 1e-10;
const long long int MOD = 1000000007;

int solve ();
int main () {
    cout.setf(ios::fixed); cout.precision(10);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}

struct S {
    double R, C;
    S () {}
    S (double r, double c) : R(r), C(c) { }
    bool operator < (const S &s) const {
        return C < s.C;
    }
};

int solve () {
    int T;
    cin >> T;
    int caseNum = 1;
    while (T--) {
        double ans = INFD;
        int N;
        cin >> N;
        double V, X;
        cin >> V >> X;
        vector<S> source(N);
        for (int i = 0; i < N; i++) {
            double R, C;
            cin >> R >> C;
            source[i] = S(R, C);
        }
        sort(source.begin(), source.end());
        /*
        for (int i = 0; i < source.size(); i++) {
        cout << source[i].R << " " << source[i].C << " " << source[i].energy << endl;
        }
        */
        if (N == 1) {
            if (abs(source[0].C - X) < EPS) {
                ans = V / source[0].R;
            } 
        } else {
            if (source[0].C < X && X < source[1].C) {
                double v1 = (X*V-V*source[1].C) / (source[0].C - source[1].C);
                double v2 = V - v1;
                ans = max(v1/source[0].R, v2/source[1].R);
            }
            if (abs(source[0].C - X) < EPS) {
                ans = min(ans, V/source[0].R);
            }
            if (abs(source[1].C - X) < EPS) {
                ans = min(ans, V/source[1].R);
            }
            if (abs(source[0].C - X) < EPS && abs(source[1].C - X) < EPS) {
                ans = min(ans, V/(source[0].R + source[1].R));
            }
        }
        if (ans == INFD) cout << "Case #" << caseNum++ << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << caseNum++ << ": " << ans << endl;
    }
    return 0;
}
