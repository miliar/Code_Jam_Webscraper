#include <iostream>
#include <fstream>
#include <map>

#define fs first
#define sc second

using namespace std;

pair<char, int> tb[105][105];
int cnt;

bool arrow(char c)
{
    return c == '>' || c == '<' || c == 'v' || c =='^';
}

int go(int r, int c, int x, int y)
{
    char ar, i = 0;
    while (1)
    {
        if (!(x >= 0 && x < r && y >=0 && y < c))
        {
            cnt++;
            break;
        }
        if (tb[x][y].sc <= 1)
        {
            tb[x][y].sc = 1;
            break;
        }
        if (arrow(tb[x][y].fs))
        {
            ar = tb[x][y].fs;
            if (i == 0)
                tb[x][y].sc = 0;
            else
                tb[x][y].sc = 1;
        }
        if (ar == '<')
        {
            x += 0;
            y += -1;
        }
        if (ar == '>')
        {
            x += 0;
            y += 1;
        }
        if (ar == 'v')
        {
            x += 1;
            y += 0;
        }
        if (ar == '^')
        {
            x += -1;
            y += 0;
        }
        ++i;
    }
}

int f(int r, int c)
{
    for (int i = 0; i < r; ++i)
        for (int i2 = 0; i2 < c; ++i2)
        {
            if (arrow(tb[i][i2].fs))
            {
                go(r, c, i, i2);
            }
        }

    for (int i = 0; i < r; ++i)
        for (int i2 = 0; i2 < c; ++i2)
        {
            int flag = 0;
            char ar1 = 0, ar2 = 0, ar3 = 0, ar4 = 0;
            if (tb[i][i2].sc == 0)
            {
                for (int x = i - 1; x >= 0; --x)
                {
                    if (tb[x][i2].sc <= 1)
                    {
                        flag = 1;
                        ar1 = '^';
                    }
                }
                for (int x = i + 1; x < r; ++x)
                {
                    if (tb[x][i2].sc <= 1)
                    {
                        flag = 1;
                        ar2 = 'v';
                    }
                }
                for (int y = i2 - 1; y >= 0; --y)
                {
                    if (tb[i][y].sc <= 1)
                    {
                        flag = 1;
                        ar3 = '<';
                    }
                }
                for (int y = i2 + 1; y < c; ++y)
                {
                    if (tb[i][y].sc <= 1)
                    {
                        flag = 1;
                        ar4 = '>';
                    }
                }
                //cerr << cnt << endl;
                //cerr << "flag = " << flag << endl;
                if (flag == 0) return -1;
                else
                {
                    //cerr << ar1 << " ";
                    //cerr << ar2 << " ";
                    //cerr << ar3 << " ";
                    //cerr << ar4 << " \n";
                    if (ar1 != tb[i][i2].fs &&
                        ar2 != tb[i][i2].fs &&
                        ar3 != tb[i][i2].fs &&
                        ar4 != tb[i][i2].fs)
                        {
                           //cnt++;
                        }
                }
            }
        }
    return cnt;
}

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int j = 1; j <= t; ++j)
    {
        int r, c;
        cnt = 0;
        cin >> r >> c;

        for (int i = 0; i < r; ++i)
            for (int i2 = 0; i2 < c; ++i2)
            {
                cin >> tb[i][i2].fs;
                tb[i][i2].sc = 5;
            }

        int ans = f(r, c);
        if (ans == -1)
            cout << "Case #" << j << ": IMPOSSIBLE"<< endl;
        else
            cout << "Case #" << j << ": " << ans << endl;
    }
}
