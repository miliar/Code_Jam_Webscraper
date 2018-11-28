#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
const int DIR_X[] = {0, 1, 0, -1, 1, 1, -1, -1};
const int DIR_Y[] = {1, 0, -1, 0, 1, -1, 1, -1};

int R, C, M;
map< int, vector< vector<char> > > ans;

vector< vector<char> > board;
bool visit[5][5];

int hash(int mine)
{
    return mine * 10000 + R * 100 + C;
}

void dfs2(int x, int y)
{
    if (!visit[x][y])
    {
        visit[x][y] = true;
        bool flag = board[x][y] != '*';
        for (int k = 0; k < 8 && flag; ++k)
        {
            int tx = x + DIR_X[k];
            int ty = y + DIR_Y[k];
            if (tx >= 0 && tx < R)
            {
                if (ty >= 0 && ty < C)
                {
                    if (board[tx][ty] == '*')
                    {
                        flag = false;
                    }
                }
            }
        }
        if (flag)
        {
            for (int k = 0; k < 8 && flag; ++k)
            {
                int tx = x + DIR_X[k];
                int ty = y + DIR_Y[k];
                if (tx >= 0 && tx < R)
                {
                    if (ty >= 0 && ty < C)
                    {
                        dfs2(tx, ty);
                    }
                }
            }
        }
    }
}

void dfs1(int index, int mine)
{
    int x = index / C;
    int y = index % C;
    if (index == R * C)
    {
        if (ans.find(hash(mine)) != ans.end())
        {
            return;
        }
        memset(visit, false, sizeof(visit));
        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            {
                if (board[i][j] == '.')
                {
                    dfs2(i, j);
                    bool flag = true;
                    for (int i = 0; i < R && flag; ++i)
                    {
                        for (int j = 0; j < C && flag; ++j)
                        {
                            if (board[i][j] == '.' && !visit[i][j])
                            {
                                flag = false;
                            }
                        }
                    }
                    if (flag)
                    {
                        ans[hash(mine)] = board;
                        ans[hash(mine)][i][j] = 'c';
                    }
                    return;
                }
            }
        }
        return;
    }
    dfs1(index + 1, mine);
    board[x][y] = '*';
    dfs1(index + 1, mine + 1);
    board[x][y] = '.';
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int cnt = 0;
    for (int i = 0; i < 5; ++i)
    {
        board.push_back(vector<char>());
        for (int j = 0; j < 5; ++j)
        {
            board[i].push_back('.');
        }
    }
    for (R = 1; R <= 5; ++R)
    {
        for (C = 1; C <= 5; ++C)
        {
            dfs1(0, 0);
        }
    }
    int T, M;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d%d", &R, &C, &M);
        printf("Case #%d: \n", t);
        if (ans.find(hash(M)) == ans.end())
        {
            puts("Impossible");
        }
        else
        {
            board = ans[hash(M)];
            for (int i = 0; i < R; ++i)
            {
                for (int j = 0; j < C; ++j)
                {
                    putchar(board[i][j]);
                }
                putchar('\n');
            }
        }
    }
    return 0;
}
