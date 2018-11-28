//
//  main.cpp
//  GoogleJam
//
//  Created by Isira Samarasekera on 3/13/16.
//  Copyright (c) 2016 Isira Samarasekera. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <numeric>
#include <math.h>
#include <iomanip>
#include <algorithm>
using namespace std;


vector<string> getpPlan(vector<int> group)
{
    // total Number of people
    vector<string> plan;
    vector<pair<int,int>> results;
    int sum = std::accumulate(group.begin(), group.end(), 0);
    int count = 0;
    while(count < sum)
    {
        vector<int>::iterator maximum = std::max_element(group.begin(), group.end());
        int maxAt = std::distance(group.begin(), maximum);
        group[maxAt] -= 1;
        count++;
        vector<int>::iterator secondMax = std::max_element(group.begin(), group.end());
        int secondMaxAt = std::distance(group.begin(), secondMax);
        group[secondMaxAt] -= 1;
        count++;
        // if removing 2nd one majority changes
        vector<int>::iterator thirdMax = std::max_element(group.begin(), group.end());
        if(2*(*thirdMax) >(sum-count))
        {
            group[secondMaxAt] += 1;
            count--;
            results.emplace_back(maxAt, -1);
        }
        else
        {
            results.emplace_back(maxAt, secondMaxAt);
        }
    }
    
    for(int i=0; i < results.size(); i++)
    {
        string s;
        s += results[i].first +65;
        if(results[i].second != -1)
        {
            s += results[i].second +65;
        }
        plan.push_back(s);
    }
    return plan;
}




int main(int argc, const char * argv[]) {
    // insert code here..
    ifstream in("/Users/isira/Documents/CodeJam/2016C/A-large.in");
    ofstream out("/Users/isira/Documents/CodeJam/2016C/A-large.out");
    string line;
    getline(in, line);
    
    int nTests = 0;
    nTests = stoi(line);
    
    for(int i= 0; i < nTests; i++)
    {
        getline(in, line);
        int groups = stoi(line);
        
        getline(in, line);
        
        stringstream ss(line);
        vector<int> groupVals;
        for(int j=0; j< groups; j++)
        {
            string temp;
            getline(ss, temp, ' ');
            
            groupVals.emplace_back(stoi(temp));
        }
        
        vector<string> plan = getpPlan(groupVals);
        out<<"Case #"<<i+1 <<": ";
        for(int j=0; j< plan.size(); j++)
        {
            out<<plan[j]<<' ';
        }
        out<<endl;
    }
    in.close();
    out.close();
    
    return 0;
}
