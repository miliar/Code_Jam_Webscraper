//
//  D.c
//  codejam
//
//  Created by jie zheng on 14-4-12.
//  Copyright (c) 2014年 jie zheng. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

double naomi[1005];
double ken[1005];
int status[1005];
int w1, w2;
int fun(int num, double *arr1, double *arr2)
{
    memset(status, 0, sizeof(int)*1005);
    int ans = 0;
    for(int i = 0; i < num; ++i)
        for(int j = 0; j < num; ++j)
        {
            if(arr1[i] < arr2[j] && status[j] == 0)
            {
                status[j] = 1;
                ans++;
                break;
            }
        
        }
    return ans;
}

int main()
{
    freopen("/Users/jiezheng/Dev/poj/D-large.in", "r", stdin);
    freopen("/Users/jiezheng/Dev/poj/d2-out.txt", "w", stdout);
    int T, N;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        cin>>N;
        for(int j = 0; j < N; ++j)
            cin>>naomi[j];
        for(int k = 0; k < N; ++k)
            cin>>ken[k];
        sort(naomi, naomi+N);
        sort(ken, ken+N);
        w1 = fun(N, ken, naomi);
        w2 = N-fun(N, naomi, ken);
        cout<<"Case #"<<i+1<<": "<<w1<<" "<<w2<<endl;
        
    }
    return 0;
}
