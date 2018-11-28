//
//  main.cpp
//  test3
//
//  Created by CCHo on 2016/4/9.
//  Copyright © 2016年 UCD. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int cases, N, J;
    cin >> cases >> N >> J;
    
    unsigned long int div[9];
    
    for (int i=0; i<9; i++)
        div[i] = 1;
    
    for (int i=0; i<N/2; i++)
    {
        for (int k=0; k<9; k++)
            div[k] *= (k+2);
    }
    
    for (int i=0; i<9; i++)
        div[i] += 1;
    
    cout << "Case #1:" << endl;
    
    for (int i=0; i<J; i++)
    {
        cout << "1";
        
        int tmp = i;
        for (int k=0; k<N/2-2; k++)
        {
            int x = tmp%2;
            tmp /= 2;
            cout << x;
        }
        
        cout << "11";
        
        tmp = i;
        for (int k=0; k<N/2-2; k++)
        {
            int x = tmp%2;
            tmp /= 2;
            cout << x;
        }
        
        cout << "1 ";
        
        for (int k=0; k<9; k++)
            cout << div[k] << " ";
        cout << endl;
    }
    

    return 0;
}