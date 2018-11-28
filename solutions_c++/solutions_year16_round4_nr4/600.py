#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <utility>

typedef long long ll;

using namespace std;

template<typename T>
T next() { T tmp; cin >> tmp; return tmp; }

int cost(const vector< string >& a, int msk, int n) {
    int ans = 0;
    for (int  i = 0; i < n * n; ++i) {
        int x = i / n;
        int y = i % n;
        if ((msk >> i) % 2 == 1 && a[x][y] == '0') {
            ans += 1;
        }
    }
    return ans;
}
bool dfs(int j, const vector< string >& a, int forb, vector< bool > & was, vector< int > & matched) {
    if (was[j]) {
        return false;
    }
    was[j] = true;
    for (int i = 0; i < a.size(); ++i) {
        if (i != forb && a[i][j] == '1') {
            if (matched[i] == -1 || dfs(matched[i], a, forb, was, matched)) {
                matched[i] = j;
                return true;
            }
        }
    }
    return false;
}

bool blocked(vector< string > a, int msk, int n) {
    for (int  i = 0; i < n * n; ++i) {
        int x = i / n;
        int y = i % n;
        if ((msk >> i) % 2 == 1) {
            a[i / n][i % n] = '1';
        }
    }
    vector< int > matched(n, -1);
    vector< bool > was(n, false);
    for (int i = 0; i < n; ++i) {
        fill(matched.begin(), matched.end(),  -1);
        int ok = 1;
        for (int j = 0; j < n; ++j) {
            if (a[i][j] == '1') {
                fill(was.begin(), was.end(), false);
                if (!dfs(j, a, i, was, matched)) {
                    ok = 0;
                }
            }
        }
        if (ok == 1) {
            return true;
        }
    }
    return false;
}

void solve() {
    int n = next< int >();
    vector< string > a(n);
    generate(a.begin(), a.end(), next< string >);
    int best = n * n;
    for (int msk = 0; msk < (1 << (n * n)); ++msk) { // 
        int cst = cost(a, msk, n);
        if (!blocked(a, msk, n)) {
            best = min(cst, best);
        }
    }
    cout << best << endl;

}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
