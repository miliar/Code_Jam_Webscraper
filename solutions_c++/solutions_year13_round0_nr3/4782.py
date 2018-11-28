/*
 * Author: stormdpzh
 * Created Time:  Saturday, April 13, 2013 PM02:31:11 HKT
 * File Name: c.cpp
 */
#include <iostream>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <functional>

#define sz(v) ((int)(v).size())
#define rep(i, n) for(int i = 0; i < n; i++)
#define repf(i, a, b) for(int i = a; i <= b; i++)
#define repd(i, a, b) for(int i = a; i >= b; i--)
#define out(n) printf("%d\n", n)
#define mset(a, b) memset(a, b, sizeof(a))
#define lint long long

using namespace std;

const int INF = 1 << 30;
const int MaxN = 100005;

int a, b;

bool check(int x)
{
    int t = 0, y = x;
    while(y) {
        t = t * 10 + y % 10;
        y /= 10;
    }
    return t == x;
}

int gao()
{
    int ans = 0;
    repf(i, a, b) {
        if(check(i)) {
            int t = (int)sqrt(i);
            if(t * t == i && check(t))
                ans++;
        }
    }
    return ans;
}

int main()
{
    int t;
    scanf("%d", &t);
//    freopen("c.out", "w", stdout);
    repf(i, 1, t) {
        scanf("%d%d", &a, &b);
        printf("Case #%d: ", i);
        out(gao());
    }
    return 0;
}

