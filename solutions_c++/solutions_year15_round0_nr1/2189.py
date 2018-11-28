// File Name: main.cpp
// Author: ***
// Created Time: 2015年04月11日 星期六 08时26分21秒

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

int solve(int n, string code)
{
  vector<int> s(code.size(), 0);
  REP (i, code.size()) {
    s[i] = code[i] - '0';
  }
  REP (i, s.size()) {
    if (s[i] > 1) {
      if (i != s.size() - 1) {
        s[i + 1] += s[i] - 1;
      }
      s[i] = 1;
    }
  }
  int res = 0;
  REP (i, s.size()) {
    if (s[i] == 0) res += 1;
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
    string code;
    cin>>n>>code;
    int num = solve(n, code);
    cout<<"Case #"<<i + 1<<": "<<num<<endl;
  }
    return 0;
}

