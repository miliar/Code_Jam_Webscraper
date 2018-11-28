#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
typedef vector<int> vi; typedef long long Int;

#endif

#ifndef TOOLS

string i2bs (unsigned long long n, long b = 64, bool zeros = true) {
  string res = "0000000000000000000000000000000000000000000000000000000000000000";
  int c = b; --b;
  while (n) {res[b] += (n&1); --b; n >>= 1;}
  if (!zeros) return res.substr(b+1,c-b-1);
  return res.substr(0,c);
}

#endif

int T, X, R, C;

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  REP(testcase,T) {
    scanf("%d %d %d\n",&X,&R,&C);
    int winner = 0;
    if (X == 1) { winner = 1; }
    if (X == 2) {
      if ((C % X == 0) || (R % X == 0)) { winner = 1; }
    }
    if (X == 3) {
      if ((R % X == 0) && (C % X == 0)) { winner = 1; }
      if ((R % 2 == 0) && (C % X == 0)) { winner = 1; }
      if ((R % X == 0) && (C % 2 == 0)) { winner = 1; }
    }
    if (X == 4) {
      if ((R % X == 0) && (C % X == 0)) { winner = 1; }
      if ((R % 3 == 0) && (C % X == 0)) { winner = 1; }
      if ((R % X == 0) && (C % 3 == 0)) { winner = 1; }      
    }

    if (winner == 0) {
        printf("Case #%d: RICHARD",testcase+1);
    } else {
        printf("Case #%d: GABRIEL",testcase+1);
    }

    printf("\n");
  }

  return 0;
}