#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <math.h>
using namespace std;
#define MAX(a,b) a > b ? a : b
#define MIN(a,b) a < b ? a : b
#define INF 0x7fffffff
#define maxn 1001000
#define eps 10e-7

char a[5][5];

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    int T = 1;
    scanf("%d",&t);
    while(t--)
    {
        for(int i = 0; i < 4;i++)
        {
            scanf("%s",a[i]);
        }
//        for(int i = 0; i < 4; i++)
//        {
//            printf("%s",a[i]);
//            printf("\n");
//        }
        int is_complete = 1;
        int T_x,T_y,is_T = 0;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                if(a[i][j] == 'T')
                {
                    is_T = 1;
                    T_x = i;
                    T_y = j;
                }
                if(a[i][j] == '.')
                {
                    is_complete = 0;
                }
            }
        }
        printf("Case #%d: ",T++);
        int o_win = 0;
        int x_win = 0;
        if(is_T)
        {
            a[T_x][T_y] = 'X';
            for(int i = 0; i < 4; i++)
            {
                if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'X')
                {
                    x_win = 1;
                }
                else if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'O')
                {
                    o_win = 1;
                }
                if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'X')
                {
                    x_win = 1;
                }
                else if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'O')
                {
                    o_win = 1;
                }
            }
            if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'O')
            {
                o_win = 1;
            }
            if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'O')
            {
                o_win = 1;
            }
            a[T_x][T_y] = 'O';
            for(int i = 0; i < 4; i++)
            {
                if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'X')
                {
                    x_win = 1;
                }
                else if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'O')
                {
                    o_win = 1;
                }
                if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'X')
                {
                    x_win = 1;
                }
                else if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'O')
                {
                    o_win = 1;
                }
            }
            if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'O')
            {
                o_win = 1;
            }
            if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'O')
            {
                o_win = 1;
            }
            if(x_win && !o_win)
            {
                printf("X won\n");
            }
            else if(!x_win && o_win)
            {
                printf("O won\n");
            }
            else if(!x_win && !o_win && !is_complete)
            {
                printf("Game has not completed\n");
            }
            else if(!x_win && !o_win && is_complete)
            {
                printf("Draw\n");
            }
            continue;
        }
        else
        {
            a[T_x][T_y] = 'X';
            for(int i = 0; i < 4; i++)
            {
                if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'X')
                {
                    x_win = 1;
                }
                else if(a[i][0] == a[i][1] && a[i][0] == a[i][2] && a[i][0] == a[i][3] && a[i][0] == 'O')
                {
                    o_win = 1;
                }
                if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'X')
                {
                    x_win = 1;
                }
                else if(a[0][i] == a[1][i] && a[0][i] == a[2][i] && a[0][i] == a[3][i] && a[0][i] == 'O')
                {
                    o_win = 1;
                }
            }
            if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][0] == a[1][1] && a[0][0] == a[2][2] && a[0][0] == a[3][3] && a[0][0] == 'O')
            {
                o_win = 1;
            }
            if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'X')
            {
                x_win = 1;
            }
            else if(a[0][3] == a[1][2] && a[0][3] == a[2][1] && a[0][3] == a[3][0] && a[0][3] == 'O')
            {
                o_win = 1;
            }
            if(x_win && !o_win)
            {
                printf("X won\n");
            }
            else if(!x_win && o_win)
            {
                printf("O won\n");
            }
            else if(!x_win && !o_win && !is_complete)
            {
                printf("Game has not completed\n");
            }
            else if(!x_win && !o_win && is_complete)
            {
                printf("Draw\n");
            }
        }
    }
    return 0;
}
