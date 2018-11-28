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
        int a1, a2;
        int g1[4][4], g2[4][4];
        scanf( "%d", &a1 );
        a1--;
        vector<int> ch;
        for ( int i = 0; i < 4; i++ ) {
            for ( int j = 0; j < 4; j++ ) {
                scanf( "%d", &g1[i][j] );
                if ( i == a1 ) {
                    ch.push_back(g1[i][j]);
                }
            }
        }
        scanf( "%d", &a2 );
        a2--;
        int cnt = 0, val;
        for ( int i = 0; i < 4; i++ ) {
            for ( int j = 0; j < 4; j++ ) {
                scanf( "%d", &g2[i][j] );
                if ( i == a2 ) {
                    for ( int k = 0; k < 4; k++ ) {
                        if ( ch[k] == g2[i][j] ) {
                            cnt++;
                            val = ch[k];
                        }
                    }
                }
            }
        }
        if ( cnt == 0 ) {
            printf( "Volunteer cheated!" );
        }
        else if ( cnt == 1 ) {
            printf( "%d", val );
        }
        else {
            printf( "Bad magician!" );
        }
        
        printf( "\n" );
    }
    
    return 0;
}
