#include <iostream>

using namespace std;

const int ALL_DIGITS_SEEN = 0x3FF; // 0011 1111 1111

int digits_in_number(long long i) {
  if (i == 0) {
    return 0x0000000001;
  }

  int digits_seen = 0x0;
  while (i > 0) {
    int digit = i % 10;
    // cout << "digit " << digit << endl;
    // cout << "combining " << digits_seen << " and " << (1 << digit) << endl;
    digits_seen = digits_seen | (1 << digit);
    i = i / 10;
  }

  return digits_seen;
}

long long solve(long long N) {
  if (N == 0) {
    return -1;
  }

  int digits_seen = 0x0;
  for (long long i = N; i <= LLONG_MAX-N; i += N) {
    digits_seen = digits_seen | digits_in_number(i);
    // cout << "i " << i << " digits_seen " << digits_seen << endl;
    if (digits_seen == ALL_DIGITS_SEEN) {
      return i;
    }
  }
  return -1;
}

int main() {
  int num_cases;
  cin >> num_cases;
  long long N;
  for (int i = 0; i < num_cases; i++) {
    cin >> N;
    long long solution = solve(N);
    cout << "Case #" << i+1 << ": ";
    if (solution == -1) {
      cout << "INSOMNIA";
    } else {
      cout << solution;
    }
    cout << endl;
  }
}

/*
1 2 3 4 5 6 7 8 9
2 4 6 8 10 12
3 6 9 12 15 18 21
23 46 69 92 115 138 161
32 64 96 128 160
*/