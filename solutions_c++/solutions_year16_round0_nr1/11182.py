#include <iostream>
#include <vector>

using namespace std;

bool is_full(vector<bool>& v)
{
  // Check if vector full
  bool full = true;
  for (int i = 0; i < 10; ++i)
  {
    full &= v[i];
  }
  return full;
}

bool update_vector(vector<bool>& v, int n, int& res)
{
  int save = n;
  while (n > 0)
  {
    res = n % 10;
    /* cout << "res: " << res << "\n"; */
    v[res] = true;

    if (is_full(v))
    {
      res = save;
      return true;
    }

    n /= 10;
  }
  return false;
}

int main()
{
  int t;
  cin >> t;

  for (int i = 1; i <= t; ++i)
  {
    int n;
    cin >> n;
    vector<bool> check(10, false);

    int tmp = n;
    if (tmp == 0)
    {
      cout << "Case #" << i << ": INSOMNIA\n";
      continue;
    }

    int j = 2;
    while (!update_vector(check, tmp, tmp))
      tmp = n * j++;

    cout << "Case #" << i << ": " << tmp << endl;
  }
  return 0;
}
