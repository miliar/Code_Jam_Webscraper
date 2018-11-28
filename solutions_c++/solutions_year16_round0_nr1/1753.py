#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int count(int a) {
  bool ten[10];
  for(int i = 0; i < 10; i++) {
    ten[i] = false;
  }
  for(int i = a; i > 0; i += a) {
    int x = i;
    for(int j = 10; j <= i * 10; j *= 10) {
      int digit = (x % j) / (j / 10);
      x = x - digit * j / 10;
      if(ten[digit] == false) {
        ten[digit] = true;
      }
      bool all = true;
      for(int k = 0; k < 10; k++) {
        if(ten[k] == false) {
          all = false;
          break;
        }
      }
      if(all) {
        return i;
      }
    }
  }
}

int main() {
  int c;
  cin >> c;
  for(int i = 0; i < c; i++) {
    int x;
    cin >> x;
    cout << "Case #" << i+1 << ": ";
    if(x == 0) {
      cout << "INSOMNIA" << endl;
    }else {
      cout << count(x) << endl;
    }
  }
}
