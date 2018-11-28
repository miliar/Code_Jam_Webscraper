#include <iostream>
#include <vector>
#include <string>
#include "string.h"
using namespace std;


int main(int argc, char const *argv[]) {
  int count;
  cin >> count;
  string buf;
  int mark[150];
  int mark2[150][150];
  int flag = 0;
  int n, total, l;
  for(int i = 0; i < count; ++i) {
    cin >> buf >> n;
    l = buf.length();
    total = 0;
    memset(mark, 0, sizeof(mark));
    memset(mark2, 0, sizeof(mark2));
    for(int j = 0; j < l - n + 1; ++j) {
      flag = 1;
      for(int k = 0; k < n; ++k) {
        if(buf[j+k] == 'a' ||
           buf[j+k] == 'e' ||
           buf[j+k] == 'i' ||
           buf[j+k] == 'o' ||
           buf[j+k] == 'u') {
          flag = 0;
          break;
        }
      }
      if (flag == 1) {
        for(int k = 0; k <= j; ++k) {
          for(int m = j + n; m <= l; ++m) {
            mark2[k][m-1] = 1;
          }
        }
      }
    }
    for(int j = 0; j < l;++j) {
      for(int k = 0;k < l;++k) {
        // cout << mark2[j][k] << " ";
        total += mark2[j][k];
      }
      // cout << endl;
    }
    cout <<"Case #" << i+1 << ": " << total;
    if(i +1 != count) {
      cout <<endl;
    }
  }
  return 0;
}
