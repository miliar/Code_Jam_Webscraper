//
//  main.cpp
//  cookieclicker
//
//  Created by Lydia Yang on 14-4-12.
//  Copyright (c) 2014年 杨荔雅5110309443. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream in("/Users/apple/Desktop/in.txt");
    ofstream out("/Users/apple/Desktop/out.txt");
    int T;
    in>>T;
    double C;
    double F;
    double X;
    double s;
    double t;
    for (int i = 0; i<T; i++) {
        in >> C;
        in >> F;
        in >> X;
        s = 2.0000000;
        t = 0.0000000;
        while (1) {
            if ((X/s)<((C/s)+(X/(F+s)))) {
                t += X/s;
                break;
            }
            else {
                t += C/s;
                s += F;
            }
        }
        out << "Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<t<<endl;
    }
    
    in.close();
    out.close();
    return 0;
}

