//this is the default for Google code jam only
#include <string>
#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#define pii pair<int, int>

using namespace std;

ifstream fi("A-small-attempt0.in");
//ifstream fi("A-large.in");
//ifstream fi("A-small-practice.in");
//ifstream fi("sample.in");
ofstream fo("sample.out");

int test;
long long res;

void input();
void solve();
void output();

long long p, q;

int main() {
  int ntest;
  fi >> ntest;
  for (test = 1; test <= ntest; test ++) {
    input();
    solve();
    output();
  }
  fi.close();
  fo.close();
  return 0;
}

long long gcd(long long a, long long b) {
  if (a < b) {
    swap(a, b);
  }
  while (b > 0) {
    long long r = a % b;
    a = b;
    b = r;
  }
  return a;
}

void input() {
  //start code here
  res = -1;
  char c;
  fi >> p >> c >> q;
  long long t = gcd(p, q);
  p = p / t;
  q = q / t;
  
  long long one = 1;
  one = (one << 40);
  if (__builtin_popcount(q) != 1) {
    return;
  }
  if (q > one) {
    return;
  }
  res = 0;
  //  cout << p << " " << q << endl;
  while (p < q) {
    res ++;
    p = p * 2;
  }
}

void solve() {
}

void output() {
  if (res == -1) {
    fo << "Case #" << test << ": impossible" << endl;
  }
  else {
    fo << "Case #" << test << ": " << res << endl;    
  }
}
