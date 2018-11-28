//
//  main.cpp
//  Cookie
//
//  Created by Tingting Cao on 12/04/2014.
//  Copyright (c) 2014 Tingting Cao. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main(int argc, const char * argv[])
{
    int case_num;
    cin>>case_num;
    
    
    for(int c=0;c<case_num;c++)
    {
        //each case
        long double farm_price,rate_gain,final_goal;

        cin>>farm_price>>rate_gain>>final_goal;
//        cout<<farm_price<<" "<<rate_gain<<" "<<final_goal;
        
        long double totalTime_needed=0;
        
        long double cur_rate=2.0;
        
        long double timeNeeded_without_buy_farm=final_goal/cur_rate;
        long double timeNeeded_with_buy_farm=farm_price/cur_rate+final_goal/(cur_rate+rate_gain);
        
        while(timeNeeded_with_buy_farm<timeNeeded_without_buy_farm)
        {
            totalTime_needed+=farm_price/cur_rate;
            
            cur_rate+=rate_gain;
            
            timeNeeded_without_buy_farm=final_goal/cur_rate;
            timeNeeded_with_buy_farm=farm_price/cur_rate+final_goal/(cur_rate+rate_gain);
        }
        
        //when it's out of loop,means no need to buy a farm now
        
        totalTime_needed+=final_goal/cur_rate;
        
        //result
        cout<<"Case #"<<c+1<<": ";
        printf("%.7Lf\n",totalTime_needed);
    }
    
    return 0;
}

