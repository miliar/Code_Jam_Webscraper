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
#define REP(i,a,b) for (int64 i=int64(a); i<int64(b); ++i)
void unittest();

int64 N, P;
int64 NN;

int64 best(int64 idx) {
  int64 left = idx;
  int64 right = NN-idx-1;
  // printf("%lld: %lld, %lld\n", idx, left, right);

  int64 ans = 0;
  REP(i, 0, N) {
    // printf("LR: %lld, %lld\n", left, right);
    ans <<= 1LL;

    if (right) {
      // Winning
      ans |= 1LL;
      --right;
    } else {
      // Losing
      --left;
    }

    if (left%2==1) {
      assert(right%2==1);
      ++left; --right;
    }
    left /= 2;
    right /=2;
  }
  // printf("best(%lld)=%lld\n", idx, ans);
  return ans;
}

int64 worst(int64 idx) {
  int64 left = idx;
  int64 right = NN-idx-1;

  int64 ans = 0;
  REP(i, 0, N) {
    ans <<= 1LL;

    if (left) {
      // Losing
      --left;

    } else {
      // Winning
      ans |= 1LL;
      --right;
    }

    if (left%2==1) {
      assert(right%2==1);
      --left; ++right;
    }

    left /= 2;
    right /=2;
  }
  // printf("best(%lld)=%lld\n", idx, ans);
  return ans;
}

void solve(int caseNum) {
  cin>>N>>P;
  NN = 1LL<<N;

  int64 bestAns = 0;

  int64 lower=0, upper=NN;

  while(lower!=upper-1) {
    int64 mid = (lower+upper)/2LL;
    int64 bestRank = NN-best(mid);
    if (bestRank<=P) {
      lower = mid;
    } else {
      upper = mid;
    }
  }
  bestAns = lower;

  int64 worstAns = 0;

  lower=0, upper=NN;
  while(lower!=upper-1) {
    int64 mid = (lower+upper)/2LL;
    int64 worstRank = NN-worst(mid);
    if (worstRank<=P) {
      lower = mid;
    } else {
      upper = mid;
    }
  }

  worstAns = lower;

  printf("Case #%d: %lld %lld", caseNum, worstAns, bestAns);
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

