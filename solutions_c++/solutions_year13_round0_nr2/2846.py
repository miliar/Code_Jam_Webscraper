/**
 * ===========================================================================
 *
 *          @file  lawn.cpp
 *         @brief  
 *
 *        @author  dengos (w), dengos.w@gmail.com, scut
 *       @version  1.0
 *          @date  04/13/2013 07:46:44 AM
 *
 * ===========================================================================
 */




#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define MAXN 102
#define MAXM 102


using std::max;
using std::min;




/**
 * @brief
 *
 * @param argc
 * @param argv[]
 *
 * @return 0 if ok.
 */
    int
main ( int argc, char *argv[] )
{
    int T, N, M;
    int i, j, k, h;
    int lawn[MAXN][MAXM];
    int row_max[MAXN];
    int col_max[MAXM];
    bool ans;
    const char *msg = NULL;

    scanf ( "%d", &T );
    for ( i = 1; i <= T; ++i ) 
    {
        scanf ( "%d %d", &N, &M );
        memset(col_max, 0, sizeof col_max);
        memset(row_max, 0, sizeof row_max);
        for ( j = 0; j < N; ++j ) 
        {
            for ( k = 0; k < M; ++k ) 
            {
                scanf ( "%d", &lawn[j][k] );
                row_max[j] = max(row_max[j], lawn[j][k]);
                col_max[k] = max(col_max[k], lawn[j][k]);
            }
        }
        ans = true;

        for ( j = 0; j < N; ++j ) 
        {
            for ( k = 0; k < M; ++k ) 
            {
                h = min(row_max[j], col_max[k]);
                if (lawn[j][k] != h)    
                {
                    ans = false;
                    k = M;  j = N;
                }
            }
        }
        msg = ans ? "YES": "NO";
        printf ( "Case #%d: %s\n", i, msg );
    }

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */


