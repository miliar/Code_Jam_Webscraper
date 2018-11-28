


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
        string s;
        cin >> s;
        reverse(s.begin(), s.end());
        bool f = false;
        for (int i = 0; i < s.size(); i++) {
            if ((s[i] == '-') ^ f) {
                f = !f;
                ans++;
            }
        }
        cout << "Case #" << caseNum++ << ": ";
        cout << ans << endl;
    }
    return 0;
}
