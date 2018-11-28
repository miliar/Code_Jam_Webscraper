//Solves Small case only

#include <iostream>

using namespace std;

int main() {
  int loops;
  cin >> loops;

  for(int loop = 1; loop <= loops; loop++) {

    int k, c, s;
    cin >> k >> c >> s;

    //note k == s

    cout << "Case #" << loop << ":";

    for(int i = 1; i <= k; i++) {
      long long int loc = i;
      for(int rep = 1; rep < c; rep++) {
        loc = ((loc - 1) * k) + i;
      }
      cout << " " << loc;
    }

    cout << endl;

  }
}