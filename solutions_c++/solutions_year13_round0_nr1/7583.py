#include <iostream>
#include <stdio.h>

using namespace std;

char check( char a, char b, char c, char d )
{
    if( a == b && a == c && a == d && a!='.')
        return a;
    else
    {
        if( a == 'T' && ( b == c && b == d ) && b != '.' )
            return b;
        else if( b == 'T' && ( a == c && a == d ) && a!= '.')
            return c;
        else if( c == 'T' && ( a == b && a == d ) && a != '.')
            return a;
        else if( d == 'T' && ( a == b && a == c ) && a!='.' )
            return a;
        else if( a == '.' || b =='.' || c =='.' || d == '.' )
            return 'n';
        else return 'c';
    }
}

int main()
{
    int tc;
    scanf("%d", &tc );
    int count = 0;

    while( tc -- )
    {
        count++;
        char **arr = new char*[4];
        for( int i = 0; i < 4; i ++ )
            arr[i] = new char[4];

        for( int i = 0; i < 4; i ++ )
           scanf("%s", arr[i] );

        bool incomplete = 0;


        char d1 = check( arr[0][0], arr[1][1], arr[2][2], arr[3][3]);
        char d2 = check( arr[0][3], arr[1][2], arr[2][1], arr[3][0] );
        if( d1 == 'X' || d2 == 'X' )
        {
            printf("Case #%d: X won\n", count );
            continue;
        }

        else if( d1 == 'O' || d2 == 'O' )
        {
            printf("Case #%d: O won\n", count );
            continue;
        }

        else if( d1 == 'n' || d2 == 'n' )
        {
            incomplete = 1;
        }

        bool cont = 0;
        for( int i = 0 ; i < 4; i ++ )
        {
            char r = check( arr[i][0], arr[i][1], arr[i][2], arr[i][3]);
            if( r == 'X' )
            {
                printf("Case #%d: X won\n", count );
                cont = 1;
                break;
            }
            if( r == 'O' )
            {
                printf("Case #%d: O won\n", count );
                cont = 1;
                break;
            }
            else if ( r == 'n' )
                incomplete = 1;

        }
        if( cont == 1 )
            continue;


        for( int i = 0 ; i < 4; i ++ )
        {
            char r = check( arr[0][i], arr[1][i], arr[2][i], arr[3][i]);
            if( r == 'X' )
            {
                printf("Case #%d: X won\n", count );
                cont = 1;
                break;
            }
            if( r == 'O' )
            {
                printf("Case #%d: O won\n", count );
                cont = 1;
                break;
            }
            else if ( r == 'n' )
                incomplete = 1;

        }
        if( cont == 1 )
            continue;


        if( incomplete == 1 )
            printf("Case #%d: Game has not completed\n", count );
        else
            printf("Case #%d: Draw\n", count );




    }
}
