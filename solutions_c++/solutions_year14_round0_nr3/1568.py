//
//  C.c
//  codejam
//
//  Created by jie zheng on 14-4-12.
//  Copyright (c) 2014年 jie zheng. All rights reserved.
//

#include <iostream>
#include <string.h>
using namespace std;

int R,C,M;
bool flag;
int arr[60][60];
int s[60][60];
int x, y;
bool solve(int cx, int cy, int remain, int status[60][60])
{
    if(remain == 0)
    {
        for(int row = 0; row < R; ++row)
            for(int col = 0; col < C; ++col)
                arr[row][col] = status[row][col];
        return true;
    }
    if(remain < 0)
        return false;
    int r = 0;
    for(int i = cx-1; i <= cx+1; ++i)
        for(int j = cy-1; j <= cy+1; ++j)
        {
            if(i>=0 && i<R && j>=0 && j<C && status[i][j]==0)
            {
                r++;
                status[i][j] = 1;
            }
        }
    
    for(int i = cx-1; i <= cx+1; ++i)
        for(int j = cy-1; j <= cy+1; ++j)
        {
            if(i>=0 && i<R && j>=0 && j<C && !(i==cx&&j==cy)&& !s[i][j])
            {
                s[i][j] = 1;
                int tmp[60][60];
                for(int row = 0; row < R; ++row)
                    for(int col = 0; col < C; ++col)
                        tmp[row][col] = status[row][col];
                if(solve(i, j, remain-r, tmp))
                {
                    return true;
                }
                s[i][j] = 0;
                    
            }
        }
    
    return false;
        
    
}

int main()
{
    freopen("/Users/jiezheng/Dev/poj/C-small-attempt0.in", "r", stdin);
    freopen("/Users/jiezheng/Dev/poj/c1-out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int i = 0; i < T; ++i)
    {
        cin>>R>>C>>M;
        for(int j = 0; j < R; ++j)
            for(int k = 0; k < C; ++k)
            {
                memset(arr, 0, sizeof(int)*3600);
                memset(s, 0, sizeof(int)*3600);
                arr[j][k] = 2;
                s[j][k] = 1;
                flag = solve(j, k, R*C-M-1, arr);
                s[j][k] = 0;
                if(flag)
                {
                    x = j;
                    y = k;
                    goto e;
                }
            }
    e:
        cout<<"Case #"<<i+1<<":"<<endl;
        if(!flag)
            cout<<"Impossible"<<endl;
        else
        {
            for(int j = 0; j < R; ++j)
            {
                for(int k = 0; k < C; ++k)
                {
                   if(arr[j][k] == 0)
                       cout<<"*";
                    else if(arr[j][k] == 1)
                        cout<<".";
                    else
                        cout<<"c";
                    
                }
                cout<<endl;
            }
        }
    }
    
    return 0;
}
