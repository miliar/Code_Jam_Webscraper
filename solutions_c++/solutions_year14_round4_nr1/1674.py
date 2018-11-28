//
//  round2A.cpp
//  codejam
//
//  Created by jie zheng on 14-5-31.
//  Copyright (c) 2014年 jie zheng. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string>
#include <stdio.h>
using namespace std;


int main()
{
    freopen("/Users/jiezheng/Dev/poj/A-large.in", "r", stdin);
    freopen("/Users/jiezheng/Dev/poj/a1-largeout.txt", "w", stdout);
    int T;
    int n, x;
    int arr[10005];
    cin>>T;
    for(int caseid = 1; caseid <= T; ++caseid)
    {
        int ans = 0;
        cin>>n>>x;
        for(int i = 0; i < n; ++i)
            cin>>arr[i];
        sort(arr, arr+n);
        for(int start = 0, end = n-1; start <= end;)
        {
            if(start == end)
            {
                ans++;
                break;
            }
            if(arr[start]+arr[end] <= x)
            {
                start++;
                end--;
                ans++;
            }
            else
            {
                end--;
                ans++;
            }
            
        }
        
        //ans++;
        cout<<"Case #"<<caseid<<": "<<ans<<endl;
    }
    
    return 0;
}