////////////////////////////////////////////////////////////////////////////////
/**
 * @file main.cpp
 * @date 2016-04-08
 * @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
 *
 * @copyright Tiago Lobato Gimenes 2015. All rights reserved.
 *
 * @license GNU Public License version 3
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * @brief
 *
 * This file contains implementation of the correspoding header file, i.e. .hpp,
 * .hh or .h
 */
////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cstdlib>

////////////////////////////////////////////////////////////////////////////////

int solve_for( int N )
{
    int digits = 0, n = 1, aux;

    while( digits != 1023 )
    {
        aux = n * N;
        n++;
        while( aux != 0 )
        {
            digits = digits | (1 << (aux % 10));
            aux = aux / 10;
        }
    }

    return --n;
}

////////////////////////////////////////////////////////////////////////////////

int main( int argc, char** argv )
{
    int T, N;

    std::cin >> T; T++;
    for( int i=1; i < T; i++ )
    {
        std::cin >> N;
        if( N == 0 ) { std::cout << "Case #" << i << ": INSOMNIA" << std::endl; }
        else
            std::cout << "Case #" << i << ": " << solve_for(N) * N << std::endl;
    }


    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
