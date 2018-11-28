#include <iostream>
#include <complex>
#include <sstream>
#include <string>
#include <algorithm>
#include <deque>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
#include <set>
#include <limits>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;
#define REP(i, j) for(int i = 0; i < (int)(j); ++i)
#define FOR(i, j, k) for(int i = (int)(j); i < (int)(k); ++i)
#define P pair<int, int>
#define SORT(v) sort((v).begin(), (v).end())
#define REVERSE(v) reverse((v).begin(), (v).end())
const double EPS = 1e-9;

int main() {
  int T; cin >>T;
  REP(t, T){
    double C, F, X, cookies = 2.0; cin >>C >>F >>X;
    double sum = 0.0;
    while(true){
      //工場を建てずに生産
      double a = X / cookies;
      //工場を建ててから生産
      double b = C / cookies + X / (cookies + F);
      if(a <= b){
        sum += a;
        break;
      }
      sum += C / cookies;
      cookies += F;
    }
    printf("Case #%d: %.7f\n", t + 1, sum);
  }
  return 0;
}
