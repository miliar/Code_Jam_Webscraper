#include <iostream>
#include <algorithm> 
using namespace std;

#define eps 1e-6

char map[100][102];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
    string s;
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", map[i]);
        }

        int cnt = 0;
        bool failed = false;
        printf("Case #%d: ", test + 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == '.') {
                    continue;
                }
                int oriDir = -1;
                if (map[i][j] == '^') {
                    oriDir = 3;
                } else if (map[i][j] == 'v') {
                    oriDir = 1;
                } else if (map[i][j] == '<')
                    oriDir = 2;
                else if (map[i][j] == '>')
                    oriDir = 0;
                bool foundMatch = false;
                bool skip = false;
                for (int dir = 0; dir < 4; dir++) {
                    for (int k = 1; k < 100; k++) {
                        int ti = i + dy[dir] * k;
                        int tj = j + dx[dir] * k;
                        if (ti < 0 || ti >= n) break;
                        if (tj < 0 || tj >= m) break;
                        if (map[ti][tj] != '.') {
                            if (dir == oriDir) {
                                skip = true;
                            }
                            else
                                foundMatch = true;
                        }
                    }
                    if (skip)
                        break;
                }
                //printf("%d %d: %d %d %d\n", i, j, oriDir, skip, foundMatch);
                if (skip)
                    continue;
                if (!foundMatch)
                {
                    failed = true;
                    break;
                } else
                    cnt++;
            }
        }
        if (failed) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", cnt);
        }
    }
    return 0;
}