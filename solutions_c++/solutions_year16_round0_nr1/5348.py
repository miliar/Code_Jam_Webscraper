#include <iostream>
#include <unordered_map>

using namespace std;

void mark_as_seen(long long n, bool* digits) {
  while (n > 0) {
    long long last_digit = n % 10;

    digits[last_digit] = true;

    n /= 10;
  }
}

bool has_seen_all(bool* digits) {
  for (long long i=0; i<10; i++) {
    if (digits[i] == false) {
      return false;
    }
  }

  return true;
}

void solve(long long n, int case_num) {
  bool digits[10] = {false};
  unordered_map<long long, bool> seen_numbers;

  long long i = 2;

  bool seen_all = false;

  long long current_n = n;

  do {
    mark_as_seen(current_n, digits);

    seen_all = has_seen_all(digits);

    if (seen_all) {
      cout << "Case #" << case_num << ": " << current_n << endl;
      break;
    }

    current_n = n * i++;

    if (seen_numbers.find(current_n) != seen_numbers.end()) {
      cout << "Case #" << case_num << ": INSOMNIA" << endl;
      break;
    }

    seen_numbers[current_n] = true;
  } while(true);
}

int main() {
  long long T;
  cin >> T;

  long long N;

  for (long long i=0; i<T; i++) {
    cin >> N;

    solve(N, i+1);
  }

  return 0;
}
