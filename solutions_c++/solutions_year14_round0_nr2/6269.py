//
//  main.cpp
//  CodeJam1
//
//  Created by Aleem Haji on 2014-04-12.
//  Copyright (c) 2014 Inner Geek inc. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <vector>

int main(int argc, const char * argv[])
{
    int iters;
    std::cin >> iters;
    
    for ( int i = 0; i < iters; ++i ) {
        double c, f, x;
        std::cin >> c >> f >> x;
        
        double dCookies = 2.0;
        double totalTime = 0;
        
        while ( true ) {
            double timeToBuy = c / dCookies;
            double timeToGoal = x / dCookies;
            
            double timeToGoalIfBuy = timeToBuy + (x / (dCookies + f));
            
            if ( timeToGoalIfBuy <= timeToGoal ) {
                // buy
                dCookies += f;
                totalTime += timeToBuy;
            }
            else {
                totalTime += timeToGoal;
                break;
            }
        }
        
        std::cout << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(7) << totalTime << "\n";
    }
    
    return 0;
}