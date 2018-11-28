#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    scanf("%d",&n);
    for(int ss=1; ss<=n; ss++)
    {
        char s[4][4];
        for(int t=0; t<4; t++)
        {
            scanf(" %s",s[t]);
        }
        int ans=0;
        for(int t=0; t<4; t++)
        {
            if(s[t][0]=='X'or s[t][0]=='T')
                if(s[t][1]=='X'or s[t][1]=='T')
                    if(s[t][2]=='X'or s[t][2]=='T')
                        if(s[t][3]=='X'or s[t][3]=='T')
                        {
                            ans=1;
                            break;
                        }
            if(s[t][0]=='O'or s[t][0]=='T')
                if(s[t][1]=='O'or s[t][1]=='T')
                    if(s[t][2]=='O'or s[t][2]=='T')
                        if(s[t][3]=='O'or s[t][3]=='T')
                        {
                            ans=2;
                            break;
                        }
        }
        for(int t=0; t<4; t++)
        {
            if(s[0][t]=='X'or s[0][t]=='T')
                if(s[1][t]=='X'or s[1][t]=='T')
                    if(s[2][t]=='X'or s[2][t]=='T')
                        if(s[3][t]=='X'or s[3][t]=='T')
                        {
                            ans=1;
                            break;
                        }
            if(s[0][t]=='O'or s[0][t]=='T')
                if(s[1][t]=='O'or s[1][t]=='T')
                    if(s[2][t]=='O'or s[2][t]=='T')
                        if(s[3][t]=='O'or s[3][t]=='T')
                        {
                            ans=2;
                            break;
                        }
        }
        if(s[0][0]=='X' or s[0][0]=='T')
        if(s[1][1]=='X' or s[1][1]=='T')
        if(s[2][2]=='X' or s[2][2]=='T')
        if(s[3][3]=='X' or s[3][3]=='T')
        ans=1;
        if(s[0][0]=='O' or s[0][0]=='T')
        if(s[1][1]=='O' or s[1][1]=='T')
        if(s[2][2]=='O' or s[2][2]=='T')
        if(s[3][3]=='O' or s[3][3]=='T')
        ans=2;
        if(s[0][3]=='X' or s[0][3]=='T')
        if(s[1][2]=='X' or s[1][2]=='T')
        if(s[2][1]=='X' or s[2][1]=='T')
        if(s[3][0]=='X' or s[3][0]=='T')
        ans=1;
        if(s[0][3]=='O' or s[0][3]=='T')
        if(s[1][2]=='O' or s[1][2]=='T')
        if(s[2][1]=='O' or s[2][1]=='T')
        if(s[3][0]=='O' or s[3][0]=='T')
        ans=2;
        printf("Case #%d: ",ss);
        if(ans!=0)
        {
            if(ans==1)
            {
                printf("X won\n");
            }
            else
            {
                printf("O won\n");
            }
        }
        else
        {
            int qq=0;
            for(int i=0; i<4; i++)
            {
                for(int j=0; j<4; j++)
                {
                    if(s[i][j]=='.')
                    {
                        qq=1;
                    }
                }
            }
            if(qq)
                printf("Game has not completed\n");
            else
                printf("Draw\n");
        }

    }
    fclose(stdin);
	fclose(stdout);
}
