
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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

int emurate_d( std::vector<double> &n, std::vector<double>& k, int &num )
{
    std::vector<double> ken_sorted = k;
    std::vector<double> naomi_sorted = n;
    int win_num = num;

    std::sort( ken_sorted.begin(), ken_sorted.end(), std::greater<double>()  );
    std::sort( naomi_sorted.begin(), naomi_sorted.end(), std::greater<double>()  );

    for( int i = 0, n_i = 0; i < num; i++ ) {
        if( ken_sorted[i] > naomi_sorted[n_i] ) {
            win_num--;
        }
        else {
            n_i++;
        }
    }
    return win_num;
}

int emurate( std::vector<double> &n, std::vector<double>& k, int &num )
{
    std::vector<double> ken_sorted = k;
    std::vector<double> naomi_sorted = n;
    int win_num = 0;

    std::sort( ken_sorted.begin(), ken_sorted.end(), std::greater<double>() );
    std::sort( naomi_sorted.begin(), naomi_sorted.end(), std::greater<double>() );

    for( int i = 0, k_i = 0; i < num; i++ ) {
        if( naomi_sorted[i] > ken_sorted[k_i] ) {
            //ken pop from bottom
            win_num++;
        }
        else {
            k_i++;
        }
    }
    return win_num;
}

int main()
{
    std::vector<int> tmp;
    int case_num = 0;

    tmp = read_line();
    case_num = tmp[0];

    for( int i = 0; i < case_num; i++ )//SET Any
    {
        std::vector<double> naomi;
        std::vector<double> ken;
        int number;
        int d_w = 0;
        int w_w = 0;


        tmp = read_line();
        number = tmp[0];

        naomi = read_line_d();
        ken = read_line_d();

        d_w = emurate_d( naomi, ken, number );
        w_w = emurate( naomi, ken, number );

        printf( "%s%d: %d %d\n", CASE, i+1, d_w, w_w );
    }
}

