#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int NMAX = 5;
const int HMAX = 25;
const int LMAX = (1 << 16);
const int INF = 0x3f3f3f3f;
int tests, N;
bool canDo[NMAX][NMAX];
char A[HMAX];

bool valid[NMAX][LMAX], H[NMAX][NMAX], taken[NMAX];
int P[NMAX], PP[NMAX];

inline int bit(int x) {
    return (1 << x);
}

inline int maskHasBit(int mask, int x) {
    return mask & bit(x);
}

inline void decode(int mask, int N, bool H[NMAX][NMAX]) {
    for (int i = 1; i <= N; i++) {
        for (int j = 0; j < N; j++) {
            H[i][j + 1] = maskHasBit(mask, (i - 1) * N + j);
        }
    }
}

bool checkBad(int N, bool H[NMAX][NMAX], int ord[NMAX]) {
    for (int i = 1; i <= N; i++) {
        PP[i] = i;
    }

    do {
        // choice of machine to work on
        memset(taken, false, sizeof(taken));
        for (int i = 1; i <= N; i++) {
            // he can't operate it
            if (!H[ord[i]][PP[i]]) {
                bool hasAlternative = false;
                for (int j = 1; j <= N; j++) {
                    if (!taken[j] && H[ord[i]][j]) {
                        hasAlternative = true;
                        break ;
                    }
                }
                if (!hasAlternative) {
                    return true;
                }
                break ;
            }
            taken[PP[i]] = true;
        }
    } while (next_permutation(PP + 1, PP + N + 1));

    return false;
}

bool check(int N, bool H[NMAX][NMAX]) {
    for (int i = 1; i <= N; i++) {
        P[i] = i;
    }

    do {
        // this is the order of the works during the day
        if (checkBad(N, H, P)) {
            return false;
        }
    } while (next_permutation(P + 1, P + N + 1));

    return true;
}

void precompute() {
    for (int N = 1; N < NMAX; N++) {
        for (int mask = 0; mask < bit(N * N); mask++) {
            decode(mask, N, H);
            if (check(N, H)) {
                valid[N][mask] = true;
            }
        }
    }
}

bool included(bool A[NMAX][NMAX], bool B[NMAX][NMAX]) {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (A[i][j] && !B[i][j]) {
                return false;
            }
        }
    }

    return true;
}

void solve() {
    int minAdd = INF;
    for (int mask = 0; mask < bit(N * N); mask++) {
        if (valid[N][mask]) {
            decode(mask, N, H);
            if (included(canDo, H)) {
                int cand = 0;
                for (int i = 1; i <= N; i++) {
                    for (int j = 1; j <= N; j++) {
                        if (H[i][j] && !canDo[i][j]) {
                            cand++;
                        }
                    }
                }

                minAdd = min(minAdd, cand);
            }
        }
    }

    printf("%d\n", minAdd);
}

void read() {
    scanf("%d\n", &N);
    for (int i = 1; i <= N; i++) {
        scanf("%s", A + 1);
        for (int j = 1; j <= N; j++) {
            canDo[i][j] = A[j] == '1';
        }
    }
}

int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);

    precompute();

    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("Case #%d: ", test);

        read();
        solve();
    }
    return 0;
}
