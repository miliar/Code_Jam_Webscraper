#include <iostream>
using namespace std;

int solve()
{
  int p[1001] = {0};
  int d;
  int max_p = 0;
  
  cin >> d;
  for(int i = 0; i < d; i++)
    {
      cin >> p[i];
      if(max_p < p[i])
	{
	  max_p = p[i];
	}
    }

  int ans = 10000;
  for(int i = 1; i <= max_p; i++)
    {
      int c_ans = 0;
      for(int j = 0; j < d; j++)
	{
	  c_ans += (p[j] - 1)/i;
	}
      c_ans += i;
      if(ans > c_ans)
	{
	  ans = c_ans;
	}
    }

  cout << ans << endl;
  
  return 0;
}

int main()
{
  int t;

  cin >> t;
  for(int i = 0; i < t; i++)
    {
      cout << "Case #" << i + 1 << ": ";
      solve();
    }
  
  return 0;
}
