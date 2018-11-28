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

int T, N;
int plate[1010];

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  REP(testcase,T) {
    scanf("%d\n",&N);
    int all = 0;
    REP(i,N) {
      scanf("%d\n",&plate[i]);
      all += plate[i];
    }

    int minM1 = 0, prev = 0;
    int minM2 = 0;
    REP(i,N) {
      if (plate[i] < prev) {
          minM1 += prev - plate[i];
      }
      prev = plate[i];
    }

    int rate = 0;
    REP(i,N-1) {
       int s = 0, e = plate[i];
       if (plate[i+1] >= plate[i]) s = 0; else s = plate[i] - plate[i+1];
       rate = max(rate, s);
    }    
    // cout << rate << endl;
    
    REP(i,N-1) {            
        minM2 += min(rate, plate[i]);
    }

    printf("Case #%d: %d %d",testcase+1,minM1,minM2);
    printf("\n");
  }

  return 0;
}