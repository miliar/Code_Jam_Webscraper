#include<cstdio>
#include<cstring>

using namespace std ;

int m1[4][4];
int m2[4][4];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _,ca=1;
    int x1,x2;
    int i , f, j,d;
    scanf ("%d", &_);
    while(_--)
    {
        scanf ("%d",&x1);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf ("%d",&m1[i][j]);
        scanf ("%d",&x2);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            scanf ("%d",&m2[i][j]);

        f=0;
        for ( i = 0 ; i < 4 ; i++ )
        {
            for(j = 0 ; j < 4 ; j++ )
            {
                if ( m1[x1-1][i] == m2[x2-1][j])
                    {
                        f++ ;
                        d=m1[x1-1][i];
                    }
            }
        }
        printf("Case #%d: ",ca++);
        if ( !f )
            puts("Volunteer cheated!");
            else if ( f > 1 )
                puts("Bad magician!");
            else printf("%d\n",d);
    }
    return 0 ;
}
