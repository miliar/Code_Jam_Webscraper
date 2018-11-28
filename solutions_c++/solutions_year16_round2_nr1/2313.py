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

int findAndDelete(char *s, char c, int countMax) {
  if (countMax == 0)
    return 0 ;
  int count = 0 ;
  int i ;
  int outi = 0 ;
  for (i = 0 ; s[i] != 0 ; i++) {
    if ((s[i] == c)&&(count<countMax)) {
      count++ ;
    }
    else {
      s[outi] = s[i];
      outi++ ;
    }
  }
  s[outi] = 0 ;
  return count ;
}

////////////////////////////////////////////////////////
// Main program here:

int runTest() {
  char s[2048];
  cin >> s ;
  int digitCounts[10] = {0,0,0,0,0,0,0,0,0,0};
  digitCounts[0] = findAndDelete(s,'Z',2048);
  findAndDelete(s,'E',digitCounts[0]);
  findAndDelete(s,'R',digitCounts[0]);
  findAndDelete(s,'O',digitCounts[0]);
  digitCounts[2] = findAndDelete(s,'W',2048);
  findAndDelete(s,'T',digitCounts[2]);
  findAndDelete(s,'O',digitCounts[2]);
  digitCounts[4] = findAndDelete(s,'U',2048);
  findAndDelete(s,'F',digitCounts[4]);
  findAndDelete(s,'O',digitCounts[4]);
  findAndDelete(s,'R',digitCounts[4]);
  digitCounts[5] = findAndDelete(s,'F',2048);
  findAndDelete(s,'I',digitCounts[5]);
  findAndDelete(s,'V',digitCounts[5]);
  findAndDelete(s,'E',digitCounts[5]);
  digitCounts[6] = findAndDelete(s,'X',2048);
  findAndDelete(s,'I',digitCounts[6]);
  findAndDelete(s,'S',digitCounts[6]);
  digitCounts[7] = findAndDelete(s,'V',2048);
  findAndDelete(s,'S',digitCounts[7]);
  findAndDelete(s,'E',digitCounts[7]*2);
  findAndDelete(s,'N',digitCounts[7]);
  digitCounts[8] = findAndDelete(s,'G',2048);
  findAndDelete(s,'E',digitCounts[8]);
  findAndDelete(s,'I',digitCounts[8]);
  findAndDelete(s,'H',digitCounts[8]);
  findAndDelete(s,'T',digitCounts[8]);
  digitCounts[3] = findAndDelete(s,'H',2048);
  findAndDelete(s,'T',digitCounts[3]);
  findAndDelete(s,'R',digitCounts[3]);
  findAndDelete(s,'E',digitCounts[3]*2);
  digitCounts[9] = findAndDelete(s,'I',2048);
  digitCounts[1] = (strlen(s) - digitCounts[9]*3)/3 ;
  
  cout << "Case #" << caseNumber << ": " ;

  int i;
  for (i = 0 ; i < 10 ; i++) {
    int j ;
    for (j = 0 ; j < digitCounts[i] ; j++) {
      cout << i ;
    }
  }
  
  cout << "" << endl ;
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
