#include <stdio.h>

void prt(int p, int q, int n);
int main()
{

    //----------------------
    FILE *fp1, *fp2;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("result_1.txt","w",stdout);
    //----------------------/    
    
    int ii,nn;
    scanf("%d\n",&nn);
    for (ii=1;ii<=nn;ii++)
    {
        int i,j;
        char a[5][5]={0};
        char c;
        int ff=0,f=0;
        int p=0,q=0;
        int tx=0,ty=0;
        for (i=1;i<=4;i++)
            {
             for (j=1;j<=4;j++)
                 {
                     a[i][j]=getchar();
                     if (a[i][j]=='.') ff=1;
                     if (a[i][j]=='T'){
                                       tx=i;
                                       ty=j;
                                       }
                 } 
                 c=getchar();
            }
        c=getchar();
        for (i=1;i<=4;i++)
        {
            p=0; q=0;
            if (a[i][1]=='X') p=1;
            if (a[i][1]=='O') q=1;
            for (j=2;j<=4;j++)
                {
                              if ((a[i][j]=='X')or(a[i][j]=='T'))
                                 {
                                                                 if ((a[i][j]==a[i][j-1])||(a[i][j]=='T')||(a[i][j-1]=='T')) p++;
                                                                    else p=1;
                                 }
                                 else p=0;
                              if ((a[i][j]=='O')||(a[i][j]=='T'))
                                 {
                                                                 if ((a[i][j]==a[i][j-1])||(a[i][j]=='T')||(a[i][j-1]=='T')) q++;
                                                                    else q=1;
                                 }
                                 else q=0;
                              if ((p==4)||(q==4)) f=1;
                }
            if (f==1) break;
        }
        if (f==1) prt(p,q,ii);
        if (f==0){
            for (j=1;j<=4;j++)
            {
                p=0; q=0;
                if (a[1][j]=='X') p=1;
                if (a[1][j]=='O') q=1;
                for (i=2;i<=4;i++)
                    {
                                  if ((a[i][j]=='X')or(a[i][j]=='T'))
                                     {
                                                                     if ((a[i-1][j]==a[i][j])||(a[i][j]=='T')||(a[i-1][j]=='T')) p++;
                                                                        else p=1;
                                     }
                                     else p=0;
                                  if ((a[i][j]=='O')||(a[i][j]=='T'))
                                     {
                                                                     if ((a[i-1][j]==a[i][j])||(a[i][j]=='T')||(a[i-1][j]=='T')) q++;
                                                                        else q=1;
                                     }
                                     else q=0;
                                  if ((p==4)||(q==4)) f=1;
                    }
                if (f==1) break;
            }
            if (f==1) prt(p,q,ii);
        }
        p=0; q=0;
        if (f==0){
                  a[tx][ty]='X';
                  if ((a[1][1]==a[2][2])&&(a[2][2]==a[3][3])&&(a[3][3]==a[4][4])&&(a[1][1]=='X'))
                  {
                     p=4;q=0;
                     f=1;
                     prt(p,q,ii);
                  }
                  a[tx][ty]='O';
                  if ((a[1][1]==a[2][2])&&(a[2][2]==a[3][3])&&(a[3][3]==a[4][4])&&(a[1][1]=='O'))
                  {
                     p=0;q=4;
                     f=1;
                     prt(p,q,ii);
                  }
                  a[tx][ty]='T';
                  }
        p=0; q=0;
        if (f==0){
                  a[tx][ty]='X';
                  if ((a[1][4]==a[2][3])&&(a[2][3]==a[3][2])&&(a[3][2]==a[4][1])&&(a[1][4]=='X'))
                  {
                     p=4;q=0;
                     f=1;
                     prt(p,q,ii);
                  }
                  a[tx][ty]='O';
                  if ((a[1][4]==a[2][3])&&(a[2][3]==a[3][2])&&(a[3][2]==a[4][1])&&(a[1][4]=='O'))
                  {
                     p=0;q=4;
                     f=1;
                     prt(p,q,ii);
                  }
                  a[tx][ty]='T';
                  }
        if (f==0) {
                  if (ff==1) printf("Case #%d: Game has not completed\n", ii);
                     else printf("Case #%d: Draw\n", ii);
                  }
    }
    return 0;
}
void prt(int p, int q, int i)
{
     if (p==4) {
               printf("Case #%d: X won\n", i);
               return;
               }
     if (q==4) {
               printf("Case #%d: O won\n", i);
               return;
               }
}
