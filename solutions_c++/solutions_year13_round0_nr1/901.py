#include <cstdio>
using namespace std;

bool print(int t, int cnt[128]) {
    if (cnt['X'] == 4 || (cnt['X'] == 3 && cnt['T'] == 1)) {
        printf("Case #%d: X won\n", t);
        return 1;
    }
    if (cnt['O'] == 4 || (cnt['O'] == 3 && cnt['T'] == 1)) {
        printf("Case #%d: O won\n", t);
        return 1;
    }
    return 0;
}

int main() {
    int T, cnt[128];
    char grid[5][5];
    bool ended, empty;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        gets(grid[0]);
        for (int i = 0; i < 4; i++)
            gets(grid[i]);

        ended = empty = 0;
        for (int i = 0; !ended && i < 4; i++) {
            cnt['X'] = cnt['O'] = cnt['T'] = 0;
            for (int j = 0; j < 4; j++) {
                cnt[grid[i][j]]++;
                if (grid[i][j] == '.')
                    empty = 1;
            }
            if (print(t, cnt))
                ended = 1;
        }
        for (int j = 0; !ended && j < 4; j++) {
            cnt['X'] = cnt['O'] = cnt['T'] = 0;
            for (int i = 0; i < 4; i++) {
                cnt[grid[i][j]]++;
                if (grid[i][j] == '.')
                    empty = 1;
            }
            if (print(t, cnt))
                ended = 1;
        }
        if (!ended) {
            cnt['X'] = cnt['O'] = cnt['T'] = 0;
            for (int i = 0; i < 4; i++)
                cnt[grid[i][i]]++;
            if (print(t, cnt))
                ended = 1;
        }
        if (!ended) {
            cnt['X'] = cnt['O'] = cnt['T'] = 0;
            for (int i = 0; i < 4; i++)
                cnt[grid[i][3-i]]++;
            if (print(t, cnt))
                ended = 1;
        }
        if (!ended) {
            if (!empty)
                printf("Case #%d: Draw\n", t);
            else
                printf("Case #%d: Game has not completed\n", t);
        }
    }
}
