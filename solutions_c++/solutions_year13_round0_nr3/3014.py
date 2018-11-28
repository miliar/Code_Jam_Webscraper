// Google CodeJam 2013 Qualifying Round B
// dom7b5

// Uses GMPxx for big integer capability.

#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <memory>
#include <gmpxx.h>

using namespace std;

/* Determine if the given big integer is a palindrome. */
bool palindrome(mpz_class n)
{
  stringstream ss;
  string s;
  ss << n;
  s = ss.str();
  int a = 0;
  int b = s.size();
  int count = b / 2;
  for (int i = 0; i < count; ++i) {
    if (s[a++] != s[--b]) {
      return false;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  int ncases = 0;
  mpz_class a, b, u, v, i, ii;
  int count = 0;
  cin >> ncases;
  for (int cs = 0; cs < ncases; ++cs) {
    cin >> a >> b;
    /* check the roots first, then square */
    u = sqrt(a);
    v = sqrt(b);
    count = 0;
    for (i = u; i <= v; ++i) {
      if (palindrome(i)) {
	ii = i * i;
	/* sqrt(mpz) will return something lower than what we
	   want in cases where its not an integer root, so just
	   check again on both sides to make sure we are properly
	   constrained. */
	if (ii >= a && ii <= b && palindrome(ii)) {
	  ++count;
	}
      }
    }
    cout << "Case #" << (cs + 1) << ": " << count << endl;
  }
}
