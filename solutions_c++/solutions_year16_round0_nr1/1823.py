#include <iostream>
#include <vector>

using namespace std;

void UpdateSeenDigits(int candidate, vector<bool>* seen_digits) {
  while (candidate > 0) {
    int digit = candidate % 10;
    (*seen_digits)[digit] = true;
    candidate = candidate / 10;
  }
}

bool SeenAllDigits(const vector<bool>& seen_digits) {
  for (int i = 0; i < 10; ++i) {
    if (!seen_digits[i]) return false;
  }
  return true;
}

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    vector<bool> seen_digits;
    for (int j = 0; j < 10; ++j) {
      seen_digits.push_back(false);
    }
    int candidate = N;
    int j = 1;
    for (; j < 1000000; ++j) {
      UpdateSeenDigits(j * candidate, &seen_digits);
      if (SeenAllDigits(seen_digits)) break;
    }
    if (j < 1000000) {
      cout << "Case #" << i << ": " << j * candidate << endl;
    } else {
      cout << "Case #" << i << ": INSOMNIA" << endl;
    }
  }
  return 0;
}
        
