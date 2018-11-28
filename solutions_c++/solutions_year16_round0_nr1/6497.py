#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool seen[10];

void update (int n){
  //int testn = n;
  bool testChange = false;

  while (n >= 10) {
  //  if (!seen[n%10] && !testChange) testChange = true;

    seen[n%10] = true;
    n /= 10;
  }

  //if (!seen[n] && !testChange) testChange = true;

  seen[n] = true;

  //if (testChange) cout << testn << endl;
}

int main () {
  int t,n;

  //int testhigh = 0;

  cin >> t;

  for (int aa = 0; aa < t; aa ++) {
    cin >> n;
    //n = aa+1;

    cout << "Case #" << aa+1 << ": ";

    for (int i = 0; i < 10; i ++) {
      seen[i] = false;
    }

    bool done = false;
    for (int i = 1; i < 1000 && n != 0; i ++) {
      //cout << n*i << endl;
      update (n*i);
      done = true;
      for (int j = 0; j < 10; j++) {
        if (!seen[j]) {
          done = false;
          break;
        }
      }
      if (done) {
        cout << n*i << endl;
        //cout << i << endl;
        //testhigh = max (testhigh,i);
        break;
      }
    }

    if (!done) {
      cout << "INSOMNIA" << endl;
    }

  }
  //cout << testhigh << endl;
}
