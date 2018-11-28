#include <bits/stdc++.h>
#define sz(x) ((int)((x).size()))
typedef long long ll;

int X, Y;
char g[104][104];
bool seen[104][104];
int yc[104], xc[104];
int dy[] = {-1,0,1,0}, dx[] = {0,1,0,-1};
int ans = 0;

void f(int y, int x) {
    if (seen[y][x]) return;
    else seen[y][x] = true;
    if (g[y][x] == '.') return;
    int d;
    if (g[y][x] == '^') d = 0;
    if (g[y][x] == '>') d = 1;
    if (g[y][x] == 'v') d = 2;
    if (g[y][x] == '<') d = 3;
    x += dx[d]; y += dy[d];
    while (0 <= y && y < Y && 0 <= x && x < X) { if (g[y][x] != '.') { f(y, x); return; } x += dx[d]; y += dy[d]; }
    ans++;
}

int main()
{
    int TC; scanf("%d", &TC);
    for (int tc = 1; tc <= TC; tc++) {
        scanf("%d%d", &Y, &X);
        for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) scanf(" %c", &g[y][x]);
        //for (int y = 0; y < Y; y++) printf("%s\n", g[y]);
        for (int y = 0; y < Y; y++) yc[y] = 0;
        for (int x = 0; x < X; x++) xc[x] = 0;
        for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) { if (g[y][x] != '.') { yc[y]++; xc[x]++; } }
        ans = 0;
        for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) if (g[y][x] != '.' && yc[y] == 1 && xc[x] == 1) ans = 1<<20;
        for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) seen[y][x] = false;
        for (int y = 0; y < Y; y++) for (int x = 0; x < X; x++) if (!seen[y][x]) f(y, x);

        if (ans < (1<<20)) printf("Case #%d: %d\n", tc, ans);
        else printf("Case #%d: IMPOSSIBLE\n", tc);
    }
}

