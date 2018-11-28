/*
 * Author:  Yzcstc
 * Created Time:  2014/4/12 21:43:10
 * File Name: B.cpp
 */
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<ctime>
#include<utility>
#define M0(x) memset(x, 0, sizeof(x))
#define MP make_pair
#define Fi first
#define Se second
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define PB push_back
#define Inf 0x3fffffff
#define eps 1e-8
typedef long long LL;
using namespace std;
double C, F, X;
int T;

void solve(){
     scanf("%lf%lf%lf", &C, &F, &X);
     double ans = X / 2.0;
     double tmp = 0, times = 0;
     double v = 2.0;
     for (int i = 1;; ++i){
           times += C / v;
           if (times > ans) break;
           v += F;
           ans = min(ans, times + X / v);
     }
     printf("%.7lf\n", ans);  
}

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i){
         printf("Case #%d: ", i); 
         solve();
    }    
    fclose(stdin);  fclose(stdout);
    return 0;
}
