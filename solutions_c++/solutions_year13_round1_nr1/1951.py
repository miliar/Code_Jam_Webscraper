/**
 * ===========================================================================
 *
 *          @file  bullseye.cpp
 *         @brief  
 *
 *        @author  dengos (w), dengos.w@gmail.com, scut
 *       @version  1.0
 *          @date  04/27/2013 09:17:11 AM
 *
 * ===========================================================================
 */


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>


using std::cin;
using std::cout;

#define PI 3.1415926



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
    int T;
    long long r, t;
    long long estimate_k, k;
    long double tmp;

    cin >> T;

    for ( int i = 1; i <= T; ++i ) 
    {
        cin >> r >> t;
        tmp = (2*r-1)*(2*r-1)+4*2*t;
        tmp = (sqrtl(tmp) - (2*r-1)) / 4.0;
        k = tmp;
        cout << "Case #" << i << ": " << k << "\n";
    }

    return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */










