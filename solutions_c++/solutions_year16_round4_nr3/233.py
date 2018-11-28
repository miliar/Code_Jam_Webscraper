#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

const int N = 16;
const int V = N * N * 4;

const int UP = 0;
const int DOWN = 1;
const int LEFT = 2;
const int RIGHT = 3;
const int DX[] = {-1, 1, 0, 0};
const int DY[] = {0, 0, -1, 1};

int n, m, vcnt;
int lover[V];
char board[N][N];
vector<int> go[V];
bool used[V];

int enc(int x, int y, int d)
{
    return x * m * 4 + y * 4 + d;
}

int conv(int x)
{
    if (x < m)
        return enc(0, x, UP);
    if (x < m + n)
        return enc(x - m, m - 1, RIGHT);
    if (x < m + n + m)
        return enc(n - 1, m - 1 - (x - m - n), DOWN);
    return enc(n - 1 - (x - m - n - m), 0, LEFT);
}

bool in_board(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

void add_edge(int a, int b)
{
    go[a].push_back(b);
    go[b].push_back(a);
}

void dfs(int v)
{
    used[v] = true;
    for (int to : go[v])
        if (!used[to])
            dfs(to);
}

bool good()
{
    for (int i = 0; i < vcnt; i++)
        go[i].clear();

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            for (int d = 0; d < 4; d++)
            {
                int x = i + DX[d];
                int y = j + DY[d];
                if (!in_board(x, y))
                    continue;
                go[enc(i, j, d)].push_back(enc(x, y, d ^ 1));
            }

            if (board[i][j] == '/')
            {
                add_edge(enc(i, j, UP), enc(i, j, LEFT));
                add_edge(enc(i, j, RIGHT), enc(i, j, DOWN));
            }
            else
            {
                add_edge(enc(i, j, UP), enc(i, j, RIGHT));
                add_edge(enc(i, j, LEFT), enc(i, j, DOWN));
            }
        }

    for (int i = 0; i < vcnt; i++)
    {
        if (lover[i] == -1)
            continue;
        fill(used, used + vcnt, false);
        dfs(i);
        if (!used[lover[i]])
            return false;
        for (int j = 0; j < vcnt; j++)
            if (j != i && j != lover[i] && lover[j] != -1 && used[j])
                return false;
    }

    return true;
}

void solve()
{
    scanf("%d%d", &n, &m);
    vcnt = n * m * 4;

    fill(lover, lover + vcnt, -1);
    for (int i = 0; i < n + m; i++)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        x--; y--;
        x = conv(x);
        y = conv(y);
        lover[x] = y;
        lover[y] = x;
    }

    for (int mask = 0; mask < (1 << (n * m)); mask++)
    {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
            {
                int p = i * m + j;
                if (mask & (1 << p))
                    board[i][j] = '/';
                else
                    board[i][j] = '\\';
            }
        if (!good())
            continue;
        for (int i = 0; i < n; i++)
        {
            board[i][m] = 0;
            puts(board[i]);
        }
        return;
    }

    puts("IMPOSSIBLE");
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d:\n", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
