#include <iostream>

using namespace std;

void solve(long n, int c)
{
  if (n == 0)
  {
    cout << "Case #" << c << ": INSOMNIA" << endl;
    return;
  }
  bool foundAll = false;
  long hits[10] = {0};
  long norig = n;
  while (not foundAll)
  {
    long temp = n;
    while (temp > 9)
    {
      hits[(temp % 10)]++;
      temp = temp / 10;
    }
    hits[temp]++;

    int notZero = 0;
    for (int i = 0; i < 10; i++)
      if (hits[i] > 0)
        notZero++;

    if (notZero == 10)
    {
      foundAll = true;
      continue;
    }
    n += norig;
  }
  cout << "Case #" << c << ": " << n << endl;
}

int main()
{
  int t;
  long n;
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    cin >> n;
    solve(n, (i+1));
  }

}