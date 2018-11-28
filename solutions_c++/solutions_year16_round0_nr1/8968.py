#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <functional>

using namespace std;

set<int> get_digits(long number)
{
  auto digits = set<int>();
  if (number == 0) {
    digits.insert(number);
  }
  while (number > 0) {
    int d = number % 10;
    digits.insert(d);
    number /= 10;
  }
  return digits;
}

int main()
{
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t)
  {
    long N;
    cin >> N;
    long last;
    auto digits = set<int>();
    for (int i = 2, n = N; digits.size() < 10; ++i) {
      if (N == 0) {
        break;
      }
      auto d = get_digits(n);
      digits.insert(d.begin(), d.end());
      last = n;
      n =  N * i;
    }
    cout << "Case #" << t + 1 << ": ";
    if (N == 0) {
      cout << "INSOMNIA";
    }
    else {
      cout << last;
    }
    cout << endl;
  }
  return 0;
}