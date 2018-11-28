////////////////////////////////////////////////////////////////////////////////
/**
 * @file q1.cpp
 * @date 2016-05-08
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

#include <bits/stdc++.h>

////////////////////////////////////////////////////////////////////////////////

#define CASE(X) std::cout << "Case #" << X+1 << ": "

////////////////////////////////////////////////////////////////////////////////

void solve_for_instance( int instance, int t )
{
    std::priority_queue< std::pair< int, char > > pq;
    std::pair< int, char > first, second;
    int total = 0;

    for( int i=0; i < t; i++ )
    {
        int n;
        std::cin >> n;
        total += n;
        pq.push( std::pair< int, char >( n, 'A'+i ) );
    }

    while( !pq.empty() )
    {
        total--;
        first = pq.top(); pq.pop();
        first.first--;
        if( first.first > 0 ) pq.emplace( first );
        if( !pq.empty() )
        {
            second = pq.top(); pq.pop();
        }
        else
            second = std::pair< int, char >(0, 0);

        if( (float)second.first/(float)total > 0.5 )
        {
            total--;
            second.first--;

            std::cout << first.second << second.second << " ";
        }
        else
        {
            std::cout << first.second << " ";
        }

        if( second.first > 0 && second.second != 0 )
            pq.emplace( second );
    }

}

////////////////////////////////////////////////////////////////////////////////

int main()
{
    int n, t;

    std::cin >> n;
    for( int i=0; i < n; i++ )
    {
        std::cin >> t;
        CASE( i );
        solve_for_instance( i, t );
        std::cout << std::endl;
    }

    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
