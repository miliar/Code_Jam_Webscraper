//
//  main.cpp
//  DeceitfulWar
//
//  Created by lmotorin on 4/12/14.
//  Copyright (c) 2014 Lior. All rights reserved.
//

#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <iostream>
using namespace std;

#define ALMOST_SAME 0.0000001

int deterWarWins(const vector<double>& naomi_w,const vector<double>& ken_w)
{
    // deter naomi wins by War optimally.
    int naomi_biggest = (int) naomi_w.size()-1;
    int ken_biggest = (int) ken_w.size()-1;
    int ken_smallest = 0;
    int war_wins = 0;
    while (naomi_biggest >= 0)
    {
        if (naomi_w[naomi_biggest] > ken_w[ken_biggest])
        {
            war_wins++;
            naomi_biggest--;
            ken_smallest++;
        }
        else
        {
            naomi_biggest--;
            ken_biggest--;
        }
    }
    return war_wins;
}

bool isBiggerThan(const vector<double>& naomi_w,const vector<double>& ken_w)
{
    int i = 0;
    int len = (int) naomi_w.size();
    
    for (i=0;i<len;++i)
    {
        if (naomi_w[i]<=ken_w[i])
            return false;
    }
    return true;
}

int deterDecefulWarWins(vector<double> naomi_w,vector<double> ken_w)
{

    
    while (!isBiggerThan(naomi_w, ken_w))
    {
        naomi_w.erase(naomi_w.begin());
        ken_w.erase(ken_w.end()-1);
    }
    
    return (int) naomi_w.size();
}


int main(int argc, const char * argv[])
{

    size_t tc = 0 , tc_i = 0;
    cin >> tc;
    
    for (tc_i = 1 ; tc_i <= tc ; ++tc_i)
    {
        vector<double> naomi_w;
        vector<double> ken_w;
        double temp;
        int len = 0 , i=0;
        cin >> len;
        
        for (i=0;i<len;++i)
        {
            cin >> temp;
            naomi_w.push_back(temp);
        }

        for (i=0;i<len;++i)
        {
            cin >> temp;
            ken_w.push_back(temp);
        }
        
        // sort both list
        std::sort(naomi_w.begin(),naomi_w.end());
        std::sort(ken_w.begin(),ken_w.end());

        cout << "Case #"<< tc_i << ": " << deterDecefulWarWins(naomi_w,ken_w) << " " << deterWarWins(naomi_w,ken_w) << endl;
    }
    return 0;
}

