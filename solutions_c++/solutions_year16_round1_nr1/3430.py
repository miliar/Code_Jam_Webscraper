////////////////////////////////////////////////////////////////////////////////
/**
 * @file last_word.cpp
 * @date 2016-04-15
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

////////////////////////////////////////////////////////////////////////////////

void solve_for_instance( int i )
{
    std::string input, output;
    
    std::cin >> input;

    for( char c: input )
    {

        if( c >= *output.begin() )
            output.insert( output.begin(), c );
        else
            output.insert( output.end(), c );
    }

    std::cout << "Case #" << i << ": " << output << std::endl;
}

////////////////////////////////////////////////////////////////////////////////

int main( int argc, char** argv, char** env )
{
    int n;

    std::cin >> n;
    for( int i=0; i < n; i++ )
    {
        solve_for_instance( i + 1 );
    }

    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
