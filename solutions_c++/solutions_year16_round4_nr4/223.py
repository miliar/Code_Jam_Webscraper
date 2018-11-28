#include <algorithm>
#include <cstdio>
using namespace std;

const int MAXN = 4;
const int MAXB = MAXN * MAXN;

int N, NB;
int br[MAXB], bc[MAXB];
int F[MAXN][MAXN], Ft[MAXN][MAXN];
bool useda[MAXN], usedb[MAXN];

bool check(int d)
{
    /*
    printf("%d\n", d);
    for (int i = 0; i < N; ++i)
        printf("|%d", (int)used[i]);
    printf("\n");
    */
    if (d >= N) return true;

    for (int i = 0; i < N; ++i) {
        if (useda[i]) continue;
        useda[i] = true;
        bool one = false;

        for (int j = 0; j < N; ++j)
            if (Ft[i][j] && !usedb[j]) {
                one = true;
                usedb[j] = true;
                bool cur = check(d + 1);
                // printf("??? %d\n", (int)cur);
                usedb[j] = false;
                if (!cur) {
                    useda[i] = false;
                    return false;
                }
            }
        useda[i] = false;
        if (!one) return false;
    }

    return true;
}

char tmp[MAXN + 1];

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d", &N);
        NB = 0;
        for (int r = 0; r < N; ++r) {
            scanf("%s", tmp);
            for (int c = 0; c < N; ++c) {
                F[r][c] = tmp[c] - '0';
                if (F[r][c] == 0) {
                    br[NB] = r; bc[NB] = c; ++NB;
                }
            }
        }

        printf("Case #%d: ", t + 1);
        for (int L = 0; L <= NB; ++L) {
            bool good = false;
            for (int i = 0; i < (1<<NB); ++i) {
                int ti = i, cnt = 0;
                while (ti > 0) { ti &= (ti - 1); ++cnt; }
                if (cnt != L) continue;

                for (int r = 0; r < N; ++r)
                    for (int c = 0; c < N; ++c)
                        Ft[r][c] = F[r][c];

                for (int j = 0; j < NB; ++j)
                    if (i & (1<<j))
                        Ft[br[j]][bc[j]] = 1;
                /*
                for (int r = 0; r < N; ++r) {
                    for (int c = 0; c < N; ++c)
                        printf("%d ", Ft[r][c]);
                    printf(" %d \n", cnt);
                }
                */
                if (check(0)) {
                    good = true;
                    break;
                }

            }

            if (good) {
                printf("%d\n", L);
                break;
            }
        }
    }

    return 0;
}
