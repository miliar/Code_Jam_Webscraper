#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "outputcookie.txt", "w", stdout );
    int T, count = 1;
    double C, F, X;
    scanf( "%d", &T );
    while( T-- )
    {
         scanf( "%lf", &C );
         scanf( "%lf", &F );
         scanf( "%lf", &X );
         double g = 2.0, current = X/2.0;
         double next = X/(g+F) + C/g;
         double bf = C/g;
         while( current > next )
         {
                current = next;
                g += F;
                next = X/(g+F) + (C/g + bf);
                bf += C/g;
               // printf( "%.7lf\n", next );
         }
         printf( "Case #%d: %.7lf\n", count++, current );
    }
}
