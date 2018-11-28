#include <algorithm>
#include <cstdio>
#include <string>
using namespace std;

const int MAXN = 14;

string best[MAXN+1][3];

int main()
{
    best[0][0] = "P";
    best[0][1] = "R";
    best[0][2] = "S";

    for (int i = 1; i <= MAXN; ++i) {
        best[i][0] = best[i - 1][0] + best[i - 1][1];
        best[i][1] = best[i - 1][0] + best[i - 1][2];
        best[i][2] = best[i - 1][1] + best[i - 1][2];
    }

    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        int N, P, R, S;
        scanf("%d%d%d%d", &N, &R, &P, &S);

        int bestv = -1;
        for (int v = 0; v < 3; ++v) {
            int nP = 0, nR = 0, nS = 0;
            for (int i = 0; i < (1<<N); ++i) {
                if (best[N][v][i] == 'P') ++nP;
                if (best[N][v][i] == 'R') ++nR;
                if (best[N][v][i] == 'S') ++nS;
            }

            if (nP == P && nR == R && nS == S) {
                bestv = v;
                break;
            }
        }

        printf("Case #%d: ", t + 1);
        if (bestv == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%s\n", best[N][bestv].c_str());
    }

    return 0;
}
