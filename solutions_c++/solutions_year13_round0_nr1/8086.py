#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <ctime>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
char p[101][101];
int judge()
{
    int i,j;
    for(i = 0;i < 4;i ++)
    {
        if(p[i][i] == '.'||p[i][i] == 'O')
        break;
    }
    if(i == 4) return 1;
    for(i = 0;i < 4;i ++)
    {
        if(p[i][3-i] == '.'||p[i][3-i] == 'O')
        break;
    }
    if(i == 4) return 1;
    for(i = 0;i < 4;i ++)
    {
        if(p[i][i] == '.'||p[i][i] == 'X')
        break;
    }
    if(i == 4) return 3;
    for(i = 0;i < 4;i ++)
    {
        if(p[i][3-i] == '.'||p[i][3-i] == 'X')
        break;
    }
    if(i == 4) return 3;
    for(i = 0;i < 4;i ++)
    {
        for(j = 0;j < 4;j ++)
        {
            if(p[i][j] == '.'||p[i][j] == 'O')
            break;
        }
        if(j == 4) return 1;
        for(j = 0;j < 4;j ++)
        {
            if(p[j][i] == '.'||p[j][i] == 'O')
            break;
        }
        if(j == 4) return 1;
    }
    for(i = 0;i < 4;i ++)
    {
        for(j = 0;j < 4;j ++)
        {
            if(p[i][j] == '.'||p[i][j] == 'X')
            break;
        }
        if(j == 4) return 3;
        for(j = 0;j < 4;j ++)
        {
            if(p[j][i] == '.'||p[j][i] == 'X')
            break;
        }
        if(j == 4) return 3;
    }
    for(i = 0;i < 4;i ++)
    {
        for(j = 0;j < 4;j ++)
        {
            if(p[i][j] == '.')
            return 4;
        }
    }
    return 2;
}
int main()
{
    int t,cas = 1,i;
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        for(i = 0;i < 4;i ++)
        scanf("%s",p[i]);
        printf("Case #%d: ",cas++);
        i = judge();
        if(i == 1)
        printf("X won\n");
        else if(i == 2)
        printf("Draw\n");
        else if(i == 3)
        printf("O won\n");
        else if(i == 4)
        printf("Game has not completed\n");
    }
    return 0;
}
