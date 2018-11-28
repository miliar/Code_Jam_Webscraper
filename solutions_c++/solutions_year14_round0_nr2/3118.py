//
//  main.cpp
//  CodeJam_QR_B
//
//  Created by Dan on 12/4/14.
//  Copyright (c) 2014年 Dan. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[])
{
    freopen("/Users/danmac/Documents/Works/Projects/CodeJam_QR_B/CodeJam_QR_B/in.txt", "r", stdin);
    freopen("/Users/danmac/Documents/Works/Projects/CodeJam_QR_B/CodeJam_QR_B/out.txt", "w", stdout);
    
    int numOfCase;
    
    cin >> numOfCase;
    
    for (int i=0; i<numOfCase; i++) {
        double factor = 2;
        double requireTime = 0;
        
        long double C, F, X;
        cin >> C >> F >> X;
        
        while ((X/factor) - (X/(factor+F)) >= (C/factor)) {
            requireTime += C / factor;
            factor += F;
        };
        
        requireTime += X / factor;
        
        cout << "Case #" << (i+1) << ": " << fixed << setprecision(7) << requireTime << '\n';
    }
    
    return 0;
}

