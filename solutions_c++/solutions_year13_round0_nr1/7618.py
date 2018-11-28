#include<cstdio>
#include<cstring>

char map[10][10];

int solve()
{
    for (int i = 0; i < 4; i++)
    {
        int flag = 1;
        for (int j = 0; j < 4; j++)
            if (map[i][j] != 'X' && map[i][j] != 'T')
                flag = 0;
        if (flag)
            return 1;
        flag = 1;
        for (int j = 0; j < 4; j++)
            if (map[j][i] != 'X' && map[j][i] != 'T')
                flag = 0;
        if (flag)
            return 1;
    }
    int flag = 1;
    for (int i = 0; i < 4; i++)
        if (map[i][i] != 'X' && map[i][i] != 'T')
            flag = 0;
    if (flag)
        return 1;

        flag = 1;
    for (int i = 0; i < 4; i++)
        if (map[i][4-i-1] != 'X' && map[i][4-1-i] != 'T')
            flag = 0;
    if (flag)
        return 1;

     //////////////////////////////////////////////////////

    for (int i = 0; i < 4; i++)
    {
        int flag = 1;
        for (int j = 0; j < 4; j++)
            if (map[i][j] != 'O' && map[i][j] != 'T')
                flag = 0;
        if (flag)
            return 2;
        flag = 1;
        for (int j = 0; j < 4; j++)
            if (map[j][i] != 'O' && map[j][i] != 'T')
                flag = 0;
        if (flag)
            return 2;
    }
    flag = 1;
    for (int i = 0; i < 4; i++)
        if (map[i][i] != 'O' && map[i][i] != 'T')
            flag = 0;
    if (flag)
        return 2;

        flag = 1;
    for (int i = 0; i < 4; i++)
        if (map[i][4-i-1] != 'O' && map[i][4-1-i] != 'T')
            flag = 0;
    if (flag)
        return 2;
       //////////////////////////////////////////////////////////
    
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if(map[i][j] == '.')
                return 4;

     return 3;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int it = 1; it <= t; it++)
    {
        for (int i = 0; i < 4; i++)
            scanf("%s", map[i]);
        int ans = solve();
        if (ans == 1)
            printf("Case #%d: X won\n", it);
        else if (ans == 2)
            printf("Case #%d: O won\n", it);
        else if (ans == 3)
            printf("Case #%d: Draw\n", it);
        else 
            printf("Case #%d: Game has not completed\n", it);
    }
    return 0;
}
