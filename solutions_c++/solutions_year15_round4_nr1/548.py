#include <algorithm>
#include <string>
#include <cstdio>
#include <set>
using namespace std;

const int MAXR = 100;
const int dr[] = { 0, 1, 0, -1 };
const int dc[] = { 1, 0, -1, 0 };

int R, C;
char F[MAXR][MAXR + 1];

int getd(char c)
{
    switch (c) {
        case '>': return 0;
        case 'v': return 1;
        case '<': return 2;
        case '^': return 3;
   }
}

bool check(int r0, int c0, int d)
{
    int tr = r0 + dr[d], tc = c0 + dc[d];

    while (tr >= 0 && tr < R && tc >= 0 && tc < C) {
        if (F[tr][tc] != '.') return true;
        tr += dr[d]; tc += dc[d];
    }

    return false;
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d%d", &R, &C);
        for (int r = 0; r < R; ++r)
            scanf("%s", &F[r][0]);

        int answer = 0;
        bool impossible = false;

        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c)
                if (F[r][c] != '.') {
                    int d = getd(F[r][c]);

                    if (check(r, c, d)) continue;
                    bool bad = true;

                    for (int d = 0; d < 4; ++d) {
                        if (check(r, c, d)) { bad = false; break; }
                    }

                    if (bad) { impossible = true; }
                    ++answer;
                }

        printf("Case #%d: ", t + 1);
        if (impossible)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", answer);
    }

    return 0;
}
