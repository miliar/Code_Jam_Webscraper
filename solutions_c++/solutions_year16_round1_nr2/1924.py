#include <iostream>
#include <vector>

using namespace std;

int main(){
  int t, n, v;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    cin >> n;
    auto xs = vector<int>(2501, 0);
    for (int j = 0; j < 2*n - 1; ++j) {
      for (int k = 0; k < n; ++k) {
        cin >> v;
        ++xs[v];
      }
    }
    cout << "Case #" << (i + 1) << ":";
    for (int j = 1; j <=2500; ++j) {
      if (xs[j] % 2 == 0) {
          continue;
      }
      cout << " " << j;
    }
    cout << endl;
  }
}
