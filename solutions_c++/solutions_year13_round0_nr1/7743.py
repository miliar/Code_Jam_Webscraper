#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int find(char s[5][5], char x)
{
    for (int i = 0; i < 4; i++)
    {
        int re = 1;
        for (int j = 0; j < 4; j++)
        {
            if (s[i][j] != x && s[i][j] != 'T') re = -1;
            if (s[i][j] == 'T') re -= 1;
        }
        if (re >= 0) return 1;
    }
    for (int i = 0; i < 4; i++)
    {
        int re = 1;
        for (int j = 0; j < 4; j++)
        {
            if (s[j][i] != x && s[j][i] != 'T') re = -1;
            if (s[j][i] == 'T') re -= 1;
        }
        if (re >= 0) return 1;
    }
    int re = 1;
    for (int i = 0; i < 4; i++)
    {
        if (s[i][i] != x && s[i][i] != 'T') re = -1;
        if (s[i][i] == 'T') re -= 1;
    }
    if (re >= 0) return 1;
    re = 1;
    for (int i = 0; i < 4; i++)
    {
        if (s[i][3 - i] != x && s[i][3 - i] != 'T') re = -1;
        if (s[i][3 - i] == 'T') re -= 1;
    }
    if (re >= 0) return 1;
    return 0;
}

int filled(char s[5][5])
{
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (s[i][j] == '.') return 0;
    return 1;
}

int main()
{
    int t;
    
    freopen("A.in", "r", stdin);
    freopen("outA.txt", "w", stdout);
    
    cin >> t;
    for (int tc = 1; tc <= t; tc++)
    {
        printf("Case #%d: ", tc); 
        char s[5][5];
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
            {
                char tmp;
                cin >> tmp;
                //cout << tmp;
                while (tmp != '.' && tmp != 'O' && tmp != 'X' && tmp != 'T') 
                    cin >> tmp;
                s[i][j] = tmp;
            }
        if (find(s, 'X'))
            printf("X won\n");
        else if (find(s, 'O'))
            printf("O won\n");
        else if (filled(s))
            printf("Draw\n");
        else 
            printf("Game has not completed\n");
        if (tc < t)
            scanf("\n");
    }
    fclose(stdin);
    //system("pause");
    fclose(stdout);
    return 0;
}
