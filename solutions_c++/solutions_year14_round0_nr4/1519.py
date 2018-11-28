//
//  main.cpp
//  Google3
//
//  Created by happy_1113xie on 14-4-12.
//  Copyright (c) 2014年 happy_1113xie. All rights reserved.
//

#include <fstream>
#include <algorithm>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream f1;
    f1.open("/Users/happy_1113xie/Desktop/D-large.in");
    ofstream f2;
    f2.open("/Users/happy_1113xie/Desktop/D.out");
    
    int T, n;
    double num1[1000], num2[1000];
    f1 >> T;
    for (int Testi = 1; Testi <= T; ++Testi){
        f2 << "Case #" << Testi << ": ";
        
        f1 >> n;
        for (int i = 0; i < n; ++i)
            f1 >> num1[i];
        for (int i = 0; i < n; ++i)
            f1 >> num2[i];
        
        sort(num1, num1 + n);
        sort(num2, num2 + n);
        
        int top = -1, ans1 = 0;
        bool flag = false;
        for (int i = 0; i < n; ++i)
        {
            flag = false;
            for (int j = top + 1; j < n; ++j)
                if (num2[j] > num1[i]){
                    top = j;
                    flag = true;
                    break;
                }
            
            if (!flag)
            {
                ans1 = i;
                break;
            }
        }
        
        if (flag)
            ans1 = 0;
        else
            ans1 = n - ans1;
        
        int ans2 = 0;
        int f = 0, r = n - 1;
        for (int i = n - 1; i >= 0; --i){
            if (num2[i] >= num1[r])
                ++f;
            else
            {
                --r;
                ++ans2;
            }
            
        }
        
        f2 << ans2 << " " << ans1;
        f2 << endl;
    }
    
    f1.close();
    f2.close();
    return 0;
}

