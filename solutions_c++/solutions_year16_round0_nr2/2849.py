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
int solve(string s)
{
  int cnt = 0;
  for (int p = s.size() - 1;p >= 0;p--) {
    if (s[p] == '-') {
      string s0(s.begin(), s.begin() + p + 1);
      assert(s0.size() == p + 1);
      if (s0[0] == '-') {
        for (int i = 0;i <= p;++i) {
          s[i] = s0[p - i];
          if (s[i] == '-') s[i] = '+';
          else if (s[i] == '+') s[i] = '-';
        }
        cnt += 1;
      } else {
        for (int i = 0;i <= p;++i) {
          if (s0[i] == '+') {
            s0[i] = '-';
          } else {
            break;
          }
        }

        for (int i = 0;i <= p;++i) {
          s[i] = s0[p - i];
          if (s[i] == '-') s[i] = '+';
          else if (s[i] == '+') s[i] = '-';
        }
        cnt += 2;
      }
    }
  }
  return cnt;
}
int main()
{
  freopen("data", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
    string s;
    cin>>s;
    int ans = solve(s);
    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
  return 0;
}

