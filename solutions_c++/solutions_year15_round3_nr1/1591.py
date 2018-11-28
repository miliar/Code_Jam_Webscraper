#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
typedef int32_t T;

T R, C, W;

T solve() {


  return (C-1)/W + W;
}

int main() {
  vector<T> result;
  int tests;

  cin >> tests;
  for (int t=0; t<tests; t++) {
    cin >> R >> C >> W;
    assert(R==1);
    result.push_back(solve());
  }

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i] << "\n";
  }
  return 0;
}
