#include <bits/stdc++.h>

using namespace std;

namespace {

    typedef double real;
    typedef long long ll;

    template<class T> ostream& operator<<(ostream& os, const vector<T>& vs) {
        if (vs.empty()) return os << "[]";
        os << "[" << vs[0];
        for (int i = 1; i < vs.size(); i++) os << " " << vs[i];
        return os << "]";
    }
    template<class T> istream& operator>>(istream& is, vector<T>& vs) {
        for (auto it = vs.begin(); it != vs.end(); it++) is >> *it;
        return is;
    }

    string s;
    void input() {
        cin >> s;
    }

    void solve() {
        string t;
        t.push_back(s[0]);
        for (int i = 1; i < s.size(); i++) {
            char f = t[0];
            char c = s[i];
            if (f <= c) {
                string u;
                u.push_back(c);
                t = u + t;
            } else {
                t.push_back(c);
            }
        }
        cout << t << endl;
    }
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

