//
//  main.cpp
//  Verizon
//
//  Created by bcstyle on 14-2-26.
//  Copyright (c) 2014年 bcstyle. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <iomanip>      // std::setprecision
using namespace std;

int main()
{
    int numCases;
    scanf("%d\n", &numCases);
    for(int curCase = 1; curCase <= numCases; curCase++) {
        double C, F, X;
        cin >> C >> F >> X;
        if(X <= C) {
            cout << "Case #" << curCase << ": " << setprecision(7) << X/2.0 << endl;
            continue;
        }
        
        double curSpeed = 2.0;
        double curCookies = C;
        double timeused = C/2.0;
        while(true) {
            double curTimeLeft = (X - curCookies) / curSpeed;
            if(curCookies >= C && (X - curCookies + C)/(curSpeed + F) <= curTimeLeft)
            {
                curCookies = C;
                curSpeed += F;
                timeused += C/curSpeed;
            }
            else {
                timeused += curTimeLeft;
                break;
            }
        }
        cout << "Case #" << curCase << ": " << setprecision(7) << timeused << endl;
    }
}

