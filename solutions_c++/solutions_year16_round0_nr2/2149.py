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
#include <string>
#include <vector>

////////////////////////////////////////////////////////////////////////////////

int greedy_solver( const std::string& S )
{
    std::vector< bool > s;
    int n_times = 0;

    s.reserve( S.size() );
    for( auto& str: S )
        s.push_back( str == '+' );

    for( auto i=s.rbegin(); i != s.rend(); i++ )
    {
        if( !*i && !(n_times % 2) ) n_times++;
        if(  *i &&  (n_times % 2) ) n_times++;
    }

    return n_times;
}

////////////////////////////////////////////////////////////////////////////////

int counting_solver( const std::string& S )
{
    std::vector< bool > s;
    int n_times = 0;

    s.reserve( S.size() );
    for( auto& str: S )
        s.push_back( str == '+' );

    for( int i=s.size()-1; i >= 0; i-- )
    {
        while( i >=0 && !s[i] )
            i--;
        
        if( i < 0 ) n_times++;
        else if( i < (int)s.size()-1 && !s[i+1] ) n_times += 2;
    }

    return n_times;
}

////////////////////////////////////////////////////////////////////////////////

int main( int argc, char** argv )
{
    int T;
    std::string S;

    std::cin >> T; T++;
    for( int i=1; i < T; i++ )
    {
        std::cin >> S;

        //std::cout << "Case #" << i << ": " << greedy_solver(S) << std::endl;
        std::cout << "Case #" << i << ": " << counting_solver(S) << std::endl;
    }

    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
