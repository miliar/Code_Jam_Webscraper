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
#include <iomanip>

#define INPUT "B-large.in"
#define OUTPUT "sample.out"

using namespace std;

ifstream fi(INPUT);
FILE *fo;

int test;
double C, F, X;
double res;

void input();
void solve();
void output();

int main() {
  int ntest;
  fi >> ntest;
  fo = fopen(OUTPUT, "w");
  for (test = 1; test <= ntest; test ++) {
    input();
    solve();
    output();
  }
  fi.close();
  fclose(fo);
  return 0;
}

void input() {
  //start code here
  fi >> C >> F >> X;
}

void solve() {
  res = X / 2;
  double a;
  a = 0;
  for (int t = 1; t <= 2000000; t ++) {
    a = a + C / (2 + (t - 1) * F);
    res = min(res, a + X / (2 + t * F));
  }
}

void output() {
  fprintf(fo, "Case #%d: %.7lf\n", test, res);
  //  fo << "Case #" << test << ": " << res << endl;
}
