#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int n,i,j,t;
char a[8][8],ch;
bool fl;

int main()
{
    scanf("%d",& n);
    scanf("%c",& ch);
    for(t=1;t<=n;t++)
    {
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%c",& a[i][j]);
            scanf("%c",& ch);
        }
        printf("Case #%d: ", t);
        scanf("%c",& ch);

        //rows
        for(i=1;i<=4;i++)
        {
            fl=true;
            for(j=1;j<=4;j++)
                if (a[i][j]=='X' || a[i][j]=='.') {fl=false;break;}
            if (fl) break;
        }
        if (fl) { printf("O won\n");continue;}
        //cols
        for(j=1;j<=4;j++)
        {
            fl=true;
            for(i=1;i<=4;i++)
                if (a[i][j]=='X' || a[i][j]=='.') {fl=false;break;}
            if (fl) break;
        }
        if (fl) { printf("O won\n");continue;}
        //diagonals
        if ((a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T') && (a[4][4]=='O' || a[4][4]=='T'))
                            { printf("O won\n");continue;}

        if ((a[1][4]=='O' || a[1][4]=='T') && (a[2][3]=='O' || a[2][3]=='T') && (a[3][2]=='O' || a[3][2]=='T') && (a[4][1]=='O' || a[4][1]=='T'))
                            { printf("O won\n");continue;}


        //rows
        for(i=1;i<=4;i++)
        {
            fl=true;
            for(j=1;j<=4;j++)
                if (a[i][j]=='O' || a[i][j]=='.') {fl=false;break;}
            if (fl) break;
        }
        if (fl) { printf("X won\n");continue;}
        //cols
        for(j=1;j<=4;j++)
        {
            fl=true;
            for(i=1;i<=4;i++)
                if (a[i][j]=='O' || a[i][j]=='.') {fl=false;break;}
            if (fl) break;
        }
        if (fl) { printf("X won\n");continue;}
        //diagonals
        if ((a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T') && (a[4][4]=='X' || a[4][4]=='T'))
                            { printf("X won\n");continue;}

        if ((a[1][4]=='X' || a[1][4]=='T') && (a[2][3]=='X' || a[2][3]=='T') && (a[3][2]=='X' || a[3][2]=='T') && (a[4][1]=='X' || a[4][1]=='T'))
                            { printf("X won\n");continue;}

        //draw
        fl=true;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                if (a[i][j]=='.') {fl=false;break;}
            if (!fl) break;
        }
        if (fl) {printf("Draw\n");continue;}

        printf("Game has not completed\n");
    }
return 0;
}
