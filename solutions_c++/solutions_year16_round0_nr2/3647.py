//
//  main.cpp
//  test2
//
//  Created by CCHo on 2016/4/8.
//  Copyright © 2016年 UCD. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int cases;
    
    cin >> cases;
    for (int c=1; c<=cases; ++c)
    {
        string cake;
        cin >> cake;
        int count = 0;
        bool bottom = true;
        for (int i = cake.length()-1; i>=0; i--)
        {
            //bool x = (cake[i]=='+')^bottom;
            if ((cake[i]=='+')^bottom)
            {
                count++;
                bottom = !bottom;
            }
        }
        cout << "Case #" << c << ": " << count << endl;
        
    }
    return 0;
}