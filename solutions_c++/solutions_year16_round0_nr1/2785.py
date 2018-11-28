// File Name: a.cpp
// Author: ***
// Created Time: 2016年04月09日 星期六 08时44分10秒

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
long long solve(int n)
{
  if (n == 0) return -1;
  map<int, int> mp;
  int c = 1;
  while (true) {
    long long n0 = (long long)n * (long long)c;
    while (n0 > 0) {
      int p = n0 % 10;
      mp[p] = 1;
      n0 /= 10;
    }
    if (mp.size() == 10) return (long long)n * (long long)c;
    c += 1;
  }
  return -1;
}
int main()
{
  freopen("data", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
    int n;
    cin>>n;
    long long ans = solve(n);

    if (ans < 0) {
      cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    } else {
      cout<<"Case #"<<i<<": "<<ans<<endl;
    }
  }
  return 0;
}

