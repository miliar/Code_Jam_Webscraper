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

int res;
int a[17];

void input();
void solve();
void output();

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

void input() {
  //start code here
  int r;
  fi >> r;
  for (int i = 1; i <= 16; i ++) {
    a[i] = 0;
  }
  for (int i = 1; i <= 4; i ++) {
    for (int j = 1; j <= 4; j ++) {
      int c;
      fi >> c;
      if (i == r) {
	a[c] ++;
      }
    }			   
  }
  fi >> r;
  for (int i = 1; i <= 4; i ++) {
    for (int j = 1; j <= 4; j ++) {
      int c;
      fi >> c;
      if (i == r) {
	a[c] ++;
      }
    }			   
  }
}

void solve() {
  res = -2;
  int c = 0;
  for (int i = 1; i <= 16; i ++) {
    if (a[i] == 2) {
      c ++;
    }
  }
  if (c == 1) {
    for (int i = 1; i <= 16; i ++) {
      if (a[i] == 2) {
	res = i;
	return ;
      }
    }
  }
  if (c == 0) {
    res = -1;
  }
  else {
    res = 0;
  }
}

void output() {
  if (res == -1) {
    fo << "Case #" << test << ": Volunteer cheated!" << endl;
  }
  else if (res == 0) {
    fo << "Case #" << test << ": Bad magician!" << endl;    
  }
  else {
    fo << "Case #" << test << ": " << res << endl;
  }
}
