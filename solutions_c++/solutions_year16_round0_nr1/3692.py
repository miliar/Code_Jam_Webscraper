#include <iostream>
#include <limits>
#include <bitset>

using namespace std;

const unsigned long long INSOMNIA = std::numeric_limits<unsigned long long>::max(); 
typedef bitset<10> Digits;

Digits getDigits(unsigned long long N) {
  Digits res;
  unsigned long long remainder = N;
  while (remainder != 0) {
    res.set(remainder % 10);
    remainder /= 10;
  }
  return res;
}

unsigned long long solve(unsigned long long N) {
  if (0 == N) {
    return INSOMNIA;
  }

  Digits answer = getDigits(N);
  unsigned long long current = N;
  unsigned long long multiplier = 2;
  while (!answer.all()) {
    current  = N * multiplier++;
    // cout << current << '\n';
    answer |= getDigits(current);
  }
  return current;
}

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    unsigned long long N; cin >> N;
    auto answer = solve(N);
    cout << "Case #" << i << ": ";
    if (INSOMNIA == answer) {
      cout << "INSOMNIA";
    } else {
      cout << answer;
    }
    cout << '\n';
  }
}
