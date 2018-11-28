#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

char res[5][5];
int board[5][5], board1[5][5], c, r;

void disp(int r1, int c1)
{
    int i, j;
    for (i = 0; i < r; i++)
    {
        for (j = 0; j < c; j++)
        {
            if ((i == r1) && (j == c1)) res[i][j] = 'c';
            else
            {
                if (board[i][j]) res[i][j] = '*';
                else res[i][j] = '.';
            }
        }
    }
    return;
}

int minenum(int r1, int c1)
{
    int n = 0;
    if ((r1 > 0) && (c1 > 0)) if (board[r1 - 1][c1 - 1]) n++;
    if (r1 > 0) if (board[r1 - 1][c1]) n++;
    if ((r1 > 0) && (c1 < c - 1)) if (board[r1 - 1][c1 + 1]) n++;
    if (c1 > 0) if (board[r1][c1 - 1]) n++;
    if (c1 < c - 1) if (board[r1][c1 + 1]) n++;
    if ((r1 < r - 1) && (c1 > 0)) if (board[r1 + 1][c1 - 1]) n++;
    if (r1 < r - 1) if (board[r1 + 1][c1]) n++;
    if ((r1 < r - 1) && (c1 < c - 1)) if (board[r1 + 1][c1 + 1]) n++;
    return n;
}

void click(int r1, int c1)
{
    int i, j;
    if (board1[r1][c1] != -1) return;
    board1[r1][c1] = minenum(r1, c1);
    if (!board1[r1][c1])
    {
        if ((r1 > 0) && (c1 > 0)) click(r1 - 1, c1 - 1);
        if (r1 > 0) click(r1 - 1, c1);
        if ((r1 > 0) && (c1 < c - 1)) click(r1 - 1, c1 + 1);
        if (c1 > 0) click(r1, c1 - 1);
        if (c1 < c - 1) click(r1, c1 + 1);
        if ((r1 < r - 1) && (c1 > 0)) click(r1 + 1, c1 - 1);
        if (r1 < r - 1) click(r1 + 1, c1);
        if ((r1 < r - 1) && (c1 < c - 1)) click(r1 + 1, c1 + 1);
    }
}

int NumberOfSetBits(int i)
{
     i = i - ((i >> 1) & 0x55555555);
     i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
     return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

int main()
{
    bool done, found;
    int c1, cnt, i, i1, j, j1, k, l, m, m1, n, n0, res_i, res_j, r1, t, temp, temp1, x;
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    cin >> t;
    for (cnt = 1; cnt <= t; cnt++)
    {
        cin >> r; cin >> c; cin >> m;
        found = false; res_i = -1; res_j = -1; x = 0; n0 = r * c; n = 1; for (i = 0; i < n0; i++) n *= 2;
        for (i = 0; i < n; i++)
        {
            if (NumberOfSetBits(i) == m)
            {
                x++; temp = i;
                for (j = 0; j < n0; j++) { board[j / c][j % c] = temp % 2; temp /= 2; }
                for (j = 0; j < n0; j++)
                {
                    r1 = j / c; c1 = j % c;
                    if (!board[r1][c1])
                    {
                        for (i1 = 0; i1 < r; i1++) for (j1 = 0; j1 < c; j1++) board1[i1][j1] = (board[i1][j1] ? 9 : -1);
                        click(r1, c1);
                        done = true;
                        for (i1 = 0; i1 < r; i1++)
                        {
                            for (j1 = 0; j1 < c; j1++)
                            {
                                if (board1[i1][j1] == -1) { done = false; break; }
                            }
                            if (!done) break;
                        }
                        if (done) { found = true; res_i = i; res_j = j; disp(r1, c1); break; }
                    }
                }
                if (found) break;
            }
        }
        cout << "Case #" << cnt << ":" << endl;
        if (found)
        {
            for (i = 0; i < r; i++)
            {
                for (j = 0; j < c; j++) cout << res[i][j];
                cout << endl;
            }
        }
        else cout << "Impossible" << endl;
    }
    return 0;
}
