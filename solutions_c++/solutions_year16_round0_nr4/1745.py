#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;
  for(int i = 0; i < t; i++) {
    cout << "Case #" << i+1 << ": ";
    int k,c,s;
    int req;
    cin >> k >> c >> s;
    if(c >= 2) {
      req = k / 2 + 1;
    }else {
      req = k;
    }
    if(req > s) {
      cout << "IMPOSSIBLE" << endl;
    }else {
      if(c == 1) {
        for(int j = 1; j <= k; j++) {
          cout << j;
          if(j == k) {
            cout << endl;
          }else {
            cout << " ";
          }
        }
      }else {
        for(int j = 1; j <= k; j += 2) {
          if(j != k) {
            cout << (j - 1) * k + (j + 1);
          }else {
            cout << k;
          }
          if(j == k || k - j == 1) {
            cout << endl;
          }else {
            cout << " ";
          }
        }
      }
    }
  }
}
