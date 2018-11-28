//
//  main.cpp
//  codejam2015
//
//  Created by Neuro Leap on 2015/04/10.
//  Copyright (c) 2015年 Neuro Leap. All rights reserved.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[])
{
    int t;
    int smax;
    string s;
    
    cin >> t;
    
    for( int i = 0; i < t; i++ )
    {
        cin >> smax;
        cin >> s;
        
        int friends = 0;
        int stand = 0;
        
        for( int j = 0; j < s.length(); j++ )
        {
            int num = s[j] - '0';
            if( stand < j )
            {
                friends += (j - stand);
                stand = j + num;
            }
            else
            {
                stand += num;
            }
        }
        
        cout << "Case #" << i + 1 << ": " << friends << endl;
    }
    

    return 0;
}
