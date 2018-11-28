#include <algorithm>
#include <iterator>
#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;

ll solve(ll n)
{
  if(n == 0)
    return -1;

  vector<bool> mask(10);
  int cnt = 0;

  ll mul = 1;
  while(cnt != 10)
  {
    ll cur = mul * n;
    while(cur)
    {
      ll last = cur % 10;
      if(!mask[last])
      {
        mask[last] = true;
        cnt++;
      }
      cur /= 10;
    }
    mul++;
  }

  return n * (mul - 1);
}

int main()
{
  int t;
  cin >> t;

  for(int tt = 1; tt <= t; tt++)
  {
    ll n;
    cin >> n;

    cout << "Case #" << tt << ": ";
    ll out = solve(n);
    if(out == -1)
      cout << "INSOMNIA" << endl;
    else
      cout << out << endl;
  }

	return 0;
}
