#include <iostream>
#include <stdio.h>    /* printf */
#include <string.h>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; ++t) {
    int Smax;
    string shyness;
    cin >> Smax >> shyness;
    int stand = 0;
    int mnf = 0;
    for (int i=0; i<shyness.length(); ++i) {
      char k1 = shyness[i];
      int k = k1 - '0';
      if ( i != 0 && stand < i ) {
        mnf += i-stand;
        stand += i-stand;
      }
      stand += k;
    }
    printf("Case #%i: %i\n", t, mnf);
  }
  return 0;
}
