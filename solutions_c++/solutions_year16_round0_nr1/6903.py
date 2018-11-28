//
//  main.cpp
//  code_jam
//
//  Created by Yanzun Huang on 4/8/16.
//  Copyright © 2016 Yanzun Huang. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;

class Checker
{
public:
    Checker()
    {
        for (int i = 0; i < 10; i++)
        {
            this->check[i] = false;
        }
        this->count = 0;
    }
    bool set(int digit)
    {
        if (!check[digit])
        {
            this->check[digit] = true;
            this->count++;
        }
        else
        {
            return false;
        }
        if (this->count == 10)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
private:
    bool check[10];
    int count;
};

bool analyzenum(long long num, Checker& check)
{
    long long temp = num;
    int num_digit = log10(temp) + 1;
    for (int i = 0; i < num_digit; i++)
    {
        int digit = temp % 10;
        temp /= 10;
        bool ret = check.set(digit);
        if (ret)
        {
            return true;
        }
    }
    return false;
}

int main(int argc, const char * argv[]) {
    int t;
    long long n;
    long long ret;
    cin>>t;
    for (int i = 1; i <= t; i++)
    {
        cin>>n;
        Checker check;
        if (n == 0)
        {
            cout << "Case #" << i <<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            long long multiply = 1;
            while (!analyzenum(multiply * n, check))
            {
                multiply++;
            }
            ret = multiply * n;
            cout << "Case #" << i <<": "<<ret<<endl;
        }
    }
    return 0;
}
