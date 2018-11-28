#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#include<list>
#include<cmath>
#include<cstdlib>

using namespace std;

#define     PI      3.1428571
#define     UL      unsigned long int
#define     ULL      unsigned long long int

#define     GETI(k)      scanf("%d",&k)
#define     GETUL(k)    scanf("%lu",&k)
#define     GETULL(k)    scanf("%llu",&k)
#define     GETF(k)      scanf("%f",&k)
#define     GETC(k)     scanf("%c",&k)
#define     GETCP(k)   scanf("%s",&k) //char pointer
#define     GETS(k)     scanf("%s",k)  //string

#define     PUTI(k)     printf("%d",k)
#define     PUTUL(k)   printf("%lu",k)
#define     PUTULL(k)   printf("%llu",k)
#define     PUTF(k)     printf("%f",k)
#define     PUTC(k)     printf("%c",k)
#define     PUTS(k)     printf("%s",k)
#define     PUTK(k)     printf(k)           //hard coded string
#define     NL    printf("\n")

int main()
{
    int n,m,tc;
    GETI(tc);
    for(int t=1; t<=tc; t++)
    {
        bool founddot=false;
        char a[4][4];
        char d;
        GETC(d);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
                GETC(a[i][j]);
            GETC(d);
        }
        //check row
        bool xwon=false;
        bool owon=false;
        for(int i=0; i<4 && !xwon && !owon; i++)
        {
            int numx=0;
            int numo=0;
            if(a[i][0]=='X' || a[i][0]=='T')
            {
                numx++;
                for(int j=1; j<4; j++) //scan colwise
                {
                    if(a[i][j]=='X' || a[i][j]=='T')
                        numx++;
                    else if(a[i][j]=='.')
                        founddot=true;
                }
                if(numx==4)
                {
                    xwon=true;
                }
            }
            else if(a[i][0]=='O' || a[i][0]=='T')
            {
                numo++;
                for(int j=1; j<4; j++)
                {
                    if(a[i][j]=='O' || a[i][j]=='T')
                        numo++;
                    else if(a[i][j]=='.')
                        founddot=true;
                }
                if(numo==4)
                    owon=true;
            }
             else
                founddot=true;
        }

        //check col
        if(!xwon && !owon)
        {
            for(int j=0; j<4 && !xwon && !owon; j++)
            {
                int numx=0;
                int numo=0;
                if(a[0][j]=='X' || a[0][j]=='T')
                {
                    numx++;
                    for(int i=1; i<4; i++) //scan col
                    {
                        if(a[i][j]=='X' || a[i][j]=='T')
                            numx++;
                        else if(a[i][j]=='.')
                            founddot=true;

                    }
                    if(numx==4)
                    {
                        xwon=true;
                    }

                }
                else if(a[0][j]=='O' || a[0][j]=='T')
                {
                    numo++;
                    for(int i=1; i<4; i++)
                    {
                        if(a[i][j]=='O' || a[i][j]=='T')
                            numo++;
                        else if(a[i][j]=='.')
                            founddot=true;
                    }
                    if(numo==4)
                        owon=true;
                }
                 else
                founddot=true;
            }
        }

        if(!xwon && !owon)
        {
            //diagonal
            int numx=0;
            int numo=0;
            int i=0;
            if(a[0][0]=='X' || a[0][0]=='T')
            {
                numx++;
                for(int i=1; i<4; i++) //scan col
                {
                    if(a[i][i]=='X' || a[i][i]=='T')
                        numx++;
                    else if(a[i][i]=='.')
                        founddot=true;
                }
                if(numx==4)
                    xwon=true;
            }
            else if(a[0][0]=='O' || a[0][0]=='T')
            {
                numo++;
                for(int i=1; i<4; i++)
                {
                    if(a[i][i]=='O' || a[i][i]=='T')
                        numo++;
                    else if(a[i][i]=='.')
                        founddot=true;
                }
                if(numo==4)
                    owon=true;
            }
             else
                founddot=true;


            if(!xwon && !owon)
            {
                //other diagonal
                int numx=0;
                int numo=0;
                int i=0;
                if(a[0][3]=='X' || a[0][3]=='T')
                {
                    numx++;
                    for(int i=1; i<4; i++) //scan col
                    {
                        if(a[i][3-i]=='X' || a[i][3-i]=='T')
                            numx++;
                        else if(a[i][3-i]=='.')
                            founddot=true;
                    }
                    if(numx==4)
                        xwon=true;
                }
                else if(a[0][3]=='O' || a[0][3]=='T')
                {
                    numo++;
                    for(int i=1; i<4; i++)
                    {
                        if(a[i][3-i]=='O' || a[i][3-i]=='T')
                            numo++;
                        else if(a[i][3-i]=='.')
                            founddot=true;
                    }
                    if(numo==4)
                        owon=true;
                }
                 else
                founddot=true;
            }
        }

        if(xwon)
            printf("Case #%d: X won\n",t);
        else if(owon)
            printf("Case #%d: O won\n",t);
        else if(!xwon && !owon && founddot)
            printf("Case #%d: Game has not completed\n",t);
        else if(!xwon && !owon && !founddot)
            printf("Case #%d: Draw\n",t);
    }

    return 0;
}
