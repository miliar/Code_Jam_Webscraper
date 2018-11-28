#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
using namespace std;

bool IsPalindrome(unsigned long long num) {
  vector<int> digits;
  while(num >= 10) {
    digits.push_back(num % 10);
    num = num / 10;
  }
  digits.push_back(num); 

  int beg = 0;
  int fin = digits.size() - 1;
  while (beg <= fin) {
    if (digits[beg] != digits[fin])
      return 0;
    beg++;
    fin--;
  }
  return 1;
}

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; ++i) {
    unsigned long a, b;
    cin >> a >> b;
    unsigned long st = ceil(sqrt(a));
    unsigned long en = floor(sqrt(b));

    int cnt = 0;
    for (unsigned long num = st; num <= en; ++num) {
      if (IsPalindrome(num) && IsPalindrome(num * num)) 
        cnt++;
    }
    cout << "Case #" << (i+1) << ": " << cnt << endl;
  }
}
