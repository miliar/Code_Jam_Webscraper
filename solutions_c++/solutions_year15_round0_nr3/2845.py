#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

typedef long long int lli;

// 'i' == 2
// 'j' == 3
// 'k' == 4

char matrix[4][4] = {
  { 1,  2,  3,  4},
  { 2, -1,  4, -3},
  { 3, -4, -1,  2},
  { 4,  3, -2, -1}
};

char multiply(char a, char b)
{
  char r = 1;
  if (a < 0) { r *= -1; a *= -1; }
  if (b < 0) { r *= -1; b *= -1; }
  return r * matrix[ a-1 ][ b-1 ];
}

bool solve(lli L, lli X, string& s)
{
  // preprocess
  for (lli i = 0; i < L; ++i) if (s[i] >= 'i') s[i] -= 'g';

  // i * j * k = -1 ?
  char mul = s[0];
  for (lli i = 1; i < L; ++i) mul = multiply( mul, s[i] );

  if (mul == 1) {
    return false;
  } else if (mul == -1) {
    if (X % 2 == 0) return false;
  } else if ((X % 2) != 0 || (X % 4) == 0) { // i, j or k
    return false; 
  }

  //////////////////////////////

  map<char, string> front_cache, back_cache;
  for (char c = -4; c <= 4; ++c) {
    // build front cache
    string cache = s;
    for (lli i = 0; i < L; ++i) {
      if (i > 0)         cache[i] = multiply( cache[i-1], cache[i] );
      else if ( c != 0 ) cache[i] = multiply( c         , cache[i] );
    }
    front_cache[c] = cache;
    // build back cache
    cache = s;
    for (lli i = L; i > 0; --i) {
      if (i < L)         cache[i-1] = multiply( cache[i-1], cache[i] );
      else if ( c != 0 ) cache[i-1] = multiply( cache[i-1], c        );
    }
    back_cache[c] = cache;
  }

  // for (lli z = 0; z < L; ++z) cout << int(front_cache[0][z]) << " ";
  // cout << endl;
  //////////////////////////////

  // find 'i'
  lli total = L * X;
  lli i = 0;
  char c = 0;
  while (i < total) {
    char last = front_cache[c][i % L];
    if (last == 2) break; // we found 'i'
    ++i;
    if (i % L == 0) c = last;
  }

  // find 'k'
  lli k = total-1;
  c = 0;
  while (k >= 0) {
    char last = back_cache[c][k % L];
    if (last == 4) break; // we found 'k'
    --k;
    if (k % L == 0) c = last;
  }
  return (i < k);
}

int main (int argc, char *argv[])
{
  int T;
  lli L, X;
  vector<int> diners;
  string s;
  cin >> T;
  for(int i = 0; i<T; ++i) {
    cin >> L >> X >> s;
    cout << "Case #" << i+1 << ": ";
    cout << (solve(L, X, s) ? "YES" : "NO");
    cout << endl;
  }

  return 0;
}

