//
//  main.cpp
//  CodeJam
//
//  Created by Sercan Tutar on 4/13/13.
//  Copyright (c) 2013 Sercan Tutar. All rights reserved.
//

#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <fstream>
#include <math.h>

#define LOG_ERROR cout << "ERROR IN LINE: " << __LINE__ << endl

using namespace std;

unsigned long long t;
unsigned long long r;

void solve()
{//cout << r << " "<< t;
    long long result = 0;
    while (true)
    {
        unsigned long long required = (2*r + 1);
        if (required <= t) {
            t -= required;
            r += 2;
            result++;
        } else
            break;
    }
    cout << result;
}

int main(int argc, const char * argv[])
{
    int noOfCases;
    cin >> noOfCases;
    for (int i = 0; i < noOfCases; i++)
    {
        // todo
        cin >> r >> t;
        
        cout << "Case #" << i+1 << ": ";
        solve();
		cout << endl;
    }
    
    return 0;
}
