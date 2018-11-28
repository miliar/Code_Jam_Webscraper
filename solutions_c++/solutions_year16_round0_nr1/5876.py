//
//  main.cpp
//  CountingSheep
//
//  Created by YOUQingfei on 4/9/16.
//  Copyright © 2016 YOUQingfei. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

int T;
vector<long long> nums;

void LoadFromFile()
{
    long long n;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        cin >> n;
        nums.push_back(n);
    }
}

void CountSheep(long long n, int i)
{
    if (n <= 0)
    {
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        return ;
    }
    
    long long result = n, copy = n;
    long long times = 1;
    int bit = 0;
    
    while (true)
    {
        result = n;
        while (n > 0)
        {
            int digit = n%10;
            n /= 10;
            bit |= 1 << digit;
            
            if (bit == (1 << 10)-1)
            {
                cout << "Case #" << i << ": " << result << endl;
                return ;
            }
        }
        n = copy * (++times);
    }
}


int main(int argc, const char * argv[]) {

    LoadFromFile();


    for (int i = 0; i < nums.size(); ++i)
    {
        CountSheep(nums[i], i+1);
    }
    return 0;
}
