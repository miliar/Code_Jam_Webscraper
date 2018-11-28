//
//  main.cpp
//  FAS
//
//  Created by Tanifuji Keita on 13/04/14.
//  Copyright (c) 2013年 Tanifuji Keita. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <math.h>
using namespace std;

class FAS
{
public:
    FAS()
    {
        count = 0;
        cin >> min;
        cin >> max;
    };
    
    //============================================================
    void check()
    {
        long number = static_cast<int>(sqrt(min));
        while( number * number <= max )
        {
            long square = number * number;
            if( square < min )
            {
                number++;
                continue;
            }
            if(isFair(number) && isFair(square))
            {
                count++;
            }
            number++;
        }
    }
    
    bool isFair( long number )
    {
        std::ostringstream stream;
        stream << number;
        string num = stream.str();
        int length = (int)num.length();
        for (int i = 0; i < length/2; ++i)
        {
            if( num[i] != num[length-1-i] ){
//                cout << "false" << endl;
                return false;
            }
        }
//        cout << "true" << endl;
        return true;
    }
    
    //============================================================
    
public:
    int min;
    int max;
    int count;
};

namespace Util {
    void WriteResult( int caseNumber, int result )
    {
        cout << "Case #" << caseNumber << ": " << result << endl;
    }
}

int main(int argc, const char * argv[])
{
    int TestCount = 0;
    cin >> TestCount;
    
    for (int i = 0; i < TestCount; ++i)
    {
        FAS fas;
        fas.check();
        Util::WriteResult(i+1, fas.count);
    }
    
    return 0;
}

