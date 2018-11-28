#include<stdio.h>
#include<iostream>
using namespace std;
char s[5][5];
bool check(char a)
{
    for(int i=0;i<4;i++)
    {
        if((s[i][0]==a)&&(s[i][3]==a)&&(s[i][1]==a)&&(s[i][2]==a))
            return true;
        if((s[0][i]==a)&&(s[3][i]==a)&&(s[1][i]==a)&&(s[2][i]==a))
            return true;
    }
    if((s[0][0]==a)&&(s[3][3]==a)&&(s[1][1]==a)&&(s[2][2]==a))
        return true;
    if((s[0][3]==a)&&(s[3][0]==a)&&(s[1][2]==a)&&(s[2][1]==a))
        return true;
}

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int n,i,j,cs=0;
    char c;
    scanf("%d ",&n);
    while(n--)
    {
        cs++;
        int x=5,y=5,k=0;
        for(i=0;i<4;i++)
        {
            gets(s[i]);
//            puts(s[i]);
            for(j=0;j<4;j++)
            {
                if(s[i][j]=='T')
                {
                    x=i;
                    y=j;
                }
                if((k==0)&&(s[i][j]=='.'))
                {
                    k=1;
                }
            }
        }
        int p=0;
        s[x][y]='O';
        p=check('O');
        if(p==1)
        {
            printf("Case #%d: O won\n",cs);
        }
        else
        {
            s[x][y]='X';
            int p=check('X');
            if(p==1)
            {
                printf("Case #%d: X won\n",cs);

            }
            else if(k==1)
            {
                printf("Case #%d: Game has not completed\n",cs);
            }
            else
            {
                printf("Case #%d: Draw\n",cs);
            }
        }
        getchar();
    }
}
