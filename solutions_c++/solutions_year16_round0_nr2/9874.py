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
        int i = s.size() - 1;
        for (; i >= 0; i--) {
            if (s[i] == '-') break;
        }
        s = s.substr(0, i + 1);
    }

    void solve() {
        if (s.size() == 0) {
            cout << 0 << endl;
            return;
        }
        int count = 0;
        char c = s[0];
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == c) continue;
            c = s[i];
            count++;
        }
        cout << count + 1 << endl;
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

