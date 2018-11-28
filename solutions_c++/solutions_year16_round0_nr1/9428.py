//
//  main.cpp
//  counting_sheep
//
//  Created by Quintin-Donnelly on 4/9/16.
//  Copyright © 2016 Quintin-Donnelly. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

bool checkArray(bool digits[]);
void addDigits(unsigned long long n, bool arr[]);
void initialize(bool arr[])
{
    for(int i = 0; i < 10; ++i)
    {
        arr[i] = false;
    }
}

int main() {
    ifstream inF;
    ofstream outF;
    
    inF.open("A-large.in");
    outF.open("a-large.out");
    
    unsigned int t;
    inF >> t;
    
    unsigned int n;
    unsigned long long result = 0;
    bool *digits = new bool[10];
    initialize(digits);
    
    for(unsigned int test_case = 1; test_case < t + 1; ++test_case)
    {
        inF >> n;
        
        if(n == 0)
        {
            outF << "Case #" << test_case << ": INSOMNIA" << endl;
            continue;
        }
        
        for(int i = 1; !checkArray(digits); ++i)
        {
            result = n * i;
            addDigits(result, digits);
        }
        
        outF << "Case #" << test_case << ": " << result << endl;
        
        result = 0;
        n = 0;
        initialize(digits);
    }
    
    
    inF.close();
    outF.close();
    delete[] digits;
    return 0;
}


bool checkArray(bool digits[])
{
    for(int i = 0; i < 10; ++i)
    {
        if(!digits[i])
            return false;
    }
    
    return true;
}


void addDigits(unsigned long long n, bool arr[])
{
    while(n != 0)
    {
        arr[n % 10] = true;
        n = n /10;
    }
}
