#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<string> A;
vector<string> B;

int order[4];
bool opened[4];

bool check(int depth) {
    if (depth == N) {
        for (int i = 0; i < N; i++)
            if (!opened[i]) return false;
        return true;
    }

    bool working = false;
    for (int i = 0; i < N; i++) {
        if (B[order[depth]][i] == '0') continue;
        if (opened[i]) continue;
        working = true;
        opened[i] = true;
        if (!check(depth + 1)) return false;
        opened[i] = false;
    }
    return working;
}

bool check_all() {
    for (int i = 0; i < N; i++) order[i] = i;
    do {
        memset(opened, false, sizeof(opened));
        if (!check(0)) return false;
    } while (next_permutation(order, order + N));
    return true;
}

void solve() {
    cin >> N;
    A.clear();
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        A.push_back(s);
        B.push_back(s);
    }

//memset(opened, false, sizeof(opened));
//cout << check(0)

    int ans = N * N;
    for (int i = 0; i < (1 << (N*N)); i++) {
        int cost = 0;
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                if (i & (1 << (j * N + k))) {
                    B[j][k] = '1';
                    cost++;
                } else {
                    B[j][k] = A[j][k];
                }
            }
        }
        if (check_all()) {
            ans = min(ans, cost);
        }
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
