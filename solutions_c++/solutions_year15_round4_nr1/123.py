#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 110

using namespace std;

int T, N, M, Ans;

char str[MaxN][MaxN];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

bool bounded(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < M;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T0 = 0, i, j, k;
    scanf("%d", &T);
    for( ; T; --T) {
        Ans = 0;
        scanf("%d%d", &N, &M);
        for(i = 0; i < N; ++i)
            scanf("%s", &str[i]);
        for(i = 0; i < N; ++i) {
            for(j = 0; j < M; ++j) {
                if(str[i][j] == '.') continue;
                int nx =i, ny = j, dir;
                if(str[i][j] == '^') dir = 2;
                if(str[i][j] == 'v') dir = 0;
                if(str[i][j] == '>') dir = 1;
                if(str[i][j] == '<') dir = 3;
                nx += dx[dir];
                ny += dy[dir];
                for( ; bounded(nx, ny) && str[nx][ny] == '.'; ) {
                    nx += dx[dir];
                    ny += dy[dir];
                }
                if(bounded(nx, ny))
                    continue;
                bool flag = 0;
                for(k = 0; k < 4; ++k) {
                    nx = i + dx[k];
                    ny = j + dy[k];
                    for( ; bounded(nx, ny) && str[nx][ny] == '.'; ) {
                        nx += dx[k];
                        ny += dy[k];
                    }
                    if(bounded(nx, ny))
                        flag = 1;
                }
                if(flag)
                    ++Ans;
                else
                    Ans = 10000000;
            }
        }
        if(Ans <= 1000000)
            printf("Case #%d: %d\n", ++T0, Ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", ++T0);
    }
    return 0;
}
