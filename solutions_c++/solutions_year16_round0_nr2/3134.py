#include <iostream>
using namespace std;

int solve()
{
  string s;
  char prev;
  int ans = 0;

  cin >> s;
  prev = s[0];
  for(int i = 0; i < s.length(); i++)
    {
      if(prev != s[i])
	{
	  prev = s[i];
	  ans++;
	}
    }
  if(s[s.length()-1] == '-')
    {
      ans++;
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
      cout << "Case #" << i+1 << ": ";
      solve();
    }
  return 0;
}
