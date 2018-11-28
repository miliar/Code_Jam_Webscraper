//
//  main.cpp
//  B
//
//  Created by IwfWcf on 13-4-14.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#define N 110

using namespace std;

int a[N][N], maxr[N], maxc[N];

inline bool check(int n, int m)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) 
            if (a[i][j] < maxr[i] && a[i][j] < maxc[j])
                return false;
    return true;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/IwfWcf/Desktop/gcj/B/in.txt", "r", stdin);
    freopen("/Users/IwfWcf/Desktop/gcj/B/out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++) maxr[i] = 0;
        for (int j = 0; j < m; j++) maxc[j] = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
                maxr[i] = max(maxr[i], a[i][j]);
                maxc[j] = max(maxc[j], a[i][j]);
            }
        printf("Case #%d: ", cases);
        if (check(n, m)) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}