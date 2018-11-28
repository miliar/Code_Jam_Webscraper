#include <iostream>
#include <vector>

using namespace std;

int main() {
  int numCase;
  cin >> numCase;
  
  for(int i=1; i <= numCase; i++) {
    int a1, b1, c1, d1, a2, b2, c2, d2;
    for(int k=0; k < 2; k++) {
      int target;
      cin >> target;

      for(int j=1; j <= 4; j++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        if(target == j) {
          if(k % 2 == 0) {
            a1 = a;
            b1 = b;
            c1 = c;
            d1 = d;
          }else {
            a2 = a;
            b2 = b;
            c2 = c;
            d2 = d;
          }
        }
      }
    }

    vector<int> data;
    if(a1 == a2 || a1 == b2 || a1 == c2 || a1 == d2) {
      data.push_back(a1);
    }
    if(b1 == a2 || b1 == b2 || b1 == c2 || b1 == d2) {
      data.push_back(b1);
    }
    if(c1 == a2 || c1 == b2 || c1 == c2 || c1 == d2) {
      data.push_back(c1);
    }
    if(d1 == a2 || d1 == b2 || d1 == c2 || d1 == d2) {
      data.push_back(d1);
    }

    cout << "Case #" << i << ": ";
    if(data.size() == 1) {
      cout << data[0] << endl;
    }else if(data.size() >= 2) {
      cout << "Bad magician!" << endl;
    }else if(data.size() == 0) {
      cout << "Volunteer cheated!" << endl;
    }
  }
}
