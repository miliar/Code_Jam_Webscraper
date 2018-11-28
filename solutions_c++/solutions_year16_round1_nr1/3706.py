#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#define rep(i,n) for(int i = 0; i < (n); i++)

int solve()
{
  string s, ans = "";
  
  cin >> s;
  ans += s[0];
  rep(i, s.length())
    {
      if(i == 0)
	{
	  continue;
	}
      if(s[i] >= ans[0])
	{
	  ans = s[i] + ans;
	}else{
	ans += s[i];
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
      cout << "Case #" << i+1 << ": ";
      solve();
    }
  return 0;
}
