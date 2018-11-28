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
void solve(int k, int c, int s)
{
	unsigned long long inc = 1;
	for (int i = 1;i <= c - 1;++i) {
		inc = inc * (unsigned long long)k;
	}
	for (int i = 0;i < s;++i) {
		unsigned long long p = (unsigned long long)i * inc + 1;
		if (i == s - 1) {
			cout<<p<<endl;
		} else {
			cout<<p<<' ';
		}
	}
}
int main()
{
  freopen("data", "r", stdin);
  int T;
  cin>>T;
  for (int i = 1;i <= T;++i) {
		int k, c, s;
		cin>>k>>c>>s;
    cout<<"Case #"<<i<<": ";
    solve(k, c, s);
  }
  return 0;
}

