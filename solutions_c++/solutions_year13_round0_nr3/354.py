#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <cmath>
// #include "Rational.h"

// !!! Don't forget to canonicalize() Rational's after input!
#include <gmpxx.h>
#include <gmp.h>
#define Integer mpz_class
#define Rational mpq_class
#define Float mpf_class

using namespace std;

bool debug = false;

bool test(const string &s) {
  int k, n2 = s.length();
  for (k = 0; k < n2/2; ++k)
    if (s[k] != s[n2-1 - k])
      break;
  return (k >= n2/2);
}

int main(void) {
  /*
  Integer test;
  while (true) {
    cin >> test;
    cout << test*test << "\n";
  }
  return 0;
  */


  int iTest, nTests; cin >> nTests;

  set<Integer> squares;

#if 1
  string one("1"), two("2");

  set<string> basesToDo;
  basesToDo.insert("");
  basesToDo.insert("0");
  basesToDo.insert("1");
  basesToDo.insert("2");
  basesToDo.insert("3");

  Integer maxNum(one + string(105, '0'));

  while (!basesToDo.empty()) {
    string base = *basesToDo.begin();
    basesToDo.erase(basesToDo.begin());

    if (debug) cerr << squares.size() << "\t" << base << "                                        \r";


    for (int nZeros = 0; true; ++nZeros) {
      Integer square;
      string root, zeros(nZeros, '0');

      if (!base.empty()) {
	Integer plain(base);
	square = plain*plain;
	if (test(square.get_str())) squares.insert(square);
      }

      root = one + zeros + base + zeros + one;
      Integer withOnes(root);
      square = withOnes*withOnes;
      if (square > maxNum) break;
      if (test(square.get_str()))
	basesToDo.insert(root);

      root = two + zeros + base + zeros + two;
      Integer withTwos(root);
      square = withTwos*withTwos;
      if (square > maxNum) break;
      if (test(square.get_str()))
	basesToDo.insert(root);
    }
  }

#else
  Integer i(1), iMax(10000000);
  for (; i <= iMax; ++i) {
    string s0 = i.get_str(10), s;
    int j, n = s0.length();
    
    {
      s = s0;
      s += s0;
      for (j = 0; j < n; ++j)
	s[n+j] = s[n-1 - j];
      Integer base(s);
      
      Integer square = base*base;
      string sSquare = square.get_str();
      int k, n2 = sSquare.length();
      for (k = 0; k < n2/2; ++k)
	if (sSquare[k] != sSquare[n2-1 - k])
	  break;
      if (k >= n2/2) {
	squares.insert(square);
	if (debug)
	  cerr << base << "^2 = " << sSquare << "\n";
      }
    }

    {
      s = s0;
      s += s0.substr(1);
      for (j = 0; j < n-1; ++j)
	s[n+j] = s0[n-2 - j];
      Integer base(s);
      
      Integer square = base*base;
      string sSquare = square.get_str();
      int k, n2 = sSquare.length();
      for (k = 0; k < n2/2; ++k)
	if (sSquare[k] != sSquare[n2-1 - k])
	  break;
      if (k >= n2/2) {
	squares.insert(square);
	if (debug)
	  cerr << base << "^2 = " << sSquare << "\n";
      }
    }

  }
#endif

  if (false && debug) {
    set<Integer>::iterator iSquare;
    for (iSquare = squares.begin(); iSquare != squares.end(); ++iSquare)
      cerr << *iSquare << "\n";
  }

  for (iTest = 1; iTest <= nTests; ++iTest) {
    cerr << iTest << "/" << nTests << "\n";

    Integer A, B;
    cin >> A >> B;

    cout << "Case #" << iTest << ": ";
    
    Integer count(0);
    set<Integer>::iterator it;
    for (it = squares.begin(); it != squares.end(); ++it)
      if (*it >= A && *it <= B)
	++count;
      else if (*it > B) 
	break;

      cout << count;
    
    cout << "\n";
  }

  return 0;
}
