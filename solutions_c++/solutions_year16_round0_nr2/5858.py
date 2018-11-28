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

int flip(int num, int length, int pos)
{
    int result = 0;
    for(int i = 0; i < length; ++i)
    {
        if(i <= pos)
        {
            // i and (pos - i), length - i and length - (pos - i)
            if((num & (1 << (length - pos + i - 1))) == 0)
            {
                result += (1 << (length - i - 1));
            }
        }else{
            if(num & (1 << (length - i - 1)))
            {
                result += (1 << (length -i - 1));
            }
        }
    }
    return result;
}

int transferNum(string s)
{
    int length = s.size();
    int size = pow(2, length);
    vector<int> buffer(size, -1);
    queue<int> currentQ;
    currentQ.push(size - 1);
    buffer[size - 1] = 0;
    int tmp, flipped;
    while(!currentQ.empty())
    {
        tmp = currentQ.front();
        currentQ.pop();
        for(int i = 0; i < length; ++i)
        {
            flipped = flip(tmp, length, i);
            if(buffer[flipped] < 0)
            {
                buffer[flipped] = buffer[tmp] + 1;
                currentQ.push(flipped);
            }
        }
    }
    int givenPos = 0;
    for(int i = 0; i < length; ++i)
    {
        givenPos += s.at(i) == '+' ? (1 << (length - i - 1)) : 0;
    }
    return buffer[givenPos];
}

int main(){
    int TestNum;
    cin >> TestNum;
    int i = 0;
    int currentNum, currentResult;
    string s;
    while(i < TestNum)
    {
        cin >> s;
        currentResult = transferNum(s);
        cout<< "Case #" <<  i + 1 << ": "<< currentResult << endl;
        i++;
    }
}