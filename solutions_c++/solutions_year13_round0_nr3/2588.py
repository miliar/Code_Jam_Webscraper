/**
 * ===========================================================================
 *
 *          @file  sp_small.cpp
 *         @brief  
 *
 *        @author  dengos (w), dengos.w@gmail.com, scut
 *       @version  1.0
 *          @date  04/13/2013 08:04:13 AM
 *
 * ===========================================================================
 */


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>


using std::rotate;
using std::reverse;


bool
is_p ( int value )
{
    static char buf[10];
    bool ans = false;
    int rvalue = 0;

    sprintf ( buf, "%d", value );
    reverse(buf, buf+strlen(buf));
    sscanf ( buf, "%d", &rvalue );
    return value == rvalue;
}		/* -----  end of function is_p  ----- */


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
    int T, A, B, value;
    int sqrt_a, sqrt_value;
    int i, j, k;
    int ans;

    scanf ( "%d", &T );
    for ( i = 1; i <= T; ++i ) 
    {
        scanf ( "%d %d", &A, &B );
        ans = 0;

        for ( value = A; value <= B; ++value ) 
        {
            if (is_p(value))
            {
                sqrt_value = sqrt(value);
                if (sqrt_value * sqrt_value == value
                        && is_p(sqrt_value))
                    ++ans;
            }
        }

        printf ( "Case #%d: %d\n", i, ans );
    }

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */








