#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iomanip>
#include <queue>

using namespace std;

unsigned long long num (vector<bool> &b, long long base)
{
  unsigned long long n = 0;
  for(int i = 0; i < b.size(); i++)
  {
    n *= base;
    n += b[i];
  }
  return n;
}

void inc(vector<bool> &b)
{
  for(int i = b.size() - 2; i >= 1; i--)
  {
    b[i] = !b[i];
    if(b[i]) break;
  }
}

int main()
{
  int n = 1;
  //cin >> n;
  for(int c = 1; c <= n; c++)
  {
    //solving
    int n, j;
    //cin >> n >> j;
    vector<bool> foot(16,0);
    foot[0] = 1;
    foot[15] = 1;
    cout << "Case #" << c << ": " << endl;
    for(int i = 0; i < 500; i++)
    {
      for(bool b : foot)
        cout << b;
      for(bool b : foot)
        cout << b;
      //that was the number, now the divisors are the rep in base i
      for(int i = 2; i <= 10; i++)
        cout << " " << num(foot, i);
      cout << endl;
      inc(foot);
    }
  }
  return 0;
}
