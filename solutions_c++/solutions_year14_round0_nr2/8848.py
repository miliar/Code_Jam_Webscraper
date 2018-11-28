#pragma once

#include <exception>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class CookieClicker
{
public:
    CookieClicker();
    CookieClicker(int, ifstream&);
    ~CookieClicker();
    
    double fastest_time_to_win(double C, double F, double X);
    void output_to_file(ofstream&, int, double);
    void test(int tc, double fastest_time);

private:
    vector<double> test_results;
};

