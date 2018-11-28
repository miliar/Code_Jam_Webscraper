#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;


typedef long long LL;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}
const int N = 55;
int chess[N][N], vis[N][N], state[N * N];
pair<int, int> que[N * N];
int move[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
int main()
{
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("C-small-attempt2.out", "w", stdout);
    int t, cas = 1, R, C, M, tx, ty;
    int i, j, k;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d", &R, &C, &M);
        for(i = 0; i < R * C - M; i++)
            state[i] = 0;
        for(; i < R * C; i++)
            state[i] = 1;
        int hasSolution = 0;
        do
        {
            for(i = 0; i < R * C; i++)
            {
                if(state[i] == 0)   chess[i / C + 1][i % C + 1] = 0;
                else                chess[i / C + 1][i % C + 1] = -1;
            }
            int sx = -1, sy = -1;
            for(i = 1; i <= R; i++)
                for(j = 1; j <= C; j++)
                {
                    if(chess[i][j] != -1)
                    {
                        tx = i, ty = j;
                        for(k = 0; k < 8; k++)
                        {
                            int nx = i + move[k][0];
                            int ny = j + move[k][1];
                            if(nx >= 1 && nx <= R && ny >= 1 && ny <= C)
                                chess[i][j] += (chess[nx][ny] == -1);
                        }
                        if(chess[i][j] == 0)
                        {
                            sx = i;
                            sy = j;
                        }
                    }
                }
            if(sx == -1 && R * C - M == 1)
            {
                hasSolution = 1;
                break;
            }
            tx = sx, ty = sy;
            int head = 0, tail = 0, cnt = 0;
            memset(vis, 0, sizeof(vis));
            que[tail++] = make_pair(sx, sy);
            vis[sx][sy] = 1;
            cnt++;
            while(head < tail)
            {
                int cx = que[head].first, cy = que[head].second;
                head++;
                if(chess[cx][cy] == 0)
                {
                    for(k = 0; k < 8; k++)
                    {
                        int nx = cx + move[k][0];
                        int ny = cy + move[k][1];
                        if(nx >= 1 && nx <= R && ny >= 1 && ny <= C && !vis[nx][ny] && chess[nx][ny] >= 0)
                        {
                            que[tail++] = make_pair(nx, ny);
                            vis[nx][ny] = 1;
                            cnt++;
                        }
                    }
                }
            }
            //printf("cnt: %d\n", cnt);
            if(cnt + M == R * C)
            {
                hasSolution = 1;
                break;
            }

        }
        while(next_permutation(state, state + R * C));
        printf("Case #%d:\n", cas++);
        if(hasSolution)
        {
            for(i = 1; i <= R; i++)
            {
                for(j = 1; j <= C; j++)
                {
                    if(chess[i][j] == -1)
                        printf("*");
                    else if(i == tx && j == ty)
                        printf("c");
                    else
                        printf(".");
                }
                printf("\n");
            }
        }
        else
            printf("Impossible\n");
    }
    return 0;
}
