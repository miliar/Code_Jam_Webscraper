#include <iostream>
#include <string>
using namespace std;

int main() {
  int Z;
  cin >> Z;
  for (int z = 1; z <= Z; ++z) {
    int n;
    string t;
    cin >> n >> t;
    int sum = 0;
    int max_diff = 0;
    for (int i = 0; i <= n; ++i) {
      max_diff = max(max_diff, i - sum);
      sum += (t[i] - '0');
    }
    cout << "Case #" << z << ": " << max_diff << endl;
  }
}
