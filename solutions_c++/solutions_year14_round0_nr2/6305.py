//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Zhe Zhang on 4/11/14.
//  Copyright (c) 2014 Zhe Zhang. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

double init_speed = 2.0;

void calc_min_time (double C, double F, double X, int test_case_index){
    
    vector<double> intermediate_time;
    double min_total_time = X/init_speed;
    //intermediate_time.push_back(total_time);
    int index = 0;
    
    double current_rate;
    double buy_farm_time;
    double new_total_time;
    
    while (1) {
        current_rate = init_speed + index * F;
        buy_farm_time = C/current_rate;
        if(index == 0){
            intermediate_time.push_back(buy_farm_time);
        }
        else{
            intermediate_time.push_back(buy_farm_time + intermediate_time[index-1]);
        }
        
        new_total_time = intermediate_time[index] + X/(current_rate+F);
        if (new_total_time > min_total_time) {
            break;
        }
        else{
            min_total_time = new_total_time;
        }
        index ++;
    }
    
    // print the output
    cout.precision(7);
    cout << "Case #" << test_case_index << ": " << fixed << min_total_time << endl;
    
    return;
    
}

int main(int argc, const char * argv[])
{
    
    // read the input file
    string line;
    ifstream input_file("B-large.in.txt");
    
    int test_case_num = 0;
    
    // first get the number of test cases
    getline(input_file, line);
    stringstream sstream(line);
    sstream >> test_case_num;
    
    // read the input parameters for each test case
    
    for (int i = 0; i < test_case_num; i++) {
        getline(input_file, line);
        stringstream c_f_x(line);
        double C_F_X[3];
        double read_value;
        int index = 0;
        while (c_f_x >> read_value) {
            C_F_X[index] = read_value;
            index ++;
        }
        calc_min_time(C_F_X[0], C_F_X[1], C_F_X[2], i+1);
    }

    return 0;
}

