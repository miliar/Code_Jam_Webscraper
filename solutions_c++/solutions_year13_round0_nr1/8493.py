#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<iostream>
using namespace std;
int a[1111] , n , test;
char s[5][5];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("ans.out","w",stdout);
    while(scanf("%d",&test) != EOF)
    {
        int op = 1;
        while(test--)
        {
            for(int i = 0 ; i < 4 ; i++)scanf("%s",s[i]);
            printf("Case #%d: ",op++);
            bool yes = 0;
            for(int i = 0 ; i < 4 ; i++)
            {
                bool flag = 1;
                for(int j = 0 ; j < 4 ; j++)
                    if(s[i][j] != 'X' && s[i][j] != 'T')
                        flag = 0;
                if(flag)
                {
                    printf("X won\n");
                    yes = 1;
                    break;
                }
            }
            if(yes)continue;
            for(int i = 0 ; i < 4 ; i++)
            {
                bool flag = 1;
                for(int j = 0 ; j < 4 ; j++)
                    if(s[j][i] != 'X' && s[j][i] != 'T')
                        flag = 0;
                if(flag)
                {
                    printf("X won\n");
                    yes = 1;
                    break;
                }
            }
            if(yes)continue;
            for(int i = 0 ; i < 4 ; i++)
            {
                bool flag = 1;
                for(int j = 0 ; j < 4 ; j++)
                    if(s[i][j] != 'O' && s[i][j] != 'T')
                        flag = 0;
                if(flag)
                {
                    printf("O won\n");
                    yes = 1;
                    break;
                }
            }
            if(yes)continue;
            for(int i = 0 ; i < 4 ; i++)
            {
                bool flag = 1;
                for(int j = 0 ; j < 4 ; j++)
                    if(s[j][i] != 'O' && s[j][i] != 'T')
                        flag = 0;
                if(flag)
                {
                    printf("O won\n");
                    yes = 1;
                    break;
                }
            }
            if(yes)continue;
            bool flag = 1;
            for(int i = 0 ; i < 4 ; i++)
                if(s[i][i] != 'X' && s[i][i] != 'T')
                    flag = 0;
            if(flag)
            {
                printf("X won\n");
                continue;
            }
            for(int i = 0 ; i < 4 ; i++)
                if(s[i][3-i] != 'X' && s[i][3-i] != 'T')
                    flag = 0;
            if(flag)
            {
                printf("X won\n");
                continue;
            }
            flag = 1;
            for(int i = 0 ; i < 4 ; i++)
                if(s[i][i] != 'O' && s[i][i] != 'T')
                    flag = 0;
            if(flag)
            {
                printf("O won\n");
                continue;
            }
            flag = 1;
            for(int i = 0 ; i < 4 ; i++)
                if(s[i][3-i] != 'O' && s[i][i-3] != 'T')
                    flag = 0;
            if(flag)
            {
                printf("O won\n");
                continue;
            }
            for(int i = 0 ; i < 4 ; i++)
                for(int j = 0 ; j < 4 ; j++)
                    if(s[i][j] == '.')yes = 1;
            if(yes)
                printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
}
