// File Name: main.cpp
// Author: ***
// Created Time: 2014年04月12日 星期六 08时35分01秒

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

void solve()
{
  int m1[4][4];
  int m2[4][4];
  int g1, g2;
  cin>>g1;
  for (int i = 0;i < 4;++i) for (int j = 0;j < 4;++j) cin>>m1[i][j];
  cin>>g2;
  for (int i = 0;i < 4;++i) for (int j = 0;j < 4;++j) cin>>m2[i][j];
  
  map<int, int> mp1;
  for (int i = 0;i < 4;++i) {
    mp1[m1[g1 - 1][i]] = 1;
  }
  int ans = -1;
  for (int i = 0;i < 4;++i) {
    if (mp1.count(m2[g2 - 1][i]) > 0) {//found
      if (ans > 0) {
        cout<<"Bad magician!"<<endl;
        return;
      } else {
        ans = m2[g2 - 1][i];
      }
    }
  }
  if (ans == -1) {
    cout<<"Volunteer cheated!"<<endl;
  } else {
    cout<<ans<<endl;
  }
}
int main()
{
  freopen("/home/zhanyi/Downloads/A-small-attempt0.in", "r", stdin);
  //freopen("data.txt", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
    cout<<"Case #"<<i<<": ";
    solve();
  }
  return 0;
}

