#include <cmath>
#include <cstdio>
#include <unordered_set>
#include <iostream>
#include <algorithm>
using namespace std;

void digits(unordered_set<int>& digit, unsigned long long num) {
  if (num > 9) digits(digit, num / 10);
  digit.insert(num % 10);
}

int main(int argc, char* argv[]) {
  int t, n, m;
  string s ("INSOMNIA");
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  unordered_set<int> nums;
  unordered_set<int>& addr = nums;
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    m = n;
    int j = 1;
    unsigned long long k = 0;
    while (j <= 1000000) {
      digits(addr, k = j * m);
      if (nums.size() == 10) break;
      ++j;
    }
    cout << "Case #" << i << ": ";
    if (nums.size() != 10)
      cout << s << endl;
    else
      cout << k << endl;
    nums.clear();
  }
  return 0;

}
