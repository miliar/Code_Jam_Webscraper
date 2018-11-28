#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
  int T, prob=1;
  for (cin >> T; T--;) {
    string s;
    cin >> s;
    cout << "Case #" << prob++ << ": ";
    int eC = 0, eJ = 0, oC = 0, oJ = 0;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == 'C') ((i&1)?oC:eC) += 1;
      if (s[i] == 'J') ((i&1)?oJ:eJ) += 1;
    }
    cout << 5*s.size()/2 + min(eC, oC)*5 + min(eJ, oJ)*5 << endl;
  }
}
