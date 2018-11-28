//iejr Header files
#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstring>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <limits.h>
#include <ctime>
#include <cctype>
#include <functional>
#include <utility>
#include <numeric>

using namespace std;

//iejr: Type defination
typedef unsigned long long int             ULLN;
typedef long long int                      LLN;
typedef vector<int>                        VI;
typedef vector<vector<int> >               VVI;
typedef vector<string>                     VS;
typedef vector<vector<string> >            VVS;


//iejr: Compile Options
//#define C11_Standard
//
#ifdef C11_Standard
    #include <unordered_set>
    #include <unordered_map>

    #define HASHSET                  unordered_set
    #define HASHMAP                  unordered_map;
#endif // C11_Standard


//iejr: Local Debug
#define INPUT_REDIRECTION


void flipPan( char *s, int nLeft, int nRight ){
    while( nLeft <= nRight ){
        int nTemp = s[nLeft];
        s[nLeft] = s[nRight] == '+' ? '-' : '+';
        s[nRight] = nTemp == '+' ? '-' : '+';

        ++nLeft;
        --nRight;
    }
}

//iejr: Main Function
int main()
{

#ifdef INPUT_REDIRECTION
    freopen( "B-large.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
#endif // INPUT_REDIRECTION

    int T = 0;
    scanf( "%d", &T );
    for( int i = 0;i < T;++i ){
        char sPan[505];
        memset( sPan, 0, 505 * sizeof( sPan[0] ) );

        scanf( "%s", sPan );
        int L = strlen( sPan );

        LLN nFlipCount = 0;
        for( int nRight = L - 1;nRight >= 0;--nRight ){
            if( sPan[nRight] == '+' ){
                continue;
            }

            if( sPan[0] == '+' ){
                for( int j = 0;j < nRight;++j ){
                    if( sPan[j] == '+' ){
                        sPan[j] = '-';
                    }
                    else{
                        break;
                    }
                }
                ++nFlipCount;
            }

            flipPan( sPan, 0, nRight );

            ++nFlipCount;

        //    printf( "%s : %lld\n", sPan, nFlipCount );
        }

        printf( "Case #%d: %lld\n", i + 1, nFlipCount );
    }

#ifdef INPUT_REDIRECTION
    fclose( stdin );
    fclose( stdout );
#endif // INPUT_REDIRECTION

    return 0;
}
