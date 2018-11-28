#include <iostream>
#include <vector>
#include <string>

using namespace std;

int encode(string str) {
  int len = str.size();
  int r = 1;
  for(int i = 1; i < len; ++i) {
    if(str[i] != str[i - 1]) {
      ++r;
    }
  }
  return r;
}

int num_flips(int k) {
  return k - 1;
}

int main(void) {
  int T;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    string line;
    cin >> line;
    line.push_back('+');
    int r = num_flips(encode(line));
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
