#include <iostream>
#include <cstdio>

using namespace std;

int T, x_max, o_max;
char c[10][10];
int tx, to, tk;

int mmax(int x, int y)
{
    if (x>y)
    return x;
    return y;
}

void solve(int i, int j)
{
    tx = to = 0;
    int i1 = i, j1 = j;
    if (c[i][j] == 'X')
    {
        for (; j1<4; ++j1)
            if (c[i1][j1] == 'X' || c[i1][j1] == 'T')
                tx ++;
            else
                break;
        x_max = mmax(x_max, tx);
        tx = 0;
        i1 = i; j1 = j;
        for (; i1<4; ++i1)
            if (c[i1][j1] == 'X' || c[i1][j1] == 'T')
                tx ++;
            else
                break;
        x_max = mmax(x_max, tx);
        tx = 0;
        i1 = i; j1 = j;
        for (; i1<4 && j1<4; ++i1, ++j1)
        if (c[i1][j1] == 'X' || c[i1][j1] == 'T')
                tx ++;
            else
                break;
        x_max = mmax(x_max, tx);
        tx = 0;
        i1 = i; j1 = j;
        for (; i1<4 && j1>=0; ++i1, --j1)
        if (c[i1][j1] == 'X' || c[i1][j1] == 'T')
                tx ++;
            else
                break;
        x_max = mmax(x_max, tx);
    }
    if (c[i][j] == 'O')
    {
        for (; j1<4; ++j1)
            if (c[i1][j1] == 'O' || c[i1][j1] == 'T')
                to ++;
            else
                break;
        o_max = mmax(o_max, to);
        to = 0;
        i1 = i; j1 = j;
        for (; i1<4; ++i1)
            if (c[i1][j1] == 'O' || c[i1][j1] == 'T')
                to ++;
            else
                break;
        o_max = mmax(o_max, to);
        to = 0;
        i1 = i; j1 = j;
        for (; i1<4 && j1<4; ++i1, ++j1)
        if (c[i1][j1] == 'O' || c[i1][j1] == 'T')
                to ++;
            else
                break;
        o_max = mmax(o_max, to);
        to = 0;
        i1 = i; j1 = j;
        for (; i1<4 && j1>=0; ++i1, --j1)
        if (c[i1][j1] == 'O' || c[i1][j1] == 'T')
                to ++;
            else
                break;
        o_max = mmax(o_max, to);
    }
}

int main()
{
    freopen ("A-small-attempt2.in", "r", stdin);
    freopen ("A-small-attempt2.out", "w", stdout);
    int i=1, j, k;
    cin>>T;
    for (; i<=T; ++i)
    {
        tk = 0;
        x_max = o_max = 0;
        for (j=0; j<4; ++j)
            cin>>c[j];
        for (j=0; j<4; ++j)
            for (k=0; k<4; ++k)
            {
                if (c[j][k] == '.')
                    ++tk;
                else
                    solve (j, k);
                if (x_max == 4)
                {
                    printf ("Case #%d: X won\n", i);
                    goto a;
                }
                if (o_max == 4)
                {
                    printf ("Case #%d: O won\n", i);
                    goto a;
                }
            }
            if (tk)
                printf ("Case #%d: Game has not completed\n", i);
            else
                printf ("Case #%d: Draw\n", i);
    a:;
    }
    return 0;
}
