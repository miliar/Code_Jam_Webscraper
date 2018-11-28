#include <iostream>
#include <string>

using namespace std;

string s, v;
int k, l;
char kk;

int main() {
  int t; cin >> t;

  for(int tc = 1; tc <= t; tc++) {
    cin >> s;

    l = s.length();
    v = "\0";

    for (k = 0; k < l; k++) {
      kk = s[k];

      if (v == "") {
        v = v + kk;
      } else {
        if (kk >= v[0]) {
          v = kk + v;
        } else {
          v = v + kk;
        }
      }
    }

    v[k] = '\0';

    cout << "Case #" << tc << ": " << v << endl;
  }
  
  return 0;
}
