#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

vector<vector<vector<int>>> dp; // depth, winner => (cntr, cntp, cnts);

int getl(int i) { return (i + 2) % 3; }

void precalc(int max_depth)
{
    dp.resize(max_depth, vector<vector<int>>(3, vector<int>(3, 0)));
    for (int i = 0; i < 3; ++i) dp[0][i][i] = 1;
    for (int depth = 1; depth < max_depth; ++depth) {
        for (int winner = 0; winner < 3; ++winner) {
            for (int i = 0; i < 3; ++i) {
                dp[depth][winner][i] = dp[depth - 1][winner][i] + dp[depth - 1][getl(winner)][i];
            }
        }
    }
}

string print(int depth, int winner)
{
    if (depth == 0) {
        switch (winner) {
            case 0:
                return "R";
            case 1:
                return "P";
            case 2:
                return "S";
        }
    }

    string a = print(depth - 1, winner);
    string b = print(depth - 1, getl(winner));
    if (a < b) return a + b;
    else return b + a;
}

void solve(int)
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    vector<string> possible;
    for (int i = 0; i < 3; ++i) {
        if (dp[n][i] == vector<int>{r, p, s}) {
            possible.push_back(print(n, i));
        }
    }

    if (possible.size() == 0) cout << "IMPOSSIBLE" << endl;
    else {
        string m = possible[0];
        for (auto& str: possible) m = min(m, str);
        cout << m << endl;
    }
}

int main() {
    precalc(20);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve(i);
    }
}
