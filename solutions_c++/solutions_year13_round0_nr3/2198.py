#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <istream>
#include <ostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <string.h>
#include <strings.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <cassert>
#include <assert.h>
#include <bitset>
#include <functional>
#include <utility>
#include <iomanip>
#include <cctype>
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

typedef unsigned long long ull;

#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)

//////////////////////////////////////////////////////////////////////////

bool is_palindrome (ull nb) {
  vector<int> digits;
  assert (nb > 0);
  while (nb > 0) {
    digits.push_back (nb % 10);
    nb /= 10;
  }
  int n = digits.size();
  FOR(i, 0, n / 2) {
    if (digits[i] != digits[n - 1 - i])
      return false;
  }
  return true;
}

ull mysqrt (ull nb) {
  //return (ull) floor(sqrt((double)nb));/* 52 bits of mantissa should be enough for 10^14... but I hate double! */
  ull s;
  for (s = 0; s*s <= nb; s++); /* at most 10^(14/2) iterations */
  assert (s - 1 == (ull) floor(sqrt((double)nb)));
  return s - 1;    
}

int main (int argc, char* argv[]) {

  ifstream in (argv[1]);
  ofstream out ("problem.out");
  string line;
  int nbTests;
  out.precision(12);

  in >> nbTests;
  getline(in, line);

  for (int test=0; test<nbTests; test++) {
    ull a, b, sqrta, sqrtb, i;
    ull cpt = 0;
    in >> a >> b;
    sqrta = mysqrt(a);
    sqrtb = mysqrt(b);

    for (i = sqrta; i <= sqrtb; i++) { /* I could have reduced this loop by iterating only on palindromes */
 
      assert (i*i <= b);
      if ((a <= i*i) && is_palindrome (i) && is_palindrome (i*i)) {
	cpt ++;
      }
    }
    assert (i*i > b);
    out << "Case #" << test+1 << ": " << cpt << endl;
    
  }
}

