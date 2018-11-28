#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int c;
  cin >> c;
  for(int i = 0; i < c; i++) {
    int d;
    cin >> d;
    int nums[d*d];
    int freqs[d * d];
    for(int j = 0; j < d*d; j++) {
      freqs[j] = 1;
    }
    int temp;
    int len = 0;
    for(int j = 0; j < d*(2*d-1); j++) {
      cin >> temp;
      bool found = false;
      for(int k = 0; k < len; k++) {
        if(nums[k] == temp) {
          freqs[k]++;
          found = true;
          break;
        }
      }
      if(!found) {
        nums[len] = temp;
        len++;
      }
    }
    vector<int> odds;
    for(int j = 0; j < len; j++) {
//      cerr << nums[j] << " " << freqs[j] << endl;
      if(freqs[j] % 2 == 1) {
        odds.push_back(nums[j]);
      }
    }
    cout << "Case #" << i+1 << ":";
    sort(odds.begin(), odds.end());
    for(int j = 0; j < d; j++) {
      cout << " " << odds[j];
    }
    cout << endl;
  }
}
