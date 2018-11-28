/** Libr@ries **/
#include "bits/stdc++.h"

using namespace std;
typedef long long LL;

int m1[ 5 ][ 5 ], m2[ 5 ][ 5 ];
int main(int argc, char const *argv[])
{
    int tc;
    cin >> tc;
    int rowFirst, rowSecond;
    int cases = 1;

    while ( tc-- ){
        cin >> rowFirst;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> m1[ i ][ j ];

        cin >> rowSecond;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> m2[ i ][ j ];

        set <int> setRow1;
        for ( int i = 0; i <4; i++ ){
            setRow1.insert( m1[ rowFirst-1 ][ i ] );
        }

        int repeat = 0, ans = -1;
        for ( int i = 0; i <4; i++ ){
            if ( setRow1.find( m2[ rowSecond-1 ][i]) != setRow1.end() ){
                ans = m2[ rowSecond-1 ][ i ];
               ++repeat;
            }
        }

        printf("Case #%d: ", cases++ );
        if ( repeat == 0 ){
            printf( "Volunteer cheated!\n" );
            continue;
        }
        if ( repeat == 1 ){
            printf("%d\n", ans);
        }else{
            printf("Bad magician!\n");
        }


    }
    return 0;
}