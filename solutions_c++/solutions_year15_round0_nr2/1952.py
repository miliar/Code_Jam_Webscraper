//
//  main.cpp
//  InfiniteHouseOfPancakes
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
#include <algorithm>
#include <queue>

using namespace std;

bool my_compare(int a, int b) { return a > b; }

int main()
{
    int num_cases = 0;
    string in_file_name;
    string out_file_name;
    cout << "Please enter input file name:";
    cin >> in_file_name;
    cout << "Please enter ouput file name:";
    cin >> out_file_name;
    std::fstream infile(in_file_name.c_str(), ios::in);
    std::fstream outfile(out_file_name.c_str(), ios::out);
    std::string line;
    std::getline(infile, line);
    std::istringstream iss(line);
    iss >> num_cases;

    for (int case_id = 1; case_id <= num_cases; case_id++)
    {
        std::getline(infile, line);
        std::istringstream iss_d(line);
        int d = 0;
        iss_d >> d;
        
        vector<int> pancakes_array;
        std::getline(infile, line);
        cout << "Current test case: " << line << endl;
        std::istringstream iss_p(line);
        int total_pancakes = 0;

        int original_time = 0;
        for (int i = 0; i < d; i++)
        {
            int curr = 0;
            iss_p >> curr;
            total_pancakes += curr;
            original_time = max(curr, original_time);
            pancakes_array.push_back(curr);
        }
        int optimal_time = original_time;
        for (int i = original_time - 1; i >= 1; i--)
        {
            int special_time = 0;
            priority_queue<int> pancakes;
            for (int j = 0; j < pancakes_array.size(); j++)
            {
                pancakes.push(pancakes_array[j]);
            }
            while (pancakes.top() > i)
            {
                int pancake_moved = pancakes.top() - i;
                pancakes.pop();
                special_time++;
                pancakes.push(pancake_moved);
            }
            
            optimal_time = min(optimal_time, special_time + i);
        }


        printf("Case #%d: %d\n", case_id, optimal_time);
        outfile << "Case #" << case_id << ": " << optimal_time << endl;
    }
    outfile.close();
    return 0;
}