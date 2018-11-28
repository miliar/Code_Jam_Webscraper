//
//  main.cpp
//  Cookie_Clicker_Alpha
//
//  Created by CuiLei on 4/12/14.
//  Copyright (c) 2014 wolfshow. All rights reserved.
//

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    int T;
    cin >> T;
    
    for(int ca = 1; ca <=T; ca++)
    {
        double C, F, X, time;
        double cur = 2;
        time = 0;
        cin >> C >> F >> X;
        
        while(true)
        {
            double tmp1 = X / cur;
            
            double tmp2 = C / cur;
            
            double tmp3 = X / (cur + F);
            
            if(tmp2 + tmp3 < tmp1)
            {
                time += tmp2;
                //time += tmp3;
                cur += F;
            }
            else
            {
                time += tmp1;
                break;
            }
        }
        
        cout << "Case #" << ca << ": " << fixed << setprecision(7) << time << endl;

        
    }
    
    //std::cout << "Hello, World!\n";
    return 0;
}

