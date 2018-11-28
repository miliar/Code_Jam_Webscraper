#include <iostream>
#include <string>

using namespace std;

int
main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int smax;
    string shL;
    cin >> smax >> shL;
    int level;
    int peInL;
    int stUpPe = 0;
    int peToInvForCase;
    int peToInv = 0;
    for (int j = 0; j < smax + 1; ++j) {
      level = j;
      peInL = shL[level] - '0';
      peToInvForCase = 0;
      if (level > 0 && peInL > 0) {
        if (stUpPe < level) { 
          peToInvForCase = (level - stUpPe);
          peToInv += peToInvForCase;
        }
      }
      stUpPe += (peToInvForCase + peInL);
    }
    cout << "Case #" << i + 1 << ": " << peToInv << endl;
  }
  return 0;
}
