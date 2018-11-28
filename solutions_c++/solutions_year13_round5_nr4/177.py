#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

const int MN = 1<<20;
double dp[MN];
int N;
int mm;

double rec(int mask) {
  if (dp[mask]>=0) return dp[mask];
  if (mask==mm-1) return 0;

  double sum=0.0;

  REP(i, 0, N) {
    int cur = i;
    int wait = 0;
    while(mask&(1<<cur)) {
      ++wait;
      ++cur;
      cur%=N;
    }
    int newMask = mask | (1<<cur);
    double profit = double(N-wait) + rec(newMask);
    // printf("P %d, %d, %d\n", mask, N-wait, profit);

    sum += profit;
  }

  double avg = sum / double(N);
  dp[mask] = avg;

  // printf("rec(%d) = %lf\n", mask, dp[mask]);

  return avg;
}

void solve(int caseNum) {
  string s;
  cin>>s;
  N = s.size();
  mm = (1<<N);
  REP(i, 0, mm)
    dp[i] = -1;
  // cout<<N<<endl;
  int initMask = 0;
  REP(i, 0, N) {
    if (s[i]=='X') {
      initMask |= (1<<i);
    }
  }

  double ans = rec(initMask);

  printf("Case #%d: %.10lf", caseNum, ans);
  printf("\n", caseNum);
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

