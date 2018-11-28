#include <iostream>
#include <vector>
#include <algorithm>
#include <assert.h> 
using namespace std;

const int kMAX = 2500;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    int h;
    vector<int> index(kMAX + 1, 0);
    for (int i = 0; i < 2 * N - 1; ++i) {
      for (int j = 0; j < N; ++j) {
        cin >> h;
        index[h]++;
      }
    }
    vector<int> m;
    for (int k = 0; k <= kMAX; ++k) {
      if (index[k] % 2 == 1) m.push_back(k);
    }
    sort(m.begin(), m.end());
    
    cout << "Case #" << t << ":";
    for (int k = 0; k < N; ++k) {
      cout << " " << m[k];
    }
    cout << endl;
  }
}
