#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    vector<int> data;
    for (int n = 0; n < N; ++n) {
      int val;
      cin >> val;
      data.push_back(val);
    }
    int case1 = 0;
    int maxdiff = 0;
    for (int n = 1; n < N; ++n) {
      case1 += std::max(data[n-1]-data[n], 0);
      maxdiff = std::max(data[n-1]-data[n], maxdiff);
    }
    int case2 = 0;
    for (int n = 1; n < N; ++n) {
      case2 += std::min(data[n-1], maxdiff);
    }
    cout << "Case #" << t << ": " << case1 << " " << case2 << endl;
  }

  return 0;
}

