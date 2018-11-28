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

using namespace std;

double C, F, X;
double dp[100002];
int vis[100002], t;

double func(){
    dp[0] = C/2.0;
    if(dp[0] + X / (F+2.0) >= X /(2.0)) return X/2.0;
    for(int i = 1; i <= 100000; i++){
        double buyFarm = C / ((double)i * F + 2.0);
        double waitX = X / ((double)i * F+ 2.0);
        if(buyFarm + dp[i-1] + (X / ((double)(i+1) * F + 2.0)) > waitX + dp[i-1]){
            dp[i] = waitX + dp[i-1];
            return dp[i];
        }else{
            dp[i] = buyFarm + dp[i-1];
        }
    }
    return dp[10000];
}

int main(void){
    //freopen("in.in", "r", stdin);
    //freopen("out", "w", stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++){
        scanf("%lf%lf%lf", &C, &F, &X);
        memset(vis,0,sizeof(vis));
        printf("Case #%d: %.7lf\n", test, func());
    }
    return 0;
}
