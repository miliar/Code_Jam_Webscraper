#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int main(){
freopen("A-small-attempt1.in","r",stdin);
freopen("A-small-attempt1.txt","w",stdout);
int test,t,i,j,k,ti,tj;
char s[5][5];
scanf("%d",&t);
getchar();
for(test=1;test<=t;test++)
{
    int dot=0;
    for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                s[i][j]=getchar();
                if (s[i][j]=='.')
                    dot++;
                else if (s[i][j]=='T')
                {
                    ti=i;
                    tj=j;
                }
            }
            getchar();
        }
    getchar();
    printf("Case #%d: ",test);
    /*for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        putchar(s[i][j]);
    putchar('\n');
    } */
    s[ti][tj]='X';
    char ans='\0';
    for(i=1;i<=4;i++)
    {
        if (s[i][1]=='X' && s[i][1]==s[i][2] && s[i][2]==s[i][3] && s[i][3]==s[i][4])
        {
            ans='X';
            break;
        }
    }
    if (ans=='X')
    {
        puts("X won");
        continue;
    }
    for(i=1;i<=4;i++)
    {
        if (s[1][i]=='X' && s[1][i]==s[2][i] && s[2][i]==s[3][i] && s[3][i]==s[4][i])
        {
            ans='X';
            break;
        }
    }
    if (ans=='X')
    {
        puts("X won");
        continue;
    }
    if (s[1][1]=='X' && s[1][1]==s[2][2] && s[2][2]==s[3][3] && s[3][3]==s[4][4])
    {
        puts("X won");
        continue;
    }
    if (s[1][4]=='X' && s[1][4]==s[2][3] && s[2][3]==s[3][2] && s[3][2]==s[4][1])
    {
        puts("X won");
        continue;
    }


    s[ti][tj]='O';
    for(i=1;i<=4;i++)
    {
        if (s[i][1]=='O' && s[i][1]==s[i][2] && s[i][2]==s[i][3] && s[i][3]==s[i][4])
        {
            ans='O';
            break;
        }
    }
    if (ans=='O')
    {
        puts("O won");
        continue;
    }

    for(i=1;i<=4;i++)
    {
        if (s[1][i]=='O' && s[1][i]==s[2][i] && s[2][i]==s[3][i] && s[3][i]==s[4][i])
        {
            ans='O';
            break;
        }
    }
    if (ans=='O')
    {
        puts("O won");
        continue;
    }
    if (s[1][1]=='O' && s[1][1]==s[2][2] && s[2][2]==s[3][3] && s[3][3]==s[4][4])
    {
        puts("O won");
        continue;
    }
    if (s[1][4]=='O' && s[1][4]==s[2][3] && s[2][3]==s[3][2] && s[3][2]==s[4][1])
    {
        puts("O won");
        continue;
    }
    if (dot==0)
        puts("Draw");
    else puts("Game has not completed");



}

return 0;
}
