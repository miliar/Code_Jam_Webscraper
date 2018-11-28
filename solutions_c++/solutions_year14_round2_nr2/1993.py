#include <iostream>
#include <algorithm>

using namespace std;

typedef long long i64;

void run(istream& in, int t) {
  i64 A, B, K, ret = 0;
  in >> A >> B >> K;
  for (int i = 0; i < A; ++i) {
    for (int j = 0; j < B; ++j) {
      if ((j & i) < K) ret++;
    }
  }
  cout << "Case #" << t << ": " << ret << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    run(cin, i + 1);
  }
}
