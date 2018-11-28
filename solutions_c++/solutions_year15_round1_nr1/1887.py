//
//  main.cpp
//  MushroomMonster
//
//  Created by Bai, Shi on 4/17/15.
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
        std::istringstream iss_N(line);
        int N = 0;
        iss_N >> N;
        vector<int> mushrooms(N);
        std::getline(infile, line);
        std::istringstream iss_mushroom(line);
        for (int i = 0; i < N; i++)
        {
            iss_mushroom >> mushrooms[i];
            cout << "Current mushroom : " << mushrooms[i] << endl;
        }

        int num_method1 = 0;
        int num_method2 = 0;

        for (int i = 1; i < N; i++)
        {
            if (mushrooms[i] < mushrooms[i - 1])
            {
                num_method1 += mushrooms[i - 1] - mushrooms[i];
            }
        }

        int max_diff = 0;
        for (int i = 1; i < N; i++)
        {
            max_diff = max(mushrooms[i - 1] - mushrooms[i], max_diff);
        }
        for (int i = 0; i < N - 1; i++)
        {
            num_method2 += min(max_diff, mushrooms[i]);
        }

        printf("Case #%d: %d %d\n", case_id, num_method1, num_method2);
        outfile << "Case #" << case_id << ": " << num_method1 << " " << num_method2 << endl;
    }
    outfile.close();
    return 0;
}
