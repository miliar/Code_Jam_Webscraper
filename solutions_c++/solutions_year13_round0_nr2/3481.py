#include <cstdio>
using namespace std;

int H, W;
int field[110][110];

void cut(bool dir, int h)
{
    int n = dir ? H : W;
    int m = dir ? W : H;
    for (int i = 0; i < n; ++i) {
        bool ok = true;
        for (int j = 0; j < m; ++j) {
            int v = dir ? field[i][j] : field[j][i];
            if (v != -1 && v != h) {
                ok = false;
                break;
            }
        }
        if (ok) {
            for (int j = 0; j < m; ++j) {
                if (dir)
                    field[i][j] = -1;
                else
                    field[j][i] = -1;
            }
        }
    }
}

int main()
{
    int T; scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase) {
        scanf("%d%d", &H, &W);
        for (int y = 0; y < H; ++y) {
            for (int x = 0; x < W; ++x) {
                scanf("%d", &field[y][x]);
            }
        }

        for (int h = 1; h <= 100; ++h) {
            cut(false, h);
            cut(true, h);
        }

        bool ok = true;
        for (int y = 0; y < H; ++y) {
            for (int x = 0; x < W; ++x) {
                if (field[y][x] != -1)
                    ok = false;
            }
        }

        printf("Case #%d: ", testcase);
        if (ok) puts("YES");
        else puts("NO");
    }
}
