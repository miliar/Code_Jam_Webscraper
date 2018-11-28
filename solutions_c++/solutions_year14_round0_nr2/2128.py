
#include <iostream>
#include <string>
#include <vector>

#include <stdio.h>
#include <stdlib.h>

char CASE[] = "CASE #";

std::vector<int> read_line()
{
    int index = 0;
    int prev  = 0;

    std::string line;
    std::vector<int> values;
    std::getline( std::cin, line );

    while( std::string::npos != index )
    {
        int size = 0;
        index = line.find( " ", prev );
        if( std::string::npos != index ) {
            size = index - prev;
        }
        else {
            size = index;
        }
        std::string tmp_string = line.substr( prev, size );
        values.push_back( atoi( tmp_string.c_str() ) );
        if( std::string::npos == index )
        {
            break;
        }
        prev = index+1;
    }

    return values;
}

std::vector<double> read_line_d()
{
    int index = 0;
    int prev  = 0;

    std::string line;
    std::vector<double> values;
    std::getline( std::cin, line );

    while( std::string::npos != index )
    {
        int size = 0;
        index = line.find( " ", prev );
        if( std::string::npos != index ) {
            size = index - prev;
        }
        else {
            size = index;
        }
        std::string tmp_string = line.substr( prev, size );
        values.push_back( atof( tmp_string.c_str() ) );
        if( std::string::npos == index )
        {
            break;
        }
        prev = index+1;
    }

    return values;
}

double emurate( double &c, double &f, double &x )
{
    int idx = 0;
    double inc = 2.0;
    double time = 0.0;

    for( idx = 0; ; idx++ ){
        time += c / inc;
        if( ( x - c ) > inc * ( c / f ) ){
            inc += f;
        }
        else {
            time += ( x - c ) / inc;
            break;
        }
    }
    return time;
}

int main()
{
    std::vector<int> tmp;
    int case_num = 0;

    tmp = read_line();
    case_num = tmp[0];

    for( int i = 0; i < case_num; i++ )//SET Any
    {
        std::vector<double> status;
        double time;

        status = read_line_d();
        time = emurate( status[0], status[1], status[2] );
        printf( "%s%d: %1.7f\n", CASE, i+1, time );
    }
}

