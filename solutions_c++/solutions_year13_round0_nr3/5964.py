//
//  LAwnmower
//  
//
//  Created by Laszlo Majer on 4/13/13.
//
//


#include <iostream>
#include <sstream>
#include <string>


using namespace std;


typedef unsigned long long UInt64;


// Global variables
bool IsPalindrome(UInt64 number)
{
    stringstream stringStream;
    stringStream << number;
    std::string numberString = stringStream.str();
    size_t length = numberString.length();
    size_t halfLength = length / 2;
    for (int i = 0; i < halfLength; ++i)
    {
        if (numberString[i] == numberString[length - 1 - i])
            continue;

        return false;
    }

    return true;
};


int main()
{
    int T = 0;

    cin >> T;
    for (int n = 0; n < T; ++n)
    {
        UInt64 lowerLimit = 0;
        UInt64 upperLimit = 0;
        cin >> lowerLimit;
        cin >> upperLimit;
        
        // Find starting point
        UInt64 startingRoot = 1;
        while ((startingRoot * startingRoot) < lowerLimit)
            ++startingRoot;
        
        int result = 0;
        for (int i = startingRoot; i * i <= upperLimit; ++i)
        {
            if (!IsPalindrome(i))
                continue;
            if (!IsPalindrome(i * i))
                continue;

            ++result;
        }

        cout << "Case #" << n + 1 << ": " << result << endl;
    }
}
