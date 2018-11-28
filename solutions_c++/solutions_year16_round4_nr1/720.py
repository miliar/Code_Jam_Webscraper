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

    int N, R, P, S;;
    void input() {
        cin >> N >> R >> P >> S;
    }
    
    const string s = "RPS";

    int win(int h) { // hにかつやつ
        return (h + 1) % 3;
    }

    int lose(int h) { // hにまけるやつ
        return (h + 2) % 3;
    }

    void step(string& ans, int index, int depth, int w) {
        if (depth == N) {
            ans[index] = s[w];
            return;
        }
        int l = lose(w);
        step(ans, index * 2, depth + 1, l);
        step(ans, index * 2 + 1, depth + 1, w);
    }

    bool check(string& ans) {
        map<char, int> M;
        for (int i = 0; i < ans.size(); i++) {
            M[ ans[i] ]++;
        }
        return (M['R'] == R && M['P'] == P && M['S'] == S);
    }

    void tr(string& ans) {
        //cerr << "before: " << ans << endl;
        for (int t = 0; t < N; t++) {
            vector<string> bs(1 << (N - t));
            for (int j = 0; j < (1 << (N - t)); j++) {
                int size = 1 << t;
                bs[j] = ans.substr(j * size, size);
            }
            for (int i = 0; i < bs.size(); i+=2) {
                if (bs[i] > bs[i + 1]) {
                    swap(bs[i], bs[i + 1]);
                }
            }
            ans.clear();
            for (int i = 0; i < bs.size(); i++) {
                ans += bs[i];
            }
            //cerr << "after:" << t << "-> " << ans << endl;
        }
        //cerr << "after:  " << ans << endl;
    }

    void solve() {
        string ans; ans.push_back('Z');
        for (int x = 0; x < 3; x++) {
            string c(1<<N, '.');
            step(c, 0, 0, x);
            if (check(c)) {
                tr(c);
                ans = min(ans, c);
            }
        }
        if (ans[0] == 'Z') {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 0; i < ans.size(); i++) {
                cout << ans[i];
            }
            cout << endl;
        }
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

