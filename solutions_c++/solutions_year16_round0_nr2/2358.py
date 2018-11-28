#ifndef INCLUDED
#include <bits/stdc++.h>
#define INCLUDED
#define F first
#define S second
#define MP make_pair
#define PB push_back

using namespace std;
typedef long long L;
typedef long double LD;
#endif
/*
 * Author: raghumdani
 * Date Created: 09/04/2016
*/

#define TESTCASE

const int N = 123;
const int inf = 10000000;
const int mod = 1000000007;

char s[N];
int dp[N][N];

int f(int i, int mSigns, const int& n) {
  int& res = dp[i][mSigns];
  if(~res) return res;
  res = inf;
  if(i == n) {
    if(mSigns == 0) return res = 0;
    else return res;
  }
  res = min(res, f(i + 1, mSigns + ((s[i] == '-')?1:0), n));
  res = min(res, 1 + f(i + 1, i - mSigns + ((s[i] == '+')?1:0), n));
  return res;
}


int JAM16_B(int testNumber) {
  scanf("%s", s);
  int n = strlen(s);
  memset(dp, -1, sizeof(dp));
  printf("Case #%d: %d\n", testNumber, f(0, 0, n));
}

void allClear() {
  //NOTHING
}

int main() {
  int t = 1;
  #ifdef TESTCASE
    scanf("%d", &t);
  #endif
  for(int _ = 1; _ <= t; ++_) {
    int ret = JAM16_B( _ );
    allClear();
  }
  return(0);
}

