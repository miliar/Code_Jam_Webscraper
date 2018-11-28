#include <cstdio>
#include <string>
#include <iostream>

int main()
{
    int T = 0;
    scanf( "%d", &T );
    ::std::string s;
    for ( int t = 1; t <= T; ++t )
    {
        ::std::cin>>s;
        char check = '-'; // menos
        int count = 0;
        for ( int i = s.size() - 1; i >= 0; --i )
        {
            if ( s[i] == check )
            {
                count++;
                check = ( check == '-' ) ? '+' : '-' ;
            }
        }
        printf( "Case #%d: %d\n", t, count );
    }
}
