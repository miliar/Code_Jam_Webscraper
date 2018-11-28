#include <iostream>
using namespace std;

int main() {
  int nTest;
  cin >> nTest;
  
  bool ok[16];
  for (int iTest = 1; iTest <= nTest; iTest++) {
    cout << "Case #" << iTest << ": ";
    for (int i = 1; i <= 16; i++) ok[i] = true;
    int r1, r2;
    
    cin >> r1;
    for (int i = 1; i <= 16; i++) {
      int x;
      cin >> x;
      if ((i - 1) / 4 != r1 - 1) ok[x] = false;
    }

    cin >> r2;
    for (int i = 1; i <= 16; i++) {
      int x;
      cin >> x;
      if ((i - 1) / 4 != r2 - 1) ok[x] = false;      
    }

    int cnt = 0;
    for (int i = 1; i <= 16; i++) if (ok[i]) cnt++;
      
    if (cnt == 0) {
      cout << "Volunteer cheated!" << endl;    
    } else if (cnt > 1) {
      cout << "Bad magician!" << endl;    
    } else {
      for (int i = 1; i <= 16; i++) if (ok[i]) cnt = i;
        cout << cnt << endl;
    }
  }
  
  return 0;
}