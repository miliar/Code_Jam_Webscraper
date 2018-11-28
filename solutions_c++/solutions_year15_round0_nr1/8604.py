// Gogo.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string delimiter = " ";

long
standing_ovation(string line_of_data){
    long result = 0;
    long shy_max = 0;
    long cum_stands = 0;
    string shy_levels = "";
    long tmp_rslt = 0;

    int index_space = line_of_data.find_first_of(delimiter);
    shy_max = atol(line_of_data.substr(0, index_space).c_str());
    shy_levels = line_of_data.substr(index_space+1, line_of_data.size());

    for(long i=0; i<=shy_max; i++){

        if(i>cum_stands) {
            tmp_rslt = i - cum_stands;
            result += tmp_rslt;
            cum_stands += tmp_rslt;
        }
        cum_stands += shy_levels.at(i) - '0'; 
    }


    return result;
}


int main()
{
    ifstream input_file ("input.txt");
    ofstream output_file ("output.txt");
    string line_read = "";

    if (input_file.is_open() &&  output_file.is_open())
    {

        getline (input_file, line_read);

        long nb_cases = atol(line_read.c_str());
        long idx_case = 1;

        while ( getline(input_file, line_read) && (idx_case <= nb_cases))
        {
            output_file << "Case #" ;
            output_file << idx_case;
            output_file <<  ": ";
            output_file << standing_ovation(line_read);
            output_file <<"\n";
            idx_case++;
            line_read.clear();
        }

        input_file.close();
        output_file.close();
    }

    else cout << "Unable to open a file"; 

	return 0;
}

