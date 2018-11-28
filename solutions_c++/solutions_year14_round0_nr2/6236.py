//
//  main.cpp
//  cj_B
//
//  Created by Daming Lu on 4/11/14.
//  Copyright (c) 2014 Daming Lu. All rights reserved.
//

#include <iostream>

using namespace std;

double getTimeForFarms(double C, double F, int numFarms) {
    double result = 0.0;
    for(int i=1; i<=numFarms; i++) {
        result += C/(2.0+(i-1)*F);
    }
    return result;
}

int main(int argc, const char * argv[])
{

    int cases = 0;
    cin >> cases;
    
    double C=0.0, F=0.0, X=0.0;
        // 500  ,    4,     2000
    for(int i=1; i<=cases; i++) {
        cin >> C >> F >> X;
        double init = X/2.0;
        int numFarms = 1;
        while(true) {
            double timeForFarms = getTimeForFarms(C, F,numFarms);
            double timeForTarget = X/(2.0+F*numFarms);
            double curTime = timeForFarms + timeForTarget;
            if (curTime > init) {
                cout<<"Case #"<<i<<": ";
                printf("%.7f\n", init);
                break;
            } else {
                init = curTime;
                numFarms++;
            }
        }
    }
    
    return 0;
}

