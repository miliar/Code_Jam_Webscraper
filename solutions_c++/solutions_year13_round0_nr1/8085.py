
#include<iostream>
#include<math.h>

using namespace std;
#define SIZE 4


char tic[4][4];

int xwin,owin,draw,moregame;

void checkwinning()
{
    int xset,yset,more,noresult;
    int i,j;

    int set = 0;



for(int k = 0;k<4;k++)
{
    for(i = 0; i<SIZE;i++)
        {
            if(i != 0 && k>1) break;
            xset = 0;
            yset = 0;
            more = 0;
            noresult = 0;
            for(j=0;j<SIZE && !noresult;j++)
            {
                char t;

                switch(k)
                {
                    case 0:
                    t = tic[j][i];
                    break;
                    case 1:
                    t =  tic[i][j];
                     break;
                    case 2:
                    {
                        t = tic[j][j];
                    }
                    break;
                    case 3:
                    {
                        t = tic[j][SIZE - j-1];
                    }
                    break;
                }
                switch(t)
                {
                    case 'X':
                    {
                        if(yset) noresult = 1;
                        if(xset) continue;
                        else xset =1;
                    }
                    break;
                    case 'O':
                    {
                        if(xset) noresult = 1;
                        if(yset) continue;
                        else yset =1 ;
                    }
                    break;
                    case '.':
                    {
                        more = 1;
                    }
                    break;
                }
            }

            if(!noresult)
            {
            if(xset)
            {
                if(more)  moregame = 1;
                else
                {
                    xwin = 1;
                    return;
                }
            }

            else if(yset)
            {
                if(more)  moregame = 1;
                else
                {
                owin = 1;
                return;
                }
            }
            else if(!yset && !xset && more)  moregame = 1;
            }

        }
}
}

int main()
{
    int t,kk,numsqrt;
    int start,end;
    int i,j;

    freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

    scanf("%d",&t);

    for(kk=0;kk<t;kk++)
    {
        xwin = 0;
        owin = 0;
        draw = 0;
        moregame = 0;


        for(i = 0; i<SIZE;i++)
        {
            scanf("%s",tic[i]);
        }



        checkwinning();



       /* for(i = 0; i<SIZE;i++)
        {
            for(j=0;j<SIZE;j++)
            {
                printf("%c",tic[i][j]);
            }
            printf("\n");
        }

        printf("\n");*/

        if(xwin) printf("Case #%d: X won\n",kk+1);
        else if(owin) printf("Case #%d: O won\n",kk+1);
        else if(moregame) printf("Case #%d: Game has not completed\n",kk+1);
        else printf("Case #%d: Draw\n",kk+1);


        //printf("\n\n");









        //printf("Case #%d: %d\n",kk+1,numsqrt);
    }

    return 1;
}
