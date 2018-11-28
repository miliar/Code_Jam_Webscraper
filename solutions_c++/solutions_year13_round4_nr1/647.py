#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <map>
#include <set>

using namespace std;

const int MOD = 1000002013, MAXM = 1000;

int N, M;
pair<int, int> q[2*MAXM], pass[2*MAXM];
long long z0;

void solve()
{
    sort(&q[0], &q[2*M]);

    long long answer = 0;
    int NP = 0;

    for (int z = 0; z < 2*M; ++z) {
        if (q[z].second < 0) {
            pass[NP++] = make_pair(q[z].first, -q[z].second);
        } else {
            int r = q[z].second;

            while (r > 0) {
                int dist = q[z].first - pass[NP-1].first;
                int delta = min(pass[NP-1].second, r);

                dist = (dist *1LL* N - (dist *1LL* (dist-1)) / 2) % MOD;
                answer = (answer + dist *1LL* delta) % MOD;

                pass[NP-1].second -= delta; r -= delta;
                if (pass[NP-1].second == 0) --NP;
            }
        }
    }

    answer = ((z0 - answer)%MOD + MOD) % MOD;
    cout << answer;
}

int main()
{
    int T; scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        cin >> N >> M; z0 = 0;
        for (int i = 0; i < M; ++i) {
            int o, e, p;
            cin >> o >> e >> p;
            q[2*i] = make_pair(o, -p);
            q[2*i+1] = make_pair(e, p);

            int dist = e - o;
            dist = (dist *1LL* N - (dist *1LL* (dist-1)) / 2) % MOD;
            z0 = (z0 + dist *1LL* p) % MOD;
        }

        cout << "Case #" << t+1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
