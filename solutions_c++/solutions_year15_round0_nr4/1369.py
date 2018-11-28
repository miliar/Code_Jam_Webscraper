#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std ;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int _ , ca = 1 ;
    int x , r , c ;
    int tmp ;
    scanf("%d",&_);
    while(_--)
    {
        scanf("%d%d%d",&x,&r,&c);
        if ( r > c )
        {
            tmp = r ;
            r = c ;
            c = tmp ;
        }
        printf("Case #%d: ",ca++) ;
        if ( x == 1 ) puts("GABRIEL");
        else if ( x == 2 )
        {
            if ( c >= 2 && c*r % 2 == 0 ) puts("GABRIEL");
            else puts("RICHARD");
        }
        else if ( x == 3 )
        {
            if ( r >= 2 && c >= 3 && r*c % 3 == 0 ) puts("GABRIEL");
            else puts("RICHARD");
        }
        else if ( x == 4 )
        {
            if ( r >= 3 && c >= 4 && r*c % 4 == 0 ) puts("GABRIEL");
            else puts("RICHARD");
        }
    }
    return  0 ;
}
