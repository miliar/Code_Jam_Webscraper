#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool CheckAllDigits(const vector<bool>& digits) {
  for (int i = 0; i < 10; i++) {
    if (digits[i] == false) return false;
  }
  return true;
}

void UpdateDigits(vector<bool>& digits, int n) {
  while (n != 0) {
    int last_digit = n % 10;
    digits[last_digit] = true;
    n /= 10;
  }
}

int ComputeLastNumber(int n, bool* ok) {
  vector<bool> digits;
  digits.resize(10);
  for (int i = 0; i < 10; i++) {
    digits[i] = false;
  }

  int i = 1;
  do {
    int current_n = n*i;
    UpdateDigits(digits, current_n);
    int next_n = n*(i+1);
    if (current_n == next_n) {
      *ok = false;
      return -1;
    }
    i++;
  } while (!CheckAllDigits(digits));

  *ok = true;
  return n*(i-1);
}


int main(int argc, char** argv) {
  int nb_test;
  cin >> nb_test;
  for (int i = 1; i <= nb_test; ++i) {
    int n;
    cin >> n;
    bool ok = true;
    int res = ComputeLastNumber(n, &ok);
    cout << "Case #" << i << ": ";
    if (ok) cout << res;
    else  cout << "INSOMNIA";
    cout << endl;
  }
}
