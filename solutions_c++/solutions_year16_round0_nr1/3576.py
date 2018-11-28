//
//  main.cpp
//  test
//
//  Created by CCHo on 2016/4/8.
//  Copyright © 2016年 UCD. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int cases, n;
    
    cin >> cases;
    for (int c=1; c<=cases; ++c)
    {
        cin >> n;
        if (n==0)
        {
            cout << "Case #" << c << ": INSOMNIA" << endl;
        }
        else
        {
            int num = 0;
            int dig = 0;
            while (dig<1023)
            {
                num += n;
                int n_tmp = num;
                while(n_tmp>0)
                {
                    dig |= (1<<(n_tmp%10));
                    n_tmp /= 10;
                }
            }
            cout << "Case #" << c << ": " << num << endl;
        }
        
        
    }
    return 0;
}