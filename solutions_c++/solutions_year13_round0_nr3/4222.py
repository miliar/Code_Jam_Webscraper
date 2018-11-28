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

Int T,A,B;
int P[10000001];
vector<Int> fas; // fair and square numbers

Int reverseNumber (Int n) {
  Int res = 0;
  while (n) {
    res = res*10 + n%10;
    n /= 10;
  }
  return res;
}

bool isPalindrome (Int n) {
  return (n == reverseNumber(n));
}

int countLess (vector<Int> &A, Int key) {
  int count = 0;
  vector<Int>::iterator firstBigger = lower_bound(A.begin(), A.end(), key);
  if (firstBigger == A.end()) {
    count = A.size();
  } else {
    count = firstBigger - A.begin();
  }
  return count;
}

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  fas.clear();
  CLR(P,0);
  for (Int i = 1; i <= 10000000; ++i) {
    if (isPalindrome(i)) {
      P[i] = 1;
      if (isPalindrome(i*i)) {
        fas.PB(i*i);
      }
    }
  }

  /*
  cout << fas.size() << endl; // 39
  REPS(i,fas) {
    cout << fas[i] << " " << (int) sqrt(fas[i]) << endl;
  }
  */

  cin >> T;
  REP(testcase,T) {
    cin >> A >> B; 
    solution:
    printf("Case #%d: %d\n",testcase+1,countLess(fas,B+1) - countLess(fas,A));
  }

  return 0;
}