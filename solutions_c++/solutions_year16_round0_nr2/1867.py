#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

using int64 = long long;

void run() {
  string input;
  getline(cin, input);
  int total = 0;
  for (size_t i = 0; i < input.length() - 1; ++i) {
    if (input[i] != input[i + 1]) {
      total += 1;
    }
  }
  int parity = (input[0] == '+') ? 0 : 1;
  if ((parity + total) % 2 == 1) {
    total += 1;
  }
  cout << total;
  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  int cases;
  cin >> cases;
  string dummy;
  getline(cin, dummy);
  for (int case_num = 1; case_num <= cases; ++case_num) {
    cout << "CASE #" << case_num << ": ";
    run();
    cout << '\n';
  }

  return 0;
}
