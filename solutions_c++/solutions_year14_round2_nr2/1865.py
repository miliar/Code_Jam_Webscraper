#include <iostream>
#include <algorithm>
using namespace std;

int Z, A, B, K;

void read();
void solve(int);

int main() {
  cin >> Z;
  for (int zi = 1; zi <= Z; ++zi)
    read(), solve(zi);

  return 0;
}

void read() {
  cin >> A >> B >> K;
}

void solve(int zi) {
  int res = 0;

  for (int i = 0; i < A; ++i)
    for (int j = 0; j < B; ++j)
      if ((i & j) < K)
        ++res;

  cout << "Case #" << zi << ": " << res << "\n";
}
