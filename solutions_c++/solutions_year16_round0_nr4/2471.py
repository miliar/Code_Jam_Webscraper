#include <iostream>
using namespace std;

int solve()
{
  long long int k, c, s;
  cin >> k >> c >> s;
  long long int k_c=1;
  for(long long int i = 1; i < c; i++)
    {
      k_c *= k;
    }
  for(long long int i = 0; i < s; i++)
    {
      cout << " " << 1 + k_c*i;
    }
  cout << endl;
  return 0;
}


int main()
{
  int t;
  
  cin >> t;
  for(int i = 0; i < t; i++)
    {
      cout << "Case #" << i+1 << ":";
      solve();
    }
  return 0;
}
