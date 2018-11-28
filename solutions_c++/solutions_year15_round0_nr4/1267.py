// File Name: main.cpp
// Author: ***
// Created Time: 2015年04月11日 星期六 10时28分42秒

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

bool isok(int x, int r, int c)
{
  if ((r * c) % x != 0) return false;
  if (x <= 2) return true;
  if (x == 3) {
    if (r == 1 || c == 1) return false;
    return true;
  } else if (x == 4) {
    if (r > c) swap(r, c);
    if (r == 1 && c == 4) return false;
    if (r == 2 && c == 2) return false;
    if (r == 2 && c == 4) return false;
    return true;
  }
  return true;
}
int main()
{
  freopen("data.txt", "r", stdin);
  int T;
  cin>>T;
  REP (i, T) {
    int x, r, c;
    cin>>x>>r>>c;
#if 1
    if (isok(x, r, c)) {
      cout<<"Case #"<<i + 1<<": "<<"GABRIEL"<<endl;
    } else {
      cout<<"Case #"<<i + 1<<": "<<"RICHARD"<<endl;
    }
    
#endif
  }
    return 0;
}

