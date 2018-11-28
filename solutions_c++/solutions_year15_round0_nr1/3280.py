/*
 * Author:  Yzcstc
 * Created Time:  2015/4/11 21:55:50
 * File Name: a.cpp
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
#define rep(i, a, b) for (int i = (a); i <= (b); ++i)
#define red(i, a, b) for (int i = (a); i >= (b); --i)
#define M0(x)  memset(x, 0, sizeof(x))
#define MP make_pair
#define PB push_back
#define eps 1e-8
#define pi acos(-1.0)
typedef long long LL;
using namespace std;
char s[1200];

void solve(){
    int n;
    scanf("%d%s", &n, s);
    n++;
    int ans = 0, sum = 0;
    for (int i = 0; i < n; ++i){
         if (sum < i) ans += i - sum, sum = i;
         sum += s[i] - '0';
    }
    printf("%d\n", ans);
}
int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i){
          printf("Case #%d: ", i);
          solve();
    }
    return 0;
}
