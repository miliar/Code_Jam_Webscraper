
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#define MAXM 1000
#define MOD 1000002013

using namespace std;

long long N, M;

set <int> pos;
map <int, long long> numEnter, numExit;

// (start pos, num passengers left)
pair <int, long long> q[2 * MAXM];

long long solve() {
    pos.clear();
    numEnter.clear();
    numExit.clear();
    long long total = 0;

    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int u, v;
        long long cnt;
        cin >> u >> v >> cnt;

        numEnter[u] += cnt;
        numExit[v] += cnt;
        pos.insert(u);
        pos.insert(v);

        long long dist = v - u;
        long long used = ((N + N - dist) * (dist + 1) / 2) % MOD;
        total = (total + (used * cnt)) % MOD;
    }
    // cerr << total << endl;

    int j = 0;
    for (set <int>::iterator it = pos.begin(); it != pos.end(); it++) {
        int cur = *it;
        q[j] = make_pair(cur, numEnter[cur]);
        j++;

        long long left = numExit[cur];
        for (int i = j - 1; i >= 0; i--) {
            long long match = q[i].second;
            long long dist = cur - q[i].first;
            long long used = ((N + N - dist) * (dist + 1) / 2) % MOD;
            if (match <= left) {
                total = (total - (used * match) % MOD + MOD) % MOD;
                q[i].second = 0;
                left -= match;
            }
            else {
                total = (total - (used * left) % MOD + MOD) % MOD;
                q[i].second -= left;
                left = 0;
                break;
            }
        }
    }
    return total;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }
}

