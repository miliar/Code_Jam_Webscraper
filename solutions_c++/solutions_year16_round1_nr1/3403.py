//
//  main.cpp
//  Main
//
//  Created by AIdancer on 16/4/6.
//  Copyright © 2016年 AIdancer. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LL;

char str[1005];

void solve()
{
    int T;
    scanf("%d", &T);
    string ans, tmp;
    for(int Case = 1; Case <= T; Case ++)
    {
        scanf(" %s", str);
        int n = (int)strlen(str);
        ans = "";
        string c = "";
        for(int i = 0; i < n; i++)
        {
            c = "";
            c = c.append(1, str[i]);
            if(c+ans >= ans+c)
                ans = c + ans;
            else
                ans = ans + c;
        }
        printf("Case #%d: %s\n", Case, ans.c_str());
    }
}

int main(int argc, const char * argv[])
{
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/A-large.in", "r", stdin);
    freopen("/Users/AIdancer/Downloads/Problem/Main/Main/data.out", "w", stdout);
    solve();
    return 0;
}















