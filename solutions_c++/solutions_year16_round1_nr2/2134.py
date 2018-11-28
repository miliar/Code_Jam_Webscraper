#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (size_t t = 0; t < T; ++t) {
    int N;
    cin >> N;
    int used[2500];
    for (size_t i = 0; i < 2500; ++i) used[i] = 0;

    for (size_t i = 0; i < (2 * N) - 1; ++i) {
      for (size_t j = 0; j < N; ++j) {
        int val;
        cin >> val;
        used[val] += 1;
      }
    }

    vector<int> out;
    out.reserve(N);

    for (size_t i = 0; i < 2500; ++i) {
      if ((used[i] % 2) == 1) {
        out.push_back(i);
      }
    }
    sort(out.begin(), out.end());

    cout << "Case #" << (t + 1) << ": ";
    for (const auto &it : out) {
      cout << it << " ";
    }
    cout << endl;
  }
  return 0;
}
