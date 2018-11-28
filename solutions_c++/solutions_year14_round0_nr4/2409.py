// File Name: main.cpp
// Author: ***
// Created Time: 2014年04月12日 星期六 20时51分14秒

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


int game2(vector<double> &a1, vector<double> &a2)
{
  sort(a1.begin(), a1.end());
  sort(a2.begin(), a2.end());
  //cout<<endl;
  //for (int i = 0;i < a1.size();++i) {
  //  cout<<a1[i]<<' ';
  //}
  //cout<<endl;
  //for (int i = 0;i < a1.size();++i) {
  //  cout<<a2[i]<<' ';
  //}
  //cout<<endl;
  int p = 0;
  int cnt = 0;
  for (int i = 0;i < a1.size();++i) {
    for (;p < a2.size();++p) {
      if (a2[p] > a1[i]) {
        cnt += 1;
        p++;
        break;
      }
    }
  }
  return a1.size() - cnt;
}
int game1(vector<double> &a1, vector<double> &a2)
{
  sort(a1.begin(), a1.end());
  sort(a2.begin(), a2.end());
  vector<int> mark(a1.size(), 0);
  int p = 0;
  int cnt = 0;
  for (int i = 0;i < a1.size();++i) {
    if (a1[i] > a2[p]) {
      cnt ++;
      p++;
    } else {
    }
  }
  return cnt;
}
void solve()
{
  int N;
  double tmp;
  vector<double> a1;
  vector<double> a2;
  cin>>N;
  for (int i = 0;i < N;++i) {
    cin>>tmp;
    a1.push_back(tmp);
  }
  for (int i = 0;i < N;++i) {
    cin>>tmp;
    a2.push_back(tmp);
  }
  int s1 = game1(a1, a2);
  int s2 = game2(a1, a2);
  cout<<s1<<' '<<s2<<endl;

}
int main()
{
   freopen("/home/zhanyi/Downloads/D-small-attempt0.in", "r", stdin);
 //freopen("data.txt", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
    cout<<"Case #"<<i<<": ";
    solve();
  }
    return 0;
}

