/***************************************************************************
                             problem_a.cpp  -
                             -------------------
    begin                : Sat 08 Apr 2017 00:59:40 CDT
    copyright            : (c) 2017 by Akarsh Simha
    email                : akarsh.simha@kdemail.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/


/* Project Includes */

/* STL Includes */
#include <iostream>
#include <string>
#include <assert.h>

int main() {
    int T;
    std::cin >> T;

    for ( int k = 0; k < T; ++k ) {
        std::string S;
        int K;
        int count = 0;
        std::cin >> S;
        std::cin >> K;
        int N = S.length();

        std::cout << "Case #" << ( k + 1 ) << ": ";

        auto flip = [&S, &N, &K]( int startIndex ) {
            for ( int l = startIndex; l < startIndex + K; ++l ) {
                assert( l < N );
                S[l] = ( S[l] == '+' ? '-' : '+' );
            }
        };

        for ( int j = 0; j <= N - K; ++j ) {
            if ( S[j] == '+' )
                continue;
            if ( S[j] == '-' ) {
                flip( j );
                ++count;
            }
        }

        bool valid = true;
        for ( int j = ( N - K + 1 > 0 ? N - K + 1 : 0 ); j < N; ++j )
            if ( S[j] == '-' ) {
                valid = false;
                break;
            }

        if ( valid ) {
            std::cout << count << std::endl;
        }
        else
            std::cout << "IMPOSSIBLE" << std::endl;

    }
}
