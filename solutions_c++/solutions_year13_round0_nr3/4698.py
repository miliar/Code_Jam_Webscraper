//
//  main.cpp
//  acm
//
//  Created by Anton Kholkin on 4/6/13.
//  Copyright (c) 2013 Anton Kholkin. All rights reserved.
//

#include <iostream>
#include <map>
#include <vector>

#define MOD 1000000009

using namespace std;

vector<long long> pal;

bool isPal( long long x )
{
    char dig[ 200 ] = {0}, cnt = 0;
    while( x )
    {
        dig[ cnt++ ] = x % 10;
        x /= 10;
    }
    bool res= true;
    for ( int i = 0; res && i < cnt / 2; i++ )
        res &= dig[ i ] == dig[ cnt - i - 1 ];
    
    return res;
}
void preprocess()
{
    pal.push_back(0);
    for ( int i = 1; i < 10000001; i++ )
    {
        if ( isPal( i ) && isPal( 1LL * i * i ) )
            pal.push_back( 1LL * i * i );
    }
    pal.push_back(1000000000000000LL);
}

int main(int argc, const char * argv[])
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w+", stdout );

    int _; scanf( "%d", &_ );
    
    preprocess();
    
    for ( int tc = 0; tc < _; tc++ )
    {
        long long A[ 2 ], ind[ 2 ]; scanf( "%lld%lld", &A[ 0 ], &A[ 1 ] );
        A[ 0 ]--;
        for ( int i = 0; i < 2; i++ )
        {
            int l = 0, r = (int)pal.size() - 1;
            while( l < r )
            {
                int mid = l + ( r - l ) / 2 + 1;
                if ( pal[ mid ] < A[ i ] ) l = mid;
                else if ( pal[ mid ] > A[ i ] ) r = mid - 1;
                else l=r=mid;
            }
            ind[ i ] = l;
        }
        printf( "Case #%d: %lld\n", tc+1, ind[ 1 ] - ind[ 0 ] );
    }
    
    return 0;
}

