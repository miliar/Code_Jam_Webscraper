#include<stdio.h>
#include<string.h>

int amm;
char s[10][10];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int count=1;
    scanf("%d",&amm);
    while (amm--)
    {
        for (int i=0;i<4;i++)
        {
            scanf("%s",s[i]);
        }
        bool full=1,cirwin=0,crowin=0;
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                if (s[i][j]=='.'){full=0;break;}
            }
        }
        for (int i=0;i<4;i++)
        {
            int cir=0,cro=0;
            for (int j=0;j<4;j++)
            {
                if (s[i][j]=='X')cro++;
                else if (s[i][j]=='O')cir++;
                else if (s[i][j]=='T')
                {
                    cro++;cir++;
                }
            }
            if (cro==4)crowin=1;
            if (cir==4)cirwin=1;
        }
        for (int i=0;i<4;i++)
        {
            int cir=0,cro=0;
            for (int j=0;j<4;j++)
            {
                if (s[j][i]=='X')cro++;
                else if (s[j][i]=='O')cir++;
                else if (s[j][i]=='T')
                {
                    cro++;cir++;
                }
            }
            if (cro==4)crowin=1;
            if (cir==4)cirwin=1;
        }
        for (int i=0;i<1;i++)
        {
            int cir=0,cro=0;
            for (int j=0;j<4;j++)
            {
                if (s[j][j]=='X')cro++;
                else if (s[j][j]=='O')cir++;
                else if (s[j][j]=='T')
                {
                    cro++;cir++;
                }
            }
            if (cro==4)crowin=1;
            if (cir==4)cirwin=1;
        }
        for (int i=0;i<1;i++)
        {
            int cir=0,cro=0;
            for (int j=0;j<4;j++)
            {
                if (s[j][3-j]=='X')cro++;
                else if (s[j][3-j]=='O')cir++;
                else if (s[j][3-j]=='T')
                {
                    cro++;cir++;
                }
            }
            if (cro==4)crowin=1;
            if (cir==4)cirwin=1;
        }
        printf("Case #%d: ",count++);
        if (crowin)printf("X won\n");
        else if (cirwin)printf("O won\n");
        else if (full)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
