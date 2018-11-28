#include <iostream>
#include <map>
#include <bitset>
#include <cmath>
#include <vector>

using namespace std;

map<long long, long long> divisor; // =-1 if key is a prime

long long find_divisor(long long x) {
  if (divisor.count(x)) {
    return divisor[x];
  }

  for (long long i = 2; i <= sqrt(x); i++) {
    if (x % i == 0) {
      divisor[x] = i;
      return i;
    }
  }

  divisor[x] = -1;
  return -1;
}

long long convert_to_base(string binary, int base) {
  long long converted = 0;
  for (int i = 0; i < binary.length(); i++) {
    converted += (binary[i] - '0') * pow(base, binary.length() - i - 1);
  }

  return converted;
}

int main () {
  int N = 16;
  int J = 50;

  int j = 0; // number of coinjams found.

  cout << "Case #1:" << endl;
  // permute the binary strings, see if it's a jamcoin.
  for (int i = pow(2, N-1)+1; i < pow(2, N); i+=2) {
    bitset<16> coin(i);
    // cout << coin.to_string() << endl;
    vector<int> K(11, 0);
    bool is_jam = true;

    for (int base = 2; base <= 10; base++) {
      long long k = find_divisor(convert_to_base(coin.to_string(), base));
      if (k != -1) {
        K[base] = k;
      } else {
        is_jam = false;
        break;
      }
    }

    if (is_jam) {
      cout << coin.to_string() << " ";
      for (int b = 2; b <= 10; b++) {
        cout << K[b] << " ";
      }
      cout << endl;
      j++;
      if (j == J) {
        break;
      }
    }
  }
  return 0;
}