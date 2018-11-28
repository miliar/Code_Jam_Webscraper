////////////////////////////////////////////////////////////////////////////////
/**
 * @file main.cpp
 * @date 2016-04-09
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
#include <cassert>
#include <vector>

////////////////////////////////////////////////////////////////////////////////

using ulld = unsigned long long int;

////////////////////////////////////////////////////////////////////////////////

ulld get_elem_pos_at_complexity( ulld i, int C, int K )
{
    ulld pos=i;

    for( int j=1; j < C; j++ )
        pos = (pos/K)*K*K + i*(K+1);

    return pos;
}

////////////////////////////////////////////////////////////////////////////////

void small_solver( int K, int C, int S )
{
    assert( K == S );

    for( int i=0; i < K; i++ )
        std::cout << 1 + get_elem_pos_at_complexity( i, C, K ) << " ";

}

////////////////////////////////////////////////////////////////////////////////

void generate_for_base( int K, int C, const std::vector< bool >& base )
{
    std::vector< bool > G(K, true);
    std::vector< bool > gen1, gen2, *cur, *work, *aux;

    gen1 = base;
    cur = &gen1;
    work = &gen2;
    for( int i=1; i < C; i++ )
    {
        for( auto elem: *cur )
        {
            if( elem )
                work->insert( work->end(), G.begin(), G.end() );
            else
                work->insert( work->end(), base.begin(), base.end() );
        }
        aux = work;
        work = cur;
        cur = aux;
        work->clear();
    }

    for( auto b: *cur )
    {
        if( b )
            std::cout << "G";
        else
            std::cout << "L";
    }
}

////////////////////////////////////////////////////////////////////////////////

void generate_bases( int K, int C )
{
    std::vector< bool > base(K, true);
    int counter = 0, aux;

    for( int i=0; i < K; i++ ) counter = counter | (1 << i);

    while( counter >= 0 )
    {
        generate_for_base( K, C, base );
        std::cout << std::endl;
        
        counter -= 1;
        
        aux=counter;
        for( int i=0; i < K; i++ )
        {
            if( aux % 2 ) base[i] = true;
            else base[i] = false;
            aux >>= 1;
        }
    }
}

////////////////////////////////////////////////////////////////////////////////

int main( int argc, char** argv )
{
    int T,K,C,S;

    std::cin >> T;
    for( int i=1; i <= T; i++ )
    {
        std::cin >> K;
        std::cin >> C;
        std::cin >> S;

        std::cout << "Case #" << i << ": ";
        small_solver( K, C, S );
        std::cout << std::endl;
    }

    // Used to generate samples
    /*int K = 10;
    int C = 3;
    generate_bases( K, C );*/

    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
