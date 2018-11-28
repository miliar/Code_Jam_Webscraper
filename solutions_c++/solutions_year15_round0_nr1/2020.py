//
//  main.cpp
//  StandingOvation
//
//  Created by Bai, Shi on 4/10/15.
//  Copyright (c) 2015 Bai, Shi. All rights reserved.
//

#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
    int num_cases = 0;
    char s_array[1001];
    string in_file_name;
    string out_file_name;
    cout << "Please enter input file name:";
    cin >> in_file_name;
    cout << "Please enter ouput file name:";
    cin >> out_file_name;
    std::fstream infile;
    infile.open(in_file_name.c_str());
    bool is_in_open = infile.is_open();
    std::fstream outfile(out_file_name.c_str(), ios::out);
    bool is_out_open = outfile.is_open();
    std::string line;
    std::getline(infile, line);
    std::istringstream iss(line);
    iss >> num_cases;

    for (int case_id = 1; case_id <= num_cases; case_id++)
    {
        std::getline(infile, line);
        std::istringstream iss_curr(line);
        int s_max = 0;
        iss_curr >> s_max;
        iss_curr >> s_array;
        int people_need = 0;
        int people_curr = 0;
        for (int shy_level = 0; shy_level <= s_max; shy_level++)
        {
            int num_people_curr_level = (int)s_array[shy_level] - (int)'0';
            int people_need_curr = 0;
            if (num_people_curr_level > 0 && shy_level - people_curr > 0)
            {
                people_need_curr = shy_level - people_curr;
            }
            people_need += people_need_curr;
            people_curr += num_people_curr_level + people_need_curr;
        }
        printf("Case #%d: %d\n", case_id, people_need);
        outfile << "Case #" << case_id << ": " << people_need << endl;
    }
    outfile.close();
    return 0;
}