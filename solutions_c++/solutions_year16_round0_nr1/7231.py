#include <cstdlib>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <utility>
#include <queue>

#define PI 3.14159265

using namespace std;

bool all_seen( bool tab[])
{
  return tab[0] && tab[1] && tab[2] && tab[3] && tab[4] && tab[5] && tab[6] && tab[7] && tab[8] && tab[9];
}

void see_digits(bool seen[], long long number)
{
  while (number > 0)
  {
    seen[number%10] = true;
    number /= 10;
  }
}

long long count_iterations(int n)
{
  if (n == 0)
    return -1;
  long long res = n;
  bool seen[10] = {false, false, false, false, false, false, false, false, false, false};
  see_digits(seen, res);
  while (not (all_seen(seen)))
  {
    res += n;
    see_digits(seen, res);
  }
  return res;
}

int main(int argc, const char *argv[])
{
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i)
  {
    int n;
    cin >> n;
    cout << "Case #" << i+1 << ": ";
    int res = count_iterations(n);
    if (res == -1)
      cout << "INSOMNIA" << endl;
    else
      cout << res << endl;
  }
  return 0;
}


