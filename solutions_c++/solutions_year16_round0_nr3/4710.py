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

bool isPrime(unsigned long long  n, unsigned long long & divider)
{
    if( n <= 1)
    {
        divider = 1;
        return false;
    }
    else if( n <= 3)
        return true;
    else if (n % 2 == 0 || n % 3 == 0)
    {
        divider = (n %2 == 0 ? 2 : 3);
        return false;
    }
    int i = 5;
    while(i * i <= n)
    {
        if( n % i == 0 || n % (i + 2) == 0)
        {
            divider = ( n % i == 0 ? i : i + 2);
            return false;
        }
        i = i + 6;
    }
    return true;
}

unsigned long long toBaseN(string s, int base)
{
    unsigned long long result = 0;
    for(int i = 0; i < s.size(); ++i)
    {
        result = result * base + (s.at(i) - '0');
    }
    return result;
}

vector<string> findJam(int length, int J, vector<vector<unsigned long long>> & factors)
{
    int nums = 0;
    vector<string> result;
    string s(length, '0');
    s.at(0) = '1';
    s.at(length - 1) = '1';
    int size = pow(2, length - 2);
    for(int i = 0; i < size; ++i)
    {
        int tmp = i, pos = 1;
        while(tmp >= 2)
        {
            s.at(pos++) = tmp % 2 == 0? '0' : '1';
            tmp /= 2;
        }
        s.at(pos++) = tmp %2 == 0? '0' : '1';
        tmp /= 2;
        bool isJam = true;
        for(int j = 2; j <= 10; j++)
        {
            unsigned long long current= toBaseN(s, j);
            if(isPrime(current, factors[nums][j-2]))
            {
                isJam = false;
                break;
            }
        }
        if(isJam)
        {
            string tmp(s);
            result.push_back(tmp);
            ++nums;
        }
        if(nums == J)
            break;
    }
    return result;
}

int main()
{
    int numTest;
    cin >> numTest;
    int times = 0;
    while(times < numTest)
    {
        int N, J;
        cin >> N  >> J;
        vector<unsigned long long> rows(9, 0);
        vector<vector<unsigned long long>> factors(J, rows);
        vector<string> result;
        result = findJam(N, J, factors);
        cout<< "Case #" << times + 1 << ":"<<endl;
        for(int i = 0; i < J; ++i)
        {
            cout<< result[i] <<" ";
            for(int m = 0; m < 9; ++m)
                cout<< factors[i][m]<< " ";
            cout<<endl;
        }
        times++;
    }
}

