//
//  main.cpp
//  testalgo
//
//  Created by William Hutama on 12/4/14.
//  Copyright (c) 2014 William Hutama. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    int n;
    const double R = 2.f;
    
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
     
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        
        double time = 0;
        double curr = R;
        
        while (true)
        {
            double wait_time = X / curr;
            double buy_time = C / curr;
            double rem_time = X / (curr + F);
            
            if (wait_time <= (buy_time + rem_time))
            {
                time += wait_time;
                break;
            }

            time += buy_time;
            curr += F;
        }
        
        printf("Case #%d: %f\n", i, time);
    }
    
    return 0;
}

