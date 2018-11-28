#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define mp make_pair
#define forn(i, n) for (i = 0; i < (int)(n); ++i)

char a[10][10];

bool f(char c)
{
    for (int i = 0; i < 4; ++i)
    {
        bool ok = true;
        for (int j = 0; j < 4; ++j)
            if (a[i][j] != c && a[i][j] != 'T')
            {
                ok = false;
                break;
            }
        if (ok)
            return true;
    }
    for (int j = 0; j < 4; ++j)
    {
        bool ok = true;
        for (int i = 0; i < 4; ++i)
        {
            if (a[i][j] != c && a[i][j] != 'T')
            {
                ok = false;
                break;
            }
        }
        if (ok)
            return true;
    }

    bool ok = true;
    for (int i = 0; i < 4; ++i)
    {
        if (a[i][i] != c && a[i][i] != 'T')
        {
            ok = false;
            break;
        }
    }
    if (ok)
        return true;
    ok = true;
    for (int i = 0; i < 4; ++i)
    {
        if (a[i][3 - i] != c && a[i][3 - i] != 'T')
        {
            ok = false;
            break;
        }
    }
    if (ok)
        return true;
    return false;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test = 1; test <= tests; ++test)
    {
        printf("Case #%d: ", test); 
        for (int i = 0; i < 5; ++i)
        {
            gets(a[i]);
        }

        if (f('X'))
            printf("X won\n");
        else if (f('O'))
            printf("O won\n");
        else
        {
            int cnt = 0;
            for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j)
                    if (a[i][j] == 'X' || a[i][j] == 'O' || a[i][j] == 'T')
                        ++cnt;
            if (cnt == 16)
                printf("Draw\n");
            else
                printf("Game has not completed\n");

        }
    }

    return 0;
}