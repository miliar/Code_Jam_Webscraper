/* Written by Filip Hlasek 2013 */
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>

#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,b) for(int i=0;i<(b);i++)

using namespace std;

int N;
long long P;

long long best (int N, long long P) {
  if (P == (1LL << N) - 1) return P;
  return best(N - 1, (1LL << (N - 1)) - ((1LL << N) - P)/2);
}

long long worst (int N, long long P) {
  if(P == 0) return 0;
  return (1LL << (N - 1)) + worst(N - 1, (P - 1) / 2);
}

int main(int argc, char *argv[]){
  int T;   
  scanf("%d", &T);
  FOR(t, 1, T) {
    printf("Case #%d: ", t);
    scanf("%d%lld", &N, &P);
    {
    long long left = 0, right = (1LL << N) - 1, middle;
    while (left < right) {
      middle = (left + right + 1) / 2;
      if (worst(N, middle) < P) left = middle;
      else right = middle - 1;
    }
    printf("%lld ", left);
    }
    {
    long long left = 0, right = (1LL << N) - 1, middle;
    while (left < right) {
      middle = (left + right + 1) / 2;
      if (best(N, middle) < P) left = middle;
      else right = middle - 1;
    }
    printf("%lld\n", left);
    }
  }
  return 0;
}
