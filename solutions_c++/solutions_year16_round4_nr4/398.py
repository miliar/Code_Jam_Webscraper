#include <cstdio>

int N, R;

char data[5][5];

bool worker[5];
bool machine[5];

bool dfs2(int x) {
    if (x == N) {
        return false;
    }

    for (int i = 0; i < N; i ++) {
        if (worker[i]) {
            continue;
        }

        bool c = false;
        for (int j = 0; j < N; j ++) {
            if (machine[j]) {
                continue;
            }

            if (data[i][j] == '1') {
                c = true;
                worker[i] = true;
                machine[j] = true;
                if (dfs2(x + 1)) {
                    return true;
                }
                worker[i] = false;
                machine[j] = false;
            }
        }
        if (c == false) {
            return true;
        }
    }

    return false;
}

void dfs(int depth, int x, int y) {
    if (y == N) {
        dfs(depth, x + 1, 0);
        return;
    }
    if (R <= depth) {
        return;
    }
    if (x == N) {
        for (int i = 0; i < N; i ++) {
            worker[i] = false;
            machine[i] = false;
        }
        if (dfs2(0) == false) {
            R = depth;
        }
        return;
    }

    dfs(depth, x, y + 1);
    if (data[x][y] == '0') {
        data[x][y] = '1';
        dfs(depth + 1, x, y + 1);
        data[x][y] = '0';
    }
}
int main() {
    int T;
    scanf( "%d", &T );
    for (int test = 1; test <= T; test ++) {
        scanf( "%d", &N );

        R = 16;
        for (int i = 0; i < N; i ++) {
            scanf( "%s", data[i] );

        }
        dfs(0, 0, 0);

        printf( "Case #%d: %d\n", test, R );
    }
    return 0;
}

