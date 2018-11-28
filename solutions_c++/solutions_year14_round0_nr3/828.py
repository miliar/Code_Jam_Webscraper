#include <stdio.h>
#include <algorithm>
using namespace std;

#define TRANS(x,y,c) if (transpose) a[y][x] = c; else a[x][y] = c;

char a[1000][1000];

int main()
{
    int t;
    scanf("%d",&t);
    for (int l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);
        printf("\n");
        int r,c,m;
        scanf("%d %d %d",&r,&c,&m);

        if ( r == 1 )
        {
            
            int i;
            for (i=0;i<m;i++) printf("*");
            for (;i<c-1;i++) printf(".");
            printf("c\n");
            continue;
        }

        if ( c == 1 )
        {
            int i;
            for (i=0;i<m;i++) printf("*\n");
            for (;i<r-1;i++) printf(".\n");
            printf("c\n");
            continue;
        }

        bool transpose = false;
        if ( c > r )
        {
            transpose = true;
            int temp = c;
            c = r;
            r = temp;
        }

        int fill = r*c -m;

        if ( c == 2 && ( fill > 1 && fill % 2 == 1 || fill == 2 ))
        {
            printf("Impossible\n");
            continue;
        }
        if ( fill == 1 )
        {
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++)
                    TRANS(i,j,'*');
            }
            a[0][0] = 'c';
            goto print_label;
        }
        else if ( fill == 2 || fill == 3 || fill == 5 || fill == 7)
            printf("Impossible\n");
        else
        {

            for (int i=0;i<r;i++)
                for (int j=0;j<c;j++)
                   TRANS(i,j,'*');

            int x,y;


            if ( fill >= 2*c )
            {
                int f = fill;
                for (int i=0;i<r;i++)
                    for (int j=0;j<c;j++)
                    {
                        TRANS(i,j ,'.');
                        --f;
                        if ( f == 0 ) i=r,j=c; //in order to break
                    }
                a[0][0] = 'c';
                
                int k = fill /c;
                if ( fill % c == 1 )
                {
                    if ( k == 2 )
                    {
                        TRANS(0,c-1,'*');
                        TRANS(1,c-1, '*');
                        TRANS(2,1,'.');
                        a[2][2] ='.';
                    }
                    else 
                    {
                        TRANS(k-1,c-1, '*');
                        TRANS(k,1,'.');
                    }
                    
                }
                goto print_label;
            } 

            
           if ( fill % 2 == 0)
           {
                for (int i=0;i<fill/2;i++)
                {
                    TRANS(0,i,'.');
                    TRANS(1,i,'.');
                }
                a[0][0] = 'c';
           }

          if ( fill % 2 )
          {
              for (int i=0;i<3;i++)
                  for (int j=0;j<3;j++)
                      a[i][j] = '.';
              a[0][0] = 'c';

              for (int i=3;i<3+(fill-9)/2;i++)
              {
                   TRANS(0,i,'.');
                   TRANS(1,i,'.');
              } 
          }

print_label:

            if (transpose)
            {
                int temp = c;
                c = r;
                r = temp;
            }
            for (int i=0;i<r;i++)
            {
                for (int j=0;j<c;j++)
                    printf("%c",a[i][j]);

                printf("\n");
            }
           }
        }

    return 0;
}
