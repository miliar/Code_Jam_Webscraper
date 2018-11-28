#include <bits/stdc++.h>
using namespace std;

const int MAXN = 5;
int N;
bool _can[MAXN][MAXN], can[MAXN][MAXN];

bool workers[MAXN], machines[MAXN];
bool good() {
    for (int i=0; i<N; i++) {
        if (!workers[i]) {
            bool got = 0;
            for (int j=0; j<N; j++) {
                if (!machines[j] && can[i][j]) {
                    workers[i] = machines[j] = 1;
                    if (!good()) return false;
                    workers[i] = machines[j] = 0;
                    got = 1;
                }
            }
            if (!got) return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int kases; cin >> kases;
    for (int kase=1; kase<=kases; kase++) {
        cout << "Case #" << kase << ": ";
        cin >> N;
        for (int i=0; i<N; i++) {
            string s; cin >> s;
            for (int j=0; j<N; j++) {
                _can[i][j] = (s[j] == '1');
            }
        }
        int best = N*N;
        for (int i=0; i<(1 << N*N); i++) {
            int cost = 0;
            for (int j=0; j<N; j++) {
                for (int k=0; k<N; k++) {
                    if (_can[j][k] || (i&(1 << (j*N+k)))) can[j][k] = 1;
                    else can[j][k] = 0;
                    if (can[j][k] == 1 && _can[j][k] == 0) cost++;
                }
            }
            if (cost >= best) continue;
            memset(workers, 0, sizeof(workers));
            memset(machines, 0, sizeof(machines));
            if (good())
                best = min(best, cost);
        }
        cout << best << '\n';
    }
    return 0;
}
