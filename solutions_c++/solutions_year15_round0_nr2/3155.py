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
int n, a[2500];

bool check(int time){
     for (int i = 1; i <= time; ++i){
           int t = i;
           for (int j = 0; j < n; ++j){
                t += (a[j]-1) / i;
                if (t > time) break;
           }
           if (t <= time) return 1;
     }
     return 0;
}

void solve(){
     int ans = 0;
     scanf("%d", &n);
     for (int i = 0; i < n; ++i)
          scanf("%d", &a[i]), ans = max(a[i], ans);
     int l = 1, r = ans;
    // cout << check(5) << endl;
     while (l <= r){
          int mid = (l + r) >> 1;
         // cout << l << " " << r << endl;
          if (check(mid)) ans = min(mid, ans), r  = mid - 1;
          else l = mid + 1;
     }
     cout << ans << endl;
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
