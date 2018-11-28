//
//  main.cpp
//  Leetcode
//
//  Created by Shuang Guan on 3/6/16.
//  Copyright (c) 2016 Shuang Guan. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <queue>
#include "math.h"
#include <string>

using namespace std;

bool isPossible(int K, int C, int S, vector<unsigned long long>& pos)
{
    if(C * S < K)
        return false;
    unsigned long long tmp = 0;
    
    if(K == S)
    {
        for(int i = 0; i < K; ++i)
        {
            pos.push_back(i + 1);
        }
        return true;
    }
    int i = 0;
    while(i < K)
    {
        tmp = 0;
        for(int j = 0; j < C; ++j)
        {
            tmp += (i < K ? i : (K - 1)) * pow(K, C - j - 1);
            ++i;
        }
        pos.push_back(tmp + 1);
    }
    return true;
}

int main()
{
    int numTest;
    cin >> numTest;
    int times = 0;
    while(times < numTest)
    {
        int K, C, S;
        cin >> K >> C >> S;
        vector<unsigned long long> pos;
        cout<<"Case #" << times + 1 << ":";
        if(isPossible(K, C, S, pos))
        {
            for(int j = 0; j < pos.size(); ++j)
            {
                cout<<" "<<pos[j];
            }
            cout<<endl;
        }else {
            cout<<" IMPOSSIBLE"<<endl;
        }
        times++;
    }
}

