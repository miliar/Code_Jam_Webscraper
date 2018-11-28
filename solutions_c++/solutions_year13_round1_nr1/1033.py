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
#include <math.h>

#define MOD 1000000000000000007LL

using namespace std;

int main(int argc, const char * argv[])
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w+", stdout );
    
    int _; scanf( "%d", &_ );
    
    for ( int tc = 0; tc < _; tc++ )
    {
        printf( "Case #%d: ", tc+1 );
        long long r, t; scanf( "%lld%lld", &r, &t );

        long long left = 0, right = min( 1000000000LL, 2000000000000000000LL / ( 2 * r ) );
        
        while( left < right )
        {
            long long mid = left + ( right - left ) / 2 + 1;
//            if ( mid > 1000000000 )
            long long curr = 1LL * ( 2 * r + 2 * mid - 1 ) * mid;
            if ( curr < 0 )
            {
                curr = curr;
            }
            if ( curr > t ) right = mid - 1;
            else {
                left = mid;   
            }
        }
        long long res = left;
            
        printf( "%lld", res );
        printf( "\n" );
    }
    return 0;
}

