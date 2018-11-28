#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <cmath>
#include <set>

std :: set < uint64_t > set;

uint64_t reverse ( uint64_t i )
{
    uint64_t rev = 0;
    while ( i )
    {
        rev = rev * 10 + i % 10;
        i /= 10;
    }

    return rev;
}

bool isPalindrome ( uint64_t i )
{
    return i == reverse ( i );
}

void init ( void )
{
    for ( uint64_t i = 1; i <= 10e7; i++ )
    {
        if ( isPalindrome ( i ) && isPalindrome ( i * i ) )
            set . insert ( i * i );
    }

}

uint64_t Solve ( void )
{
    uint64_t src, dst, cnt = 0;
    scanf ( "%lu %lu\n", & src, & dst );

    std :: set < uint64_t > :: iterator it = set . begin ( );

    while ( * it <= dst )
    {
        if ( * it >= src )
            cnt ++;

        it ++;
    }

    return cnt;
}


int main ( void )
{
    init ( );
    int casesCnt;
    scanf ( "%d", & casesCnt );
    for ( int i = 1; i <= casesCnt; i++ )
        printf ( "Case #%d: %ld\n", i, Solve ( ) );
}
