// File Name: main.cpp
// Author: ***
// Created Time: 2015年04月11日 星期六 09时07分25秒

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
#define FOR(i,a,b)  for(int i=(int)(a);i<(int)(b);++i)
#define REP(i,a)  FOR(i,0,a)
#define PB push_back
#define MP make_pair
#define VC vector
#define PII pair <int, int>
#define VI VC < int >
#define VF VC < float >
#define VS VC < string >
#define VVS VC < VS >
#define DB(a) cerr << #a << ": " << (a) << endl;
#define VALID(ret) (!isnan(ret) && !isinf(ret))
using namespace std;
int solve(vector<int> &num)
{
  sort(num.begin(), num.end(), greater<int>());

  int res = num[0];

  for (int i = 1;i <= num[0];++i) {
    vector<int> tmp = num;
    int ex = 0;
    REP (j, tmp.size()) {
      while (tmp[j] > i) {
        tmp[j] -= i;
        ex += 1; 
      }
    }
    if (i + ex < res) res = i + ex;
  }
  return res;
}
int main()
{
  freopen("data.txt", "r", stdin);
  int T;
  cin>>T;
  REP (i, T) {
    int n;
    cin>>n;
    vector<int> num(n, 0);
    REP (j, n) cin>>num[j];
    int res = solve(num);
    cout<<"Case #"<<i + 1<<": "<<res<<endl;
  }
    return 0;
    return 0;
}

