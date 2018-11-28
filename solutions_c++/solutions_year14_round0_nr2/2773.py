//
//  main.cpp
//  CookieClicker
//
//  Created by lmotorin on 4/12/14.
//  Copyright (c) 2014 Lior. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[])
{

    size_t tc = 0 , tc_i = 0;
    cin >> tc;
    
    for (tc_i=1;tc_i<=tc;++tc_i)
    {
        
        double C = 0 , F = 0 , X = 0;
        cin >> C >> F >> X;
        double target_rate = ((X-C)*F)/C;
        
        // calculate time until we exceed target rate
        double rate = 2.0;
        double time = 0;
        while (rate < target_rate)
        {
            time += C/rate;
            rate += F;
        }
        
        time += X/rate;
        
        printf("Case #%d: %.7f\n",(int)tc_i,time);
        
        
    }
    
    
    return 0;
}

