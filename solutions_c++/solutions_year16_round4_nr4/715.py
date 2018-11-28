#include <bits/stdc++.h>

using namespace std;

const int MAXN = 10;

int N;

bool a[MAXN][MAXN];

bool b[MAXN][MAXN];

bool check() {
    int turn[MAXN];
    for (int i = 0; i < N; ++i)
        turn[i] = i;
    bool res = true;
    do {
        int choose[MAXN];
        for (int i = 0; i < N; ++i)
            choose[i] = i;
        bool ok = true;
        do {
            bool mark[MAXN];
            for (int i = 0; i < N; ++i) mark[i] = 0;
            for (int i = 0; i < N; ++i)
                if (!a[turn[i]][choose[i]] && !b[turn[i]][choose[i]]) {
                    int cnt = 0;
                    for (int j = 0; j < N; ++j)
                        if (!mark[j] && (a[turn[i]][j] || b[turn[i]][j]))
                            ++cnt;
                    if (cnt > 0) continue;
                    ok = false;
                    break;
                }
                else
                    mark[choose[i]] = 1;
            if (!ok) {
                res = false;
                break;
            }

        } while (next_permutation(choose, choose + N));
        if (!res) {
            break;
        }
    } while (next_permutation(turn, turn + N));
    return res;
}

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int i = 0; i < N; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < N; ++j)
                a[i][j] = s[j] - '0';
        }
        int res = N * N + 1;
        for (int mask = 0; mask < (1 << (N * N)); ++mask) {
            int cost = 0;
            for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) {
                int pos = i * N + j;
                if (mask & (1 << pos))
                    b[i][j] = 1, ++cost;
                else
                    b[i][j] = 0;
            }

            if (cost < res && check()) res = cost;
        }
        cout << "Case #" << t << ": " << res << endl;
    }
}
