#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  long long T;
  cin >> T;

  for (long long ii = 1; ii <= T; ii++) {
    cout << "Case #" << ii << ": ";
    long long N, X;
    cin >> N >> X;
    long long size;
    vector<long long> files;
    for (long long jj = 0; jj < N; jj++) {
      cin >> size;
      files.push_back(size);
    }
    sort(files.begin(), files.end());
    long long ret = 0;
    while (files.size()) {
      long long i1 = files[0];
      long long i2 = files.size();
      for (int jj = files.size()-1; jj > 0; jj--) {
        if (files[0] + files[jj] <= X) {
          i2 = jj;
          break;
        }
      }
      if (i2 != files.size()) {
        files.erase(files.begin() + i2);
      }
      files.erase(files.begin());
      ret += 1;
    }
    cout << ret << endl;
  }
}
