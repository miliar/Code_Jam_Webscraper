#include <iostream>

int main()
{
  int T;
  std::string s;
  std::cin >> T;
  for ( int t = 1; t <= T; ++t )
    {
      std::cin >> s;
      std::string ans;
      for ( int i = 0; i < s.size(); ++i )
	{
	  if ( ans.empty() )
	    ans.push_back(s[i]);
	  else
	    {
	      if ( ans[0] <= s[i] )
		ans.insert(ans.begin(), s[i]);
	      else
		ans.push_back(s[i]);
	    }
	}
      std::cout << "Case #" << t << ": " << ans << std::endl;
    }
  return 0;
}
