#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    vector<int> t;
    vector<int> tt;
    vector<int> r;
    int v_row;
    cin >> v_row;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        int tv;
        cin >> tv;
        if (j == v_row - 1) {
          t.push_back(tv);
        }
      } 
    }
    cin >> v_row;
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        int tv;
        cin >> tv;
        if (j == v_row - 1) {
          tt.push_back(tv);
        }
      } 
    }
    for (int j = 0; j < 4; ++j) {
      for (int k = 0; k < 4; ++k) {
        if (t[j] == tt[k]) {
          r.push_back(t[j]);
        }
      }
    }
    cout << "Case #" << i + 1 << ": ";
    if (r.size() == 0) {
      cout << "Volunteer cheated!" << endl;
    } else if (r.size() == 1) {
      cout << r[0] << endl;
    } else {
      cout << "Bad magician!" << endl;
    }
  }
}
