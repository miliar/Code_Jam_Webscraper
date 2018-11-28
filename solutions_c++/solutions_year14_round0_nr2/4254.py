//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Kotsur on 12.04.14.
//  Copyright (c) 2014 Dmytro Kotsur. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

ifstream in("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Cookie Clicker Alpha/google_test.txt");
ofstream out("/Users/userMac/Projects/Contests/Google Code Jam 2014/Qualification_Round/Cookie Clicker Alpha/out.txt");

int T;
double C, F, X;

void solve(double c, double f, double x);

int main(int argc, const char * argv[])
{
    in >> T;
    for (int t = 1; t <= T; ++t) {
        in >> C >> F >> X;
        out << "Case #" << t << ": ";
        solve(C, F, X);
    }
    return 0;
}

void solve(double c, double f, double x) {
    
    double r = 2;
    double sum = 0.0;
    while (sum + x / r > sum + c / r + x / (f + r)) {
        sum += c / r;
        r += f;
    }
    sum += x / r;
    out << fixed << setprecision(7) << sum << endl;
}

