#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char str[10][10];

bool iswon(char ch)
{
    bool flag;

    //horizonal
    for (int i = 1; i <= 4; i++)
    {
        flag = true;
        for (int j = 1; j <= 4; j++)
        {
            if (str[i][j] != ch && str[i][j] != 'T')
            {
                flag = false;
            }
        }
        if (flag) return true;
    }

    //vertical
    for (int j = 1; j <= 4; j++)
    {
        flag = true;
        for (int i = 1; i <= 4; i++)
        {
            if (str[i][j] != ch && str[i][j] != 'T')
            {
                flag = false;
            }
        }
        if (flag) return true;
    }

    //diagonal
    flag = true;
    for (int i = 1; i <= 4; i++)
    {
        if (str[i][i] != ch && str[i][i] != 'T')
        {
            flag = false;
        }
    }
    if (flag) return true;

    //inverse diagonal
    flag = true;
    for (int i = 1; i <= 4; i++)
    {
        if (str[i][5-i] != ch && str[i][5-i] != 'T')
        {
            flag = false;
        }
    }
    if (flag) return true;

    return false;
}

bool isfill()
{
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            if (str[i][j] == '.') return false;
        }
    }
    return true;
}

int main()
{
    freopen("/home/zhj/Documents/A-large.in", "r", stdin);
    freopen("/home/zhj/Documents/A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        for (int i = 1; i <= 4; i++)
        {
            scanf("%s", str[i]+1);
        }

        if (iswon('X'))
        {
            printf("Case #%d: X won\n", cas);
        }
        else if (iswon('O'))
        {
            printf("Case #%d: O won\n", cas);
        }
        else if (isfill())
        {
            printf("Case #%d: Draw\n", cas);
        }
        else
        {
            printf("Case #%d: Game has not completed\n", cas);
        }
    }
    return 0;
}
