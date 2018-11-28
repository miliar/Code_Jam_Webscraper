#include <iostream>
#include <vector>

using namespace std;

bool all(const vector<bool>& v) {
  for (const auto b : v) {
    if (!b) {
      return false;
    }
  }
  return true;
}

void processDigits(uint64_t x, vector<bool>& v) {
  while (x > 0) {
    auto lastDigit = x % 10;
    v[lastDigit] = true;
    x /= 10;
  }
}

uint64_t solve(uint64_t n) {
  vector<bool> digitSeen(10, false);
  int i;
  for (i = 1; !all(digitSeen); ++i) {
    processDigits(i * n, digitSeen);
  }
  return (i-1) * n;
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    uint64_t N;
    cin >> N;
    cout << "Case #" << t << ": ";
    if (N == 0) {
      cout << "INSOMNIA"; 
    } else {
      cout << solve(N);
    }
    cout << '\n';
  }

  return 0;
}
