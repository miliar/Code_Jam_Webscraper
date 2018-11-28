//
//  main.cpp
//  R1a
//
//  Created by CCHo on 2016/4/15.
//  Copyright © 2016年 UCD. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int cases;
    string S;
    char ans[30];
    
    cin >> cases;
    for (int c = 1; c <= cases; c++)
    {
        cin >> S;
        int head = 14;
        int tail = 14;
        ans[head] = S[0];
        
        for (int i = 1; i < S.length(); i++)
        {
            if (S[i]>=ans[head])
            {
                head--;
                ans[head] = S[i];
            }
            else
            {
                tail++;
                ans[tail] = S[i];
            }
        }
        
        
        cout << "Case #" << c << ": ";
        for (int i = head; i <= tail; i++)
        {
            cout << ans[i];
        }
        cout << endl;
        
    }
    return 0;
}