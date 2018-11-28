#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> dp;

string _itos(int x) {
    stringstream stream;
    stream << x;
    string res;
    stream >> res;
    return res;
}

int _stoi(const string& s) {
    stringstream stream;
    stream << s;
    int res;
    stream >> res;
    return res;
}

int f(int x) {
    string s = _itos(x);
    reverse(s.begin(), s.end());
    return _stoi(s);
}

void prec() {
    dp[1] = 1;

    set<pair<int, int>> q;
    q.insert({1, 1});
    while (!q.empty()) {
        auto p = *q.begin();
        q.erase(q.begin());
        int t = p.second;

        if (t > (int) 1e6 * 3)
            continue;

        int to[2] = {t + 1};
        to[1] = f(t);
        for (int i = 0; i < 2; i++) {
            if (dp.count(to[i]) == 0)
                dp[to[i]] = (int) 1e9;
            if (dp[to[i]] > dp[t] + 1) {
                q.erase({dp[to[i]], to[i]});
                dp[to[i]] = dp[t] + 1;
                q.insert({dp[to[i]], to[i]});
            }
        }
    }
}

void solve() {
    int n;
    scanf("%d", &n);

    printf("%d\n", dp[n]);
}

int main() {
    ifstream in("data.txt");

    for (int i = 1; i < (int) 1e6 * 2; i++) {
        int trash;
        in >> trash >> dp[i];
    }
    
    int t = 0;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
