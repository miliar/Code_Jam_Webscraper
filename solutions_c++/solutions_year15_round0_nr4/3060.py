#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int testy;
    scanf("%d", &testy);
    for( int numer=1; numer<=testy; numer++)
    {
       int x, r, c;
       scanf("%d%d%d", &x, &r, &c);

       if( r*c%x != 0 or x>=7 or x > max( r, c) ) {
        printf("Case #%d: RICHARD\n", numer );
        continue;
       }
       if( x == 1)
       {
        printf("Case #%d: GABRIEL\n", numer );
        continue;
       }
       if( x>=4 and ( r<3 or c<3) )
       {
        printf("Case #%d: RICHARD\n", numer );
        continue;
       }


       if( x==3 and ( r==1 or c==1) )
       {
        printf("Case #%d: RICHARD\n", numer );
        continue;
       }
        printf("Case #%d: GABRIEL\n", numer );
    }
}
