#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <string.h>

using namespace std;

char tictac[5][5];
char buf[10];

int check()
{
    for(int i = 1; i <= 4; i++)
    {
        int c1=0,c2=0,ct=0;
        for(int j = 1; j <= 4; j++)
        {
            if(tictac[i][j] == 'X')
                c1++;
            if(tictac[i][j] == 'O')
                c2++;
            if(tictac[i][j] == 'T')
                ct++;
        }
        if(c1 == 4 or (c1 == 3 and ct == 1))
            return 1;
        if(c2 == 4 or (c2 == 3 and ct == 1))
            return 2;
    }
    for(int i = 1; i <= 4; i++)
    {
        int c1=0,c2=0,ct=0;
        for(int j = 1; j <= 4; j++)
        {
            if(tictac[j][i] == 'X')
                c1++;
            if(tictac[j][i] == 'O')
                c2++;
            if(tictac[j][i] == 'T')
                ct++;
        }
        if(c1 == 4 or (c1 == 3 and ct == 1))
            return 1;
        if(c2 == 4 or (c2 == 3 and ct == 1))
            return 2;
    }

    int c1=0,c2=0,ct=0;

    for(int i = 1; i <= 4; i++)
    {
        if(tictac[i][i] == 'X')
            c1++;
        if(tictac[i][i] == 'O')
            c2++;
        if(tictac[i][i] == 'T')
            ct++;
    }
    if(c1 == 4 or (c1 == 3 and ct == 1)) return 1;
    if(c2 == 4 or (c2 == 3 and ct == 1)) return 2;

    int xi=1, yi=4;
    c1 = 0, c2 = 0, ct = 0;
    for(int i = 0; i < 4; i++)
    {
        if(tictac[xi][yi] == 'X')
            c1++;
        if(tictac[xi][yi] == 'O')
            c2++;
        if(tictac[xi][yi] == 'T')
            ct++;
        xi++;
        yi--;
    }
    if(c1 == 4 or (c1 == 3 and ct == 1)) return 1;
    if(c2 == 4 or (c2 == 3 and ct == 1)) return 2;

    int all=0;
    for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
            if(tictac[i][j] != '.') all++;
    if(all == 16) return 3;
    else
        return 4;
}

void solve(int t)
{
    for(int i = 1; i <= 4; i++)
    {
        gets(buf);
        for(int j = 0; j < 4; j++)
            tictac[i][j+1] = buf[j];
    }

    int ans = check();
    printf("Case #%d: ", t);
    if(ans == 1)
        printf("X won\n");
    else if(ans == 2)
        printf("O won\n");
    else if(ans == 3)
        printf("Draw\n");
    else
        printf("Game has not completed\n");
    gets(buf);
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cnt=0;
    int t; scanf("%d", &t); gets(buf);
    while(t--)
        solve(++cnt);
    return 0;
}
