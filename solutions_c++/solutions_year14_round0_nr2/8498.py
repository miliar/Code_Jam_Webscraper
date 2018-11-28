/* 
 * File:   main.cpp
 * Author: Peter
 *
 * Created on 12 april 2014, 13:01
 */

#include <cstdlib>
#include <iostream>
#include <iomanip>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int number=0;
    std::cin >> number;
    cout.precision(7);
    for(int i=0; i<number; i++)
    {
        double result=0.0;
        double production=2.0;
        double c;
        double f;
        double x;
        std::cin >> c >> f >> x;
        while(x/production > (x/(production+f))+(c/production))
        {
            result += c/production;
            production += f;
        }
        result += x/production;       
        std::cout << "Case #" << i+1  << ": " << fixed << result << endl;
    }
    return 0;
}

