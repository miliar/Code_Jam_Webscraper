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
    freopen("D-large.in","rt",stdin);
    //    freopen("D-sample.txt","rt",stdin);
    
    int T;
    
    cin >> T;
    
    for( int i = 0; i < T; i++ )
    {
        int X, R, C;
        cin >> X;
        cin >> R;
        cin >> C;
        
        if( X >= 7 )
        {
            cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        
        if( max(R,C) < X )
        {
            cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        
        if( (R * C) % X != 0 )
        {
            cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        
        if( (X + 1) / 2 > min(R, C) )
        {
            cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
            continue;
        }
        
        if( 1 <= X && X <= 3 )
        {
            cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
            continue;
        }
        
        if( X == 4 )
        {
            if( min(R,C) > 2 )
            {
                cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
                continue;
            }
            else
            {
                cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
                continue;
            }
        }
        
        if( X == 5 )
        {
            if( (R == 3 && C == 5) || (R == 5 && C == 3) )
            {
                cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
                continue;
            }
            else
            {
                cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
                continue;
            }
        }
        
        if( X == 6 )
        {
            if( min(R,C) > 3 )
            {
                cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
                continue;
            }
            else
            {
                cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
                continue;
            }
        }
    }
    
    return 0;
}
