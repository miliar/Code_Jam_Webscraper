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


//iejr: Main Function
int main()
{

#ifdef INPUT_REDIRECTION
    freopen( "A-large.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
#endif // INPUT_REDIRECTION

    int T = 0;
    scanf( "%d", &T );

    for( int i = 0;i < T;++i ){
        LLN N = 0;
        scanf( "%lld", &N );

        if( N <= 0 ){
            printf( "Case #%d: INSOMNIA\n", i + 1 );
            continue;
        }

        int nHash = 0;
        for( int j = 0;j < 10;++j ){
            nHash |= ((int)1) << j;
        }

        LLN lOrg = N;
        while( nHash != 0 ){
            LLN nCopy = N;
            while( nCopy > 0 ){
                int nDigit = nCopy % 10;
                nHash &= ~( (int)1 << nDigit );

                nCopy /= 10;
            }

            if( nHash == 0 ){
                printf( "Case #%d: %lld\n", i + 1, N );
                break;
            }

            N += lOrg;
        }
    }

#ifdef INPUT_REDIRECTION
    fclose( stdin );
    fclose( stdout );
#endif // INPUT_REDIRECTION

    return 0;
}
