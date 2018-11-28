#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>


using namespace std;

bool is_palindrome(unsigned long int n) {
  char s[101];
  sprintf(s, "%lu", n);
  int l = strlen(s) - 1;
  for (int i=0; i<=l; ++i, --l)
    if (s[i] != s[l]) return false;

  return true;
  


}

int main() {
  
  unsigned long int a=1; 
  unsigned long int b=(unsigned long int)floor(sqrt((float)100000000000000));
  
  vector<unsigned long int> fas;
 

  for (unsigned long int n=a; n<=b; ++n) 
      if (is_palindrome(n) && is_palindrome(n*n))
	fas.push_back(n*n);
  
  int T;

  cin >> T;

  for (int t=1; t<=T; ++t) {
    unsigned long int A, B;

    cin >> A >> B;

    int np=0;
    int i;
    for (i=0; i<fas.size(); ++i) {
      if (fas[i]>B) { cout << "Case #" << t <<": " << np << endl; break; }
      if (fas[i]>=A) np++;
    }

    if ( i==fas.size() ) cout << "Case #" << t <<": " << np << endl;

  }
  

  
  return 0;

}
