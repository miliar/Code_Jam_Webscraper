#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int dp[1024];

vector<int> getVector(int k, int n) {
    vector<int> v(n);
    for (int i = n - 1; i >= 0; --i) {
        v[i] = (k & 1);
        k >>= 1;
    }
    return v;
}

int getNumber(const vector<int> &v) {
    int n = 0;
    for (int i = 0; i < v.size(); ++i) {
        n <<= 1;
        n |= v[i];
    }
    return n;
}

int reverseFirstI(int k, int n, int i) {
    int mask = (1 << i) - 1;
    k ^= mask;
    vector<int> v = getVector(k, n);
    reverse(v.end() - i, v.end());
    return getNumber(v);
}

void showState(int state, int n) {
    cout << state << ":";
    vector<int> v = getVector(state, n);
    for (int i = 0; i < n; ++i)
        cout << v[i];
}

void solve() {
    string s;
    cin >> s;

    memset(dp, -1, 1024 * sizeof(int));

    int n = s.size(), state = 0, newState, need = (1 << n) - 1;
    for (int i = n - 1; i >= 0; --i) {
        state <<= 1;
        state |= (s[i] == '+' ? 1 : 0);
    }

    queue<int> Q;
    dp[state] = 0;
    Q.push(state);
    while (dp[need] == -1) {
        state = Q.front();
        Q.pop();
        for (int i = 1; i <= n; ++i) {
            newState = reverseFirstI(state, n, i);
            if (dp[newState] == -1) {
                dp[newState] = dp[state] + 1;
                Q.push(newState);
            }
        }
    }
    cout << dp[need];
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, test;
    for (cin >> T, test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
