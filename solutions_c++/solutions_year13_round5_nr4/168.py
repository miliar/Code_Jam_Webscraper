#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

char c[31];
LD dp[1 << 20];

int main(void) {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        fprintf(stderr, "%d\n", t);
        scanf("%s", c); int n = strlen(c);
        int cur = 0;
        REP (i, n) {
            if (c[i] == '.') {
                cur += (1 << i);
            }
        }
        for (int mask = 1; mask <= cur; ++mask) {
            dp[mask] = 0.0;
            int first = -1;
            REP (i, n) {
                if (mask & (1 << i)) {
                    first = i;
                    break;
                }
            }
            int last = first + n;
            for (int i = n - 1; i >= 0; --i) {
                if (mask & (1 << i)) {
                    last = i;
                }
                dp[mask] += dp[mask - (1 << (last % n))] + (n - (last - i));
            }
            dp[mask] /= n;
        }
        printf("Case #%d: %.15Lf\n", t, dp[cur]);
    }
    return 0;
}

            




            
