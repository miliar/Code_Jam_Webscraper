#include <bits/stdc++.h>
using namespace std;

int digits_seen;
int all_digits_seen = (1 << 10) - 1;

bool check(int n)
{
  int digit;
  while (n > 0)
  {
    digit = n % 10;
    n = n / 10;
    digits_seen |= (1 << digit);
  }

  if (digits_seen == all_digits_seen)
  {
    return true;
  }
  else
  {
    return false;
  }
}

int main()
{
  int T, N;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    digits_seen = 0;
    cin >> N;
    if (N == 0)
    {
      printf("Case #%d: INSOMNIA\n", t);
      continue;
    }
    int current_number = 0;

    for (;;)
    {
      current_number += N;
      if (check(current_number))
      {
        printf("Case #%d: %d\n", t, current_number);
        break;
      }
    }
  }
}
