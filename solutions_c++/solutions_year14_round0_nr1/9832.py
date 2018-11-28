#include<stdio.h>
#include<algorithm>
using namespace std ;
int g[10][10],b[10][10] ;
int main()
{
    freopen("1.txt","r",stdin) ;
    freopen("2.txt","w",stdout) ;
    int x,y,q=1 ;
    int Tx ;
    scanf("%d",&Tx) ;
    while(Tx--)
    {
        scanf("%d",&x) ;
        for(int i=1 ;i<=4 ;i++)
          for(int j=1 ;j<=4 ;j++)
          scanf("%d",&g[i][j]) ;
          scanf("%d",&y) ;
        for(int i=1 ;i<=4 ;i++)
         for(int j=1 ;j<=4 ;j++)
          scanf("%d",&b[i][j]) ;
        int fx=0,t ;
        for(int i=1 ;i<=4 ;i++)
          for(int j=1 ;j<=4 ;j++)
            if(g[x][i]==b[y][j])
            {
                fx++ ;
                t=g[x][i] ;
            }
        if(!fx)
                 printf("Case #%d: Volunteer cheated!\n",q++) ;
        else if(fx==1)
                 printf("Case #%d: %d\n",q++,t) ;
        else     printf("Case #%d: Bad magician!\n",q++) ;
    }
    return 0 ;
}
