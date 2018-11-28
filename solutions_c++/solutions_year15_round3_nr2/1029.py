// 2015 code jam round 1C Problem B
int v = 0 ;

#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <array>
#include <math.h>
#include <iomanip>

using namespace std ;

int caseNumber;

int runTest() {
  int k, l,s;
  cin >> k >> l >> s ;
  string keyboard ;
  cin >> keyboard ;
  string word ;
  cin >> word ;
  if (v)
    cout << "Keyboard: '" << keyboard << "', word: '" << word << "'" << endl ;
  int i,j ;
  int letterCount['Z'+1];
  char c ;
  for (c = 'A' ; c <= 'Z' ; c++) {
    letterCount[c] = 0 ;
  }
  int differentLetters = 0 ;
  for (j = 0 ; j < keyboard.length() ; j++) {
    if (!letterCount[keyboard[j]])
      differentLetters++;
    letterCount[keyboard[j]]++;
  }
  long long int combin = 1 ;
  for (i = 0 ; i < word.length() ; i++) {
    combin *= letterCount[word[i]];
  }
  if (combin == 0) {
    cout << "Case #" << caseNumber << ": " << 0 << endl ;
    return 1 ;
  }
  if (differentLetters == 1) {
    cout << "Case #" << caseNumber << ": " << 0 << endl ;
    return 1 ;
  }
    
  int longestOverlap = 0 ;
  for (i = 1 ; i < l ; i++) {
    string s1 = word.substr(0,i);
    string s2 = word.substr(l-i,i);
    if (s1 == s2)
      longestOverlap = i ;
  }
  if (v)
    cout << "longest overlap: " << longestOverlap << endl ;
  
  int maxBananas = s / l ;
  if (longestOverlap) {
    maxBananas = (s - longestOverlap) / (l-longestOverlap);
  }
  if (v)
    cout << "max Bananas: " << maxBananas << endl ;
  long long int ways = 1 ;
  for (i=1 ; i <= l ; i++)
    ways *= k ;
  if (v)
    cout << "Combin: " << combin << " Ways: " << ways << endl ;
  long double ev = ((long double)(s+1-l))*combin/ways ;
  long double evkeep = (long double)maxBananas - ev ;
  cout << "Case #" << caseNumber << ": " << setprecision(9) << evkeep << endl ;
  
  return 1 ;
}

int main (int argc, const char * argv[])
{
  int testCases ;
  cin >> testCases ;
  if (v) {
    cerr << "Verbose is on!" << endl ;
    cout << "// Test cases: " << testCases << endl ;
  }
  for (caseNumber=1 ; caseNumber <= testCases ; caseNumber++) {
    if (v)
      cout << "// Running case #" << caseNumber << endl ;
    int r = runTest();
    if (!r) {
      cerr << "test failed!" << endl ;
    }
  }
  return 0;
}

