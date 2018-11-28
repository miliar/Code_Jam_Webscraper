#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 1001
#define ll long long
#define INF 0x3f3f3f3f

using namespace std;

int t,n,d[1001],dp[1001][1001];

int f(int n, int lim){
    if(n == 1){
        return 1;
    }if(n <= lim){
        return 1;
    }else{
        if(dp[n][lim] == -1){
            dp[n][lim] = 0;
            if(n % 2 == 0){
                dp[n][lim] += f(n/2, lim);
                dp[n][lim] += f(n/2, lim);
            }else{
                dp[n][lim] += f(n/2, lim);
                dp[n][lim] += f(n/2+1, lim);
            }
        }
        return dp[n][lim];
    }
}

int main(void){
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &t);

    for(int test = 1; test <= t; test++){
        scanf("%d", &n);
        for(int i = 0; i < n; i++){
            scanf("%d", &d[i]);
        }
        sort(d,d+n);
        int top = d[n-1], ans = INF;
        while(top > 0){
            int cost = 0;
            for(int i = n-1; i >= 0 && d[i] > top; i--){
                cost += (d[i] - top) / top + (((d[i] - top) % top) != 0);
            }
            ans = min(ans, top+cost);
            top--;
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
