//
//  main.cpp
//  codejam
//
//  Created by Will Sawyer on 4/12/14.
//  Copyright (c) 2014 Will Sawyer. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;
int main(int argc, const char * argv[])
{
    float C, F, X;
    float curF=2, sum = 0;
    int T;
    cin >> T;
    for (int i=0; i<T; i++)
    {
        sum = 0;
        cin >> C >> F >> X;
        curF = 2;
        while(X/curF >= C/curF + X/(curF+F))
        {
            sum += C/curF;
            curF += F;
        }
        //curF += F;
        sum += X/curF;
        printf("Case #%d: %.7f\n", i+1, sum);
    }
    return 0;
}

