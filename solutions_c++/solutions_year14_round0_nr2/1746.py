//
//  main.cpp
//  Google2
//
//  Created by happy_1113xie on 14-4-12.
//  Copyright (c) 2014年 happy_1113xie. All rights reserved.
//

#include <fstream>
#include <iomanip>
using namespace  std;

int main(){
    ifstream f1;
    f1.open("/Users/happy_1113xie/Desktop/B-large.in");
    ofstream f2;
    f2.open("/Users/happy_1113xie/Desktop/B.out");
    
    int T;
    f1 >> T;
    f2 << fixed;
    for (int i = 1; i <= T; ++i)
    {
        double F, deltaF, C, X;
        f1 >> C >> deltaF >> X;
        
        double t = 0, checkt;
        F = 2;
        while (true){
            checkt = (F + deltaF) * C / (F* deltaF);
            if (checkt * F < X){
                t += C / F;
                F += deltaF;
            }
            else
            {
                t += X / F;
                break;
            }
        }
        
        f2 << "Case #" << i << ": ";
        f2 << setprecision(7) << t << endl;
    }
    
    f1.close();
    f2.close();
    return 0;
}
