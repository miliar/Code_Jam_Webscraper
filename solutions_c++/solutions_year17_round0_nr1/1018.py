// 2014 code jam round 1 Problem A
int v = 0 ;

#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <map>
#include <set>
#include <bitset>
using namespace std ;

typedef long long int ll;

int caseNumber ;


////////////////////////////////////////////////////////
// Main program here:

int runTest() {
  char s[2048];
  cin >> s ;
  
  ll k ;
  cin >> k ;
  
  cout << "Case #" << caseNumber << ": " ;

  ll flips = 0 ;
  ll i;
  ll n = strlen(s) - k + 1 ;
  
  for (i = 0; i < n ; i++) {
    if (s[i] == '-') {
      flips++;
      ll j ;
      for (j = 0 ; j < k ; j++) {
        if (s[i+j] == '-')
          s[i+j] = '+';
        else
          s[i+j] = '-';
      }
    }
  }
  ll possible = 1 ;
  for (i = n ; i < n+k ; i++) {
    if (s[i] == '-') {
      possible = 0 ;
      break ;
    }
  }
  if (possible)
    cout << flips << endl ;
  else
    cout <<  "IMPOSSIBLE" << endl ;
  return 1 ;
}

////////////////////////////////////////////////////////

int main (int argc, const char * argv[])
{
  int testCases ;
  //testxor();
  cin >> testCases ;
  if (argc > 1) {
    if (argv[1][0] == 'v')
      v = 1 ;
  }
  if (v) {
    cerr << "Verbose is on!" << endl ;
    cout << "// Test cases: " << testCases << endl ;
  }
  for (caseNumber=1 ; caseNumber <= testCases ; caseNumber++) {
    //if (caseNumber > 11) v = 1;
    if (v)
      cout << "// Running case #" << caseNumber << endl ;
    int r = runTest();
    if (!r) {
      cerr << "test failed!" << endl ;
    }
  }
  return 0;
}
