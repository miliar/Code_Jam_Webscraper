#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

int contains(unsigned long long val)
{
  int res = 0;
  do
  {
    res |= (1 << val%10);
    val /= 10;
  }
  while (val != 0);
  return res;
}

void compute(int val)
{
  if (val == 0) {
    cout << "INSOMNIA" << endl;
  } else {
    int seen = 0;

    unsigned long long tval = val;
    while (seen != 1023)
    {
      seen |= contains(tval);
      tval += val;
    }
    cout << tval - val << endl;
  }
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    int val;
    cin >> val;
    cout << "Case #" << i << ": "; compute(val);
  }
}
