#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int s;
    vector<int> v;
    string sh;
    cin >> s;
    cin >> sh;
    for (int i = 0; i < sh.length(); i++) {
      v.push_back(sh[i] - '0');
    }
    int st = 0;
    int r = 0;
    for (int i = 0; i < v.size(); i++) {
      if (v[i] != 0) {
        if (st >= i) {
          st += v[i];
        } else {
          int add = i - st;
          r += add;
          st += add + v[i];
        }
      }
    }
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
