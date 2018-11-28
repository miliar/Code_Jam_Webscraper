#include <cstdio>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        bool ans[4][4][4] = {
            {
                {1, 1, 1, 1},
                {1, 1, 1, 1},
                {1, 1, 1, 1},
                {1, 1, 1, 1}
            }, // x = 1
            {
                {0, 1, 0, 1},
                {1, 1, 1, 1},
                {0, 1, 0, 1},
                {1, 1, 1, 1}
            }, // x = 2
            {
                {0, 0, 0, 0},
                {0, 0, 1, 0},
                {0, 1, 1, 1},
                {0, 0, 1, 0}
            }, // x = 3
            {
                {0, 0, 0, 0},
                {0, 0, 0, 0},
                {0, 0, 0, 1},
                {0, 0, 1, 1}
            }, // x = 4
        };
        printf("Case #%d: %s\n", t, ans[x-1][r-1][c-1] ? "GABRIEL" : "RICHARD");
    }
    return 0;
}
