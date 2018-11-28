#include <iostream>
#include <stdio.h>

using namespace std;

bool sol(int a , int b , int c ) {
    if ( a == 1 )
        return 0 ;
    if ( a == 2 ) {
        if ( !((b*c)%2) )
            return 0;
        return 1;
    }
    if ( a == 3 ) {
        if ( b*c == 6 || b*c == 12 || b*c == 9 )
            return 0 ;
        return 1 ;
    }
    if ( a == 4 ) {
        if ( b*c == 16 || b*c == 12 )
            return 0 ;
        return 1 ;
    }
}
int main()
{
    //freopen("D-small-attempt6.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t , a ,b,c;
    scanf("%d",&t);
    for ( int z = 1 ; z <= t ; z++ ) {
        scanf("%d%d%d",&a,&b,&c);
        if ( sol(a,b,c) )
            printf("Case #%d: RICHARD\n",z);
        else
            printf("Case #%d: GABRIEL\n",z);
    }
    return 0;
}
