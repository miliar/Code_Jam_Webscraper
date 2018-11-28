#include <iostream>
#include <vector>
#include <bitset>
#include <string>

using namespace std;

#define debug(x) cout << #x << ": " << x << endl;

template<typename T>
void compute(T val)
{
  int count = 0;
  int start_idx = 0;
  if (val[0] == '-') {
    count++;
    for (start_idx = 1; start_idx < val.size() && val[start_idx] == '-'; ++start_idx);
  }

  for (; start_idx < val.size(); )
  {
    auto c = val[start_idx];
    if (c == '-')
    {
      count += 2;
      do {
        c = val[start_idx];
        ++start_idx;
      } while (start_idx < val.size() && c =='-');
    } else start_idx++;
  }
  cout << count << endl;
}

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
  {
    string val;
    cin >> val;
    cout << "Case #" << i << ": "; compute(val);
  }
}
