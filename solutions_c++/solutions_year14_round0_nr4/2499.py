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

//ifstream fi("A-small.in");
//ifstream fi("A-large.in");
//ifstream fi("A-small-practice.in");
ifstream fi("D-large.in");
ofstream fo("sample.out");

int test;
int n;
int rw, rd;
double a[2001];
double b[2001];

void input();
void war();
void deceitful();
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
  fi >> n;
  for (int i = 0; i < n; i ++) {
    fi >> a[i];
  }
  for (int i = 0; i < n; i ++) {
    fi >> b[i];
  }
  sort(a, a + n);
  sort(b, b + n);
}

void war() {
  rw = 0;
  bool used[1001];
  for (int i = 0; i < n; i ++) {
    used[i] = false;
  }
  for (int i = 0; i < n; i ++) {
    bool ok = false;
    for (int j = 0; j < n; j ++) {
      if (!used[j] && b[j] > a[i]) {
	used[j] = true;
	ok = true;
	break;
      }
    }
    if (!ok) {
      for (int j = 0; j < n; j ++) {
	if (!used[j]) {
	  used[j] = true;
	  break;
	}
      }
      rw ++;
    }
  }
}

void deceitful() {
  rd = 0;
  int l1 = 0;
  int l2 = l1;
  int r1 = n - 1;
  int r2 = r1;
  while (l1 <= r1) {
    if (a[l1] > b[l2]) {
      l1 ++;
      l2 ++;
      rd ++;
    }
    else {
      l1 ++;
      r2 --;
    }
  }
}

void solve() {
  war();
  deceitful();
}

void output() {
  fo << "Case #" << test << ": " << rd << " " << rw << endl;
}
