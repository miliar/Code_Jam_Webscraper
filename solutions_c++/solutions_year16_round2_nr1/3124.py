////////////////////////////////////////////////////////////////////////////////
/**
 * @file q1.cpp
 * @date 2016-04-30
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

#define CASE(X) std::cout << "Case #" << X << ": "
#define REMOVE(X) \
    assert( ( pos = find( input, X ) ) != -1 ); \
    input.erase( pos, 1 );

////////////////////////////////////////////////////////////////////////////////

int find( std::string& str, char c )
{
    for( int i=0; i < str.size(); i++ )
        if( str[i] == c )
            return i;

    return -1;
}

////////////////////////////////////////////////////////////////////////////////

void solve_for_instance( int instance )
{
    int numbers[] = {0,0,0,0,0,0,0,0,0,0};
    std::string input;
    int pos;

    std::cin >> input;
    while( find( input, 'Z' ) != -1 )
    {
        REMOVE('Z')
        REMOVE('E');
        REMOVE('R');
        REMOVE('O');
        numbers[0]++;
    }
    while( ( find( input, 'W') ) != -1 )
    {
        REMOVE('T');
        REMOVE('W');
        REMOVE('O');
        numbers[2]++;
    }
    while( ( find( input, 'F') != -1 ) && ( find( input, 'O') != -1 ) && ( find( input, 'U') != -1 ) && ( find( input, 'R') != -1 ) )
    {
        REMOVE('F');
        REMOVE('O');
        REMOVE('U');
        REMOVE('R');
        numbers[4]++;
    }
    while( find( input, 'T') != -1 && find( input, 'H') != -1 && find( input, 'R') != -1 && find( input, 'E') != -1 && find( input, 'E' ) != -1 )
    {
        REMOVE('T');
        REMOVE('H');
        REMOVE('R');
        REMOVE('E');
        REMOVE('E');
        numbers[3]++;
    }
    while( find( input, 'F') != -1 )
    {
        REMOVE('F')
        REMOVE('I');
        REMOVE('V');
        REMOVE('E');
        numbers[5]++;
    }
    while( find( input, 'X') != -1 )
    {
        REMOVE('S');
        REMOVE('I');
        REMOVE('X')
        numbers[6]++;
    }
    while( find( input, 'S') != -1 )
    {
        REMOVE('S');
        REMOVE('E');
        REMOVE('V');
        REMOVE('E');
        REMOVE('N');
        numbers[7]++;
    }
    while( find( input, 'T') != -1 )
    {
        REMOVE('E');
        REMOVE('I');
        REMOVE('G');
        REMOVE('H');
        REMOVE('T');
        numbers[8]++;
    }
    while( find( input, 'O') != -1 )
    {
        REMOVE('O');
        REMOVE('N');
        REMOVE('E');
        numbers[1]++;
    }
    while( find( input, 'N') != -1 )
    {
        REMOVE('N');
        REMOVE('I');
        REMOVE('N');
        REMOVE('E');
        numbers[9]++;
    }
    
    assert( input.size() == 0 );

    CASE(instance+1);
    for( int i=0; i < 10; i++ )
    {
        while( numbers[i] > 0 )
        {
            std::cout << i;
            numbers[i]--;
        }
    }
    std::cout << std::endl;
}

////////////////////////////////////////////////////////////////////////////////

int main()
{
    int n;

    std::cin >> n;
    for( int i=0; i < n; i++ )
    {
        solve_for_instance( i );
    }

    return EXIT_SUCCESS;
}

////////////////////////////////////////////////////////////////////////////////
