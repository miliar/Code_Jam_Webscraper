#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;
#define MAX 105

int h , w , ady[ MAX ][ MAX ];

bool solve(){
    int i , j , k;

    for( i = 0 ; i < h ; ++i ){
        for( j = 0 ; j < w ; ++j ){
            bool b1 = true , b2 = true;
            for( k = 0 ; k < h ; ++k ){
                if( ady[ k ][ j ] > ady[ i ][ j ] ){ b1 = false; break; }
            }

            for( k = 0 ; k < w ; ++k ){
                if( ady[ i ][ k ] > ady[ i ][ j ] ){ b2 = false; break; }
            }
            if( !b1 && !b2 ) return false;
        }
    }
    return true;

}

int main(){

    int t , q , i , j;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    for( q = 1 ; q <= t && scanf("%d %d" , &h , &w ); ++q ){
        for( i = 0 ; i < h ; ++i )
            for( j = 0 ; j < w && scanf("%d" , &ady[ i ][ j ] ) ; ++j );
        printf("Case #%d: %s\n" , q ,  solve() == 1 ? "YES" : "NO" );
    }
    return 0;
}
