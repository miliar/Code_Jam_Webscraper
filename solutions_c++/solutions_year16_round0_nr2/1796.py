#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int c;
  cin >> c;
  bool pcks[100];
  string temp;
  getline(cin, temp);
  for(int i = 0; i < c; i++) {
    getline(cin, temp);
    istringstream iss(temp);
    char x;
    int len;
    for(len = 0; iss >> x; len++) {
      if(x == '-') {
        pcks[len] = false;
      }else {
        pcks[len] = true;
      }
    }
    int times = 0;
    len--;
    while(len != -1) {
      if(pcks[len]) {
        len--;
      }else {
        if(pcks[0]) {
          int j;
          for(j = 0; pcks[j]; j++) {
            pcks[j] = false;
          }
          times++;
          bool temp[len + 1];
          for(int k = 0; k <= len; k++) {
            temp[k] = pcks[k];
          }
          for(int k = 0; k <= len; k++) {
            pcks[k] = !temp[len - k];
          }
          times++;
        }else {
          bool temp[len + 1];
          for(int k = 0; k <= len; k++) {
            temp[k] = pcks[k];
          }
          for(int k = 0; k <= len; k++) {
            pcks[k] = !temp[len - k];
          }
          times++;
        }
      }
    }
    cout << "Case #" << i+1 << ": " << times << endl;
  }
}
