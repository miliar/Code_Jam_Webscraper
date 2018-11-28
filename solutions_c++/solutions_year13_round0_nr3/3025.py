//
//  main.cpp
//  FairAndSquare
//
//  Created by Ahmed Mohammed Abdurahman on 4/13/13.
//  Copyright (c) 2013 Better MDM LLC. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>


using namespace std;



int floor2Pow(uint64_t n)
{
    for (int i = 63; i; i--)
        if (n & ((uint64_t)1) << i) return i;
    return 0;
}

// returns digit count
int getDecimalDigits(uint64_t n, int out[30])
{
    int i = 0;
    for (; n; i++, n /= 10)
        out[i] = n % 10;
    return i;
}

uint64_t evaluateDecimal(int digits[0], int digitCount)
{
    uint64_t result = 0;
    for (int i = digitCount - 1; i >= 0; i--)
        result = (result << 3) + (result << 1) + digits[i];
    return result;
}


bool isPalindrome(uint64_t n)
{
    int digits[30];
    int dc = getDecimalDigits(n, digits);
    int lastDigitIndex = dc - 1;
    for (int i = 0; i < (dc >> 1); i++)
        if (digits[i] != digits[lastDigitIndex - i])
            return false;
    return true;
}



int main(int argc, const char * argv[])
{
    if (argc < 3)
    {
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(1);
    }
    
    
    // open files
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open())
    {
        printf("Unable to open input file\n");
        exit(1);
    }
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open())
    {
        printf("Unable to open output file\n");
        exit(1);
    }
    fout.seekp(0);
    
    
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {           // process each test case
        uint64_t a, b;
        
        fin >> a >> b;
        
        // approximate square roots
        uint64_t ar = ((uint64_t)1) << (floor2Pow(a) / 2);
        uint64_t br = ((uint64_t)1) << (floor2Pow(b) / 2 + 1);
        
        // find the first larger palindrome
        for (; ar <= br; ar++)
            if (isPalindrome(ar)) break;
        
        uint64_t count = 0;
        for (; ar <= br; ar++)
        {
            if (isPalindrome(ar))
            {
                uint64_t ar2 = ar * ar;
                if ((a <= ar2) && (ar2 <= b))
                    if (isPalindrome(ar2))count++;
            }
        }
        
        fout << "Case #" << (tcase + 1) << ": " << count << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}