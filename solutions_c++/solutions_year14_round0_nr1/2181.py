//
//  main.cpp
//  codejam
//
//  Created by jie zheng on 14-4-12.
//  Copyright (c) 2014年 jie zheng. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    freopen("/Users/jiezheng/Dev/poj/A-small-attempt0.in", "r", stdin);
    freopen("/Users/jiezheng/Dev/poj/a1-out.txt", "w", stdout);
    int T,r1, r2;
    int arr1[5][5];
    int arr2[5][5];
    int res[20];
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        memset(res, 0, sizeof(int)*20);
        cin>>r1;
        for(int j = 0; j < 4; ++j)
            for(int k = 0; k < 4; ++k)
                cin>>arr1[j][k];
        cin>>r2;
        for(int j = 0; j < 4; ++j)
            for(int k = 0; k < 4; ++k)
                cin>>arr2[j][k];
        
        for(int j = 0; j < 4; ++j)
        {
            res[arr1[r1-1][j]] += 1;
            res[arr2[r2-1][j]] += 1;
        }
        int ans = 0;
        bool flag = false;
        for(int j = 1; j <= 16; ++j)
        {
            if(res[j] == 2)
            {
                if(!flag)
                {
                    flag = true;
                    ans = j;
                }
                else
                {
                    cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
                    ans = 0;
                    break;
                }
            }
        }
        if(flag&&ans)
            cout<<"Case #"<<i+1<<": "<<ans<<endl;
        else if(!flag)
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        
    }
    return 0;
}

