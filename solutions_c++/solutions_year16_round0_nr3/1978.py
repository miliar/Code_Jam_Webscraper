#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <bitset>

using namespace std;

//const int N = 6;
//const int K = 3;
//const int N = 16;
//const int K = 50;
const int N = 32;
const int K = 500;

const int MAX_DIV = (int)1e6;

int random_mask(int n) {
  int mid = rand() % (1 << (n - 2));
  return (1 << (n - 1)) + (mid << 1) + 1;
}

bool divisible(int base, int mask, int mod) {
  int cur = 1;
  int rem = 0;
  for (int i = 0; i < N; ++i) {
    if (mask >> i & 1) {
      rem = (rem + cur) % mod;
    }
    cur = (cur * base) % mod;
  }
  return rem == 0;
}

int find_divisor(int base, int mask) {
  for (int i = 3; i <= MAX_DIV; ++i) {
    if (divisible(base, mask, i)) return i;
  }
  return -1;
}

vector<int> find_all_divisors(int mask) {
  vector<int> divs;
  for (int i = 2; i <= 10; ++i) {
    int div = find_divisor(i, mask);
    if (div == mask || div == -1) {
      return vector<int>();
    }
    divs.push_back(div);
  }
  return divs;
}

int main() {
  srand(12345);
  set<int> found;
  cout << "Case #1: " << endl;
  while (found.size() < K) {
    int mask = random_mask(N);
    if (found.count(mask)) continue;
    vector<int> divisors = find_all_divisors(mask);
    if (!divisors.empty()) {
      found.insert(mask);
      cerr << found.size() << endl;
      cout << bitset<N>(mask);
      for (int div : divisors) cout << " " << div;
      cout << endl;
    }
  }
  return 0;
}
