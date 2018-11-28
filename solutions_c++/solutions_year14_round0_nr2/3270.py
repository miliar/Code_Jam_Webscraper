#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
// 初期化！
int t;
double c, f, x;
// c : num of cookies to add a farm
// f : num of cookies per sec when add a farm
// x : num of cookies to win

void solve(int testnum) {
  double est_time1 = 0.0; // estimated time of making x cookies without making farms anymore.
  double est_time2 = 0.0; // estimated time of making x cookies with adding a farm.
  vector<double> ans; // minimum time of making x cookies.
  double cookies = 0; // num of cookies made till now
  double per_total = 2.0; // num of cookies per sec now
  while(cookies < x) {
    double per_total2 = per_total;
    // printf("per_total: %.7f\n", per_total); 
    est_time1 = est_time2 = 0.0; // initialize
    est_time1 = x / per_total;
    // printf("est_time1: %.7f\n", est_time1);
    est_time2 = c / per_total; // estimated time to make next farm.
    // printf("est_time2 to make next farm: %.7f\n", est_time2);
    // cookies += c;
    // printf("cookies: %.7f\n", cookies);
    per_total2 += f; // num of cookies per sec when add a farm.
    // printf("per_total2: %.6f\n", per_total2);
    double total_time = est_time2 + (x / per_total2);
    // printf("total_time: %.7f\n", total_time);
    if (est_time1 > total_time) {
      per_total = per_total2;
      ans.push_back(est_time2);
    }
    else {
      ans.push_back(est_time1);
      cookies = x;
    }
  }
  double answer = 0.0;
  rep(i,ans.size()){
    answer += ans.at(i);
  }
  printf("Case #%d: %.7f\n", testnum, answer);
}

int main() {
  cin >> t;
  rep(i,t) {
    cin >> c >> f >> x;
    solve(i+1); // 1 origin

  }
  return 0;
}
