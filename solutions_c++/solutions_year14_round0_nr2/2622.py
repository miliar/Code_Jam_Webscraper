// File Name: main.cpp
// Author: ***
// Created Time: 2014年04月12日 星期六 10时23分16秒

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring>
#include <cassert>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

double C,F,X;
double getCost(int time)
{
  double ans = 0;
  for (int i = 0;i < time;++i) {
    ans += C / (2.0 + i * F);
  }
  ans += X / (2.0 + time * F);
  return ans;
}
void solve()
{
  cin>>C>>F>>X;
  double ans0 = X / 2;
  for (int t = 1;;t++) {
    double cost = getCost(t);
    //cout<<cost<<endl;
    if (cost < ans0) {
      ans0 = cost;
    } else if (cost >= ans0) {
      break;
    }
  }
  printf("%.9f\n", ans0);
  //cout<<ans0<<endl;

}
int main()
{
  freopen("/home/zhanyi/Downloads/B-small-attempt0.in", "r", stdin);
  //freopen("data.txt", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
    cout<<"Case #"<<i<<": ";
    solve();
  }
    return 0;
}

