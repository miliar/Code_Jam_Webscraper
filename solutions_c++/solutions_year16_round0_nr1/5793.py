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
#include <fstream>

using namespace std;

int numTurn(int n)
{
    vector<int> nums(10, 0);
    int multiplier = 1;
    int current;
    bool full = false;
    if(n == 0)
        return 0;
    while(!full){
        current = n * multiplier;
        while(current >= 10){
            nums[current%10] = 1;
            current /= 10;
        }
        nums[current] = 1;
        full = true;
        for(int i = 0; i < 10; ++i)
        {
            if(nums[i] == 0)
            {
                full = false;
                break;
            }
        }
        if(full)
            return n * multiplier;
        multiplier++;
    }
    return 0;
}

int main(){
    int TestNum;
    cin >> TestNum;
    int i = 0;
    int currentNum, currentResult;
    while(i < TestNum)
    {
        cin >> currentNum;
        currentResult = numTurn(currentNum);
        if(currentResult == 0)
        {
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        } else {
            cout << "Case #" << i+1 << ": " << currentResult <<endl;
        }
        i++;
    }
}