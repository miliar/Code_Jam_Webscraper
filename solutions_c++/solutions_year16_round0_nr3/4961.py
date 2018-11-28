#include <iostream>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

map<int, map<string, vector<uint64_t>>> nums;

uint64_t as_base(string bin, int base) {
  uint64_t total = 0;
  reverse(bin.begin(), bin.end());
  for (int i = 0; i < bin.length(); i++) {
    if (bin[i] == '1') {
      total += (uint64_t) pow(base, i);
    }
  }
  return total;
}

uint64_t first_divisor(uint64_t num) {
  for (uint64_t i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      return i;
    }
  }
  return 0;
}

void gen_nums(int current, int limit, string built) {
  if (current == limit - 1) {
    vector<uint64_t> representations;
    built += '1';
    for (int i = 2; i <= 10; i++) {
      uint64_t num = as_base(built, i);
      uint64_t first = first_divisor(num);
      if (first == 0) {
        break;
      }
      representations.push_back(first);
    }
    if (representations.size() == 9) {
      if (nums.find(limit) == end(nums)) {
        nums[limit] = map<string, vector<uint64_t>>{};
      }
      nums[limit][built] = representations;
    }
  } else {
    gen_nums(current+1, limit, built+'1');
    if (current != 0) {
      gen_nums(current+1, limit, built+'0');
    }
  }
}

int main() {
  int t;
  cin >> t;
  uint64_t n, j;
  cin >> n >> j;
  for (int i = 2; i <= n; i++) {
    cerr << "i = " << i << endl;
    gen_nums(0, i, "");
  }
  cout << "Case #1:" << endl;
  auto results = nums[n];
  int k = 0;
  for (auto result : results) {
    cout << result.first;
    for (uint64_t current : result.second) {
      cout << " " << current;
    }
    cout << endl;
    k++;
    if (k >= j) {
      return 0;
    }
  }
}
