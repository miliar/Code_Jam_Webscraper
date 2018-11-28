#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    int tc; scanf( "%d", &tc );
    for ( int _ = 0; _ < tc; _++ ) {
        printf( "Case #%d: ", _+1 );
        int a, b, k; scanf( "%d%d%d", &a, &b, &k );
        int res = 0;
        for ( int i = 0; i < a; i++ ) {
            for ( int j = 0; j < b; j++ ) {
                res += (i&j) < k;
            }
        }
        printf( "%d", res );
        printf( "\n" );
    }
    
    return 0;
}
