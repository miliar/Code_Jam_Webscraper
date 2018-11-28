#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

void gen(int x, int J) {
  for(int i = 0; i < x; i+=2) {
    for(int j = 1; j < x; j+=2) {
      cout << "1";
      for(int k = 0; k < x; k++) {
        if(k != i && k != j) {
          cout << "0";
        }else {
          cout << "1";
        }
      }
      cout << "1";
      for(int k = 3; k < 12; k++) {
        cout << " " << k;
      }
      cout << endl;
      J--;
      if(J == 0) {
        return;
      }
    }
  }
  if(J != 0) {
    for(int i = 0; i < x; i+=2) {
      for(int j = i+2; j < x; j+=2) {
        for(int k = 1; k < x; k+=2) {
          for(int l = k+2; l < x; l+=2) {
            cout << "1";
            for(int m = 0; m < x; m++) {
              if(m != i && m != j && m != k && m != l) {
                cout << "0";
              }else {
                cout << "1";
              }
            }
            cout << "1";
            for(int m = 3; m < 12; m++) {
              cout << " " << m;
            }
            cout << endl;
            J--;
            if(J == 0) {
              return;
            }
          }
        }
      }
    }
  }
}

int main() {
  int c,n,j;
  cin >> c;
  //base-odd always even
  for(int i = 0; i < c; i++) {
    cin >> n >> j;
    cout << "Case #" << i+1 << ":" << endl;
    gen(n - 2, j);
  }
}
