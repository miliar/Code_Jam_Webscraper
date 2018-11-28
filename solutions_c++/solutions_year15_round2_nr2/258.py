#include <iostream>
#include <cstdio>

using namespace std;

const int N = 10005;
bool board[N][N];
int n, m;

void clear()
{
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            board[i][j] = false;
}

void paint(int cnt, int md)
{
    for(int i = 1; i < n - 1; i++)
        for(int j = 1; j < m - 1; j++)
            if((i + j) % 2 == md && cnt) { board[i][j] = true; cnt--; }

    for(int i = 0; i < n ; i++)
        for(int j = 0; j < m; j++)
            if(((i > 0 && i < n - 1) || (j > 0 && j < m - 1)) && (i + j) % 2 == md && cnt && !board[i][j]) { board[i][j] = true; cnt--; }

    for(int i = 0; i < n ; i++)
        for(int j = 0; j < m; j++)
            if((i + j) % 2 == md && cnt && !board[i][j]) { board[i][j] = true; cnt--; }
}

const int DI[] = { -1, 1, 0, 0 } ;
const int DJ[] = { 0, 0, -1, 1 } ;
int noise()
{
    int res = 0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            for(int d = 0; d < 4; d++)
            {
                int ii = i + DI[d], jj = j + DJ[d];
                if(ii < 0 || ii >= n) continue;
                if(jj < 0 || jj >= m) continue;
                res += !board[i][j] && !board[ii][jj];
            }
    return res / 2;
}

void draw()
{
    for(int i = 0; i < n; i++)
        for(int j = 0; j <= m; j++)
            printf("%c", j == m ? '\n' : board[i][j] ? '@' : '.');
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int test;
    scanf("%i", &test);

    for(int t = 1; t <= test; t++)
    {
        int num;
        scanf("%i %i %i", &n, &m, &num);

        bool flip = false;
        if(num <= (n * m + 1) / 2) { printf("Case #%i: 0\n", t); continue; }

        num = n * m - num;
        clear();
        paint(num, 0);
        int res = noise();
        clear();
        paint(num, 1);
        res = min(res, noise());

        printf("Case #%i: %i\n", t, res);
    }

    return 0;
}
