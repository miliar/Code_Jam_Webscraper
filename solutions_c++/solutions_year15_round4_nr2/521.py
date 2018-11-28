//
//  main.cpp
//  B
//
//  Created by Nikifor Zhao on 15/5/30.
//  Copyright (c) 2015年 Nikifor Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("output.txt");

double eps = 1e-6;
int main(int argc, const char * argv[]) {
    int T;
    fin >> T;
    for (int ti = 1; ti <= T; ++ ti) {
        //cout << ti << endl;
        double ans = 0;
        int bad = 0;
        int n;
        double v, x;
        fin >> n >> v >> x;
        if (n == 1) {
            double c, r;
            fin >> r >> c;
            if (fabs(x - c) < eps) {
                ans = v / r;
            } else {
                bad = 1;
            }
        } else {
            double c1, r1, c2, r2;
            fin >> r1 >> c1 >> r2 >> c2;
            if (fabs(c1 - x) < eps && fabs(c2 - x) < eps) {
                ans = v / (r1 + r2);
            } else if (fabs(c1 - x) < eps) {
                ans = v / r1;
            } else if (fabs(c2 - x) < eps) {
                ans = v / r2;
            } else if (c1 > x && c2 > x) {
                bad = 1;
            } else if (c1 < x && c2 < x) {
                bad = 1;
            } else {
                double d1 = fabs(c1 - x), d2 = fabs(c2 - x);
                double t1 = v / r1 * d2 / (d1 + d2), t2 = v * d1 / (d1 + d2) / r2;
                ans = max(t1, t2);
            }
        }

        if (bad) fout << "Case #" << ti << ": " << "IMPOSSIBLE"  <<endl;
        else fout << fixed << setprecision(6) << "Case #" << ti << ": " << ans  <<endl;
        
    }
    return 0;
}
