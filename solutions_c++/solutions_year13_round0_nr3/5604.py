#include <iostream>
#include <cmath>

using namespace std;

bool isFair(int n)
{
  int a[20], count = 0;
  while (n > 0)
  {
    a[count++] = n % 10;
    n /= 10;
  }
  for (int i = 0; i < (count + 1) / 2; i++)
    if (a[i] != a[count - 1 - i]) return false;
  return true;
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++)
  {
    int a, b;
    cin >> a >> b;
    int count = 0;
    for (int j = a; j <= b; j++)
    {
      double t = sqrt(j);
      if (t != (int)t) continue;
      if (isFair(t) && isFair(j)) count++;
    }
    cout << "Case #" << i << ": " << count << endl;
  }
  return 0;
}

