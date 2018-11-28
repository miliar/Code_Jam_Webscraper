#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;

main()
{
  ll T;

  // INPUT
  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    ll N;
    int count = 0;
    vector<bool> digits (10, false);
    cin >> N;
    if (N == 0)
      cout << "Case #" << i << ": INSOMNIA" << endl;
    else {
      ll result;
      for (ll j = 1; true && count < 10; ++j) {
        ll tmp = N*j;
        result = tmp;
        while (tmp > 0) {
          int digit = tmp % 10;
          if (digits[digit] == false)
            ++count;
          digits[digit] = true;
          tmp /= 10;
        }
      }
      cout << "Case #" << i << ": " << result << endl;
    }
  }
}
