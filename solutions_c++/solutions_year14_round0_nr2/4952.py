//
//  main.cpp
//  2
//
//  Created by Nikifor Zhao on 14-4-12.
//  Copyright (c) 2014年 Han Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("out.txt");

int main(int argc, const char * argv[])
{
    double c, f, x;
    int t;
    fin >> t;
    for (int ni = 0; ni < t ; ni ++){
        fin >> c >> f >> x;
        double nowt = 0, nowc = 0, nowv = 2;
        while (1){
            double t1 = (x - nowc) / nowv;
            double t2 = (c - nowc) / nowv + x / (nowv + f);
            if (t1 < t2) {
                nowt += t1;
                break;
            }else{
                nowt += (c - nowc) / nowv;
                nowv += f;
            }
        }
        fout << "Case #" << ni+1 << ": ";
        fout << setiosflags(ios::fixed) << setprecision(7) << nowt << endl;
    }
    return 0;
}

