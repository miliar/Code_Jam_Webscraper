//
//  main.cpp
//  C
//
//  Created by IwfWcf on 13-4-13.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>
#define PB push_back

using namespace std;

typedef long long LL;

int n, a[10];
vector<LL> v;

inline bool check(LL x)
{
    int len = 0, d[20];
    while (x) {
        d[len++] = x % 10;
        x /= 10;
    }
    for (int i = 0; i < len / 2; i++)
        if (d[i] != d[len - i - 1]) return false;
    return true;
}

void dfs(int dep)
{
    if (dep > (n + 1) / 2) {
        LL ret = 0;
        for (int i = 1; i <= n / 2; i++)
            ret = ret * 10 + a[i];
        if (n % 2)
            ret = ret * 10 + a[(n + 1) / 2];
        for (int i = n / 2; i; i--)
            ret = ret * 10 + a[i];
        int x = sqrt(ret);
        if (LL(x) * x == ret && check(x) && check(ret)) v.PB(ret);
        return;
    }
    if (dep == 1) {
        for (int i = 1; i < 10; i++) {
            a[dep] = i;
            dfs(dep + 1);
        }
    } else {
        for (int i = 0; i < 10; i++) {
            a[dep] = i;
            dfs(dep + 1);
        }
    }
}

int main(int argc, const char * argv[])
{
    freopen("/Users/IwfWcf/Desktop/gcj/C/in.txt", "r", stdin);
    freopen("/Users/IwfWcf/Desktop/gcj/C/out.txt", "w", stdout);
    v.PB(1), v.PB(4), v.PB(9);
    for (n = 2; n <= 14; n++) dfs(1);
    //cout << v.size() << "\n";
    //for (int i = 0; i < v.size(); i++) cout << v[i] << " ";
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        LL a, b;
        cin >> a >> b;
        vector<LL>::iterator low, up;
        low = lower_bound(v.begin(), v.end(), a);
        up = upper_bound(v.begin(), v.end(), b);
        printf("Case #%d: %d\n", cases, up - low);
    }
    return 0;
}

