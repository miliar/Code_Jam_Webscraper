// =========================================================
//
//       Filename:  Cookie Clicker Alpha
//
//    Description:
//
//        Version:  1.0
//        Created:  04/11/2014
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  CGG
//      Copyright:  Copyright (c) 04/11/2014
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>

using namespace std;

double solve(double C, double F, double X)
{
    double time = 0.0;
    double p = 2.0;

    while (p < F*(X/C-1))
    {
        time += C/p;
        p += F;
    }
    time += X/p;
    return time;
}

int main()
{
    // load input
    unsigned int case_no;
    cin >> case_no;

    for (unsigned int t = 0; t < case_no; ++t)
    {
        double C, F, X;
        cin >> C >> F >> X;

        // sove problem
        double result;
        result = solve(C, F, X);

        std::cout.precision(10);
        cout << "Case #" << t+1 << ": ";
        cout << result << endl;
    }

    return 0;

}
