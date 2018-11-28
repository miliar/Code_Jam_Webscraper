#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int A, B, K;
    cin >> A >> B >> K;
    int result = 0;
    for (int a = 0; a < A; ++a) {
      for (int b = 0; b < B; ++b) {
        if ((a&b) < K) ++result;
      }
    }
    cout << "Case #" << t << ": " << result << endl;
  }
}
