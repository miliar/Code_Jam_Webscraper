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

    int N;
    vector<string> F;
    void input() {
        cin >> N;
        F.clear(); F.resize(N); cin >> F;
    }
    const int INF = 1<<20;

    bool check(int bit, const vector<int>& ord, int index, int used) {
        if (index == N) return true;
        bool flag = false;
        for (int i = 0; i < N; i++) {
            if (used & (1 << i)) continue;
            int y = ord[index], x = i;
            int b = y * N + x;
            if (bit & (1 << b)) {
                flag = true;
                int nused = (used | (1 << i));
                if (not check(bit, ord, index + 1, nused)) return false;
            }
        }
        return flag;
    }

    int cost(int bit) ;
    bool check(int bit) {
        // make all orders;
        vector<int> ord;
        for (int i = 0; i < N; i++) ord.push_back(i);
        do {
            //cout << ord << " " << bit  << "  " << cost(bit) << "  " << check(bit, ord, 0, 0) << endl;
            if (not check(bit, ord, 0, 0)) return false;
        } while (next_permutation(ord.begin(), ord.end()));
        return true;
    }

    int cost(int bit) {
        int ret = 0;
        for (int i = 0; i < (N*N); i++) {
            int y = i / N; 
            int x = i % N;
            if (bit & (1 << i)) {
                if (F[y][x] == '0') ret++;
            } else {
                if (F[y][x] == '1') return INF;
            }
        }
        return ret;
    }

    void solve() {
        int ans = INF;
        for (int bit = 0; bit < (1<<(N*N)); bit++) {
            int c = cost(bit);
            if (c >= INF) continue;
            if (check(bit)) {
                ans = min(ans, c);
            }
        }
        cout << ans << endl;
    }
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cerr << t << endl;
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

