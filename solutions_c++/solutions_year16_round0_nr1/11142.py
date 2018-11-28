#include <iostream>
#include <sstream>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int tn = 1; tn <= t; tn++)
    {
      int n;
      cin >> n;
      if (n == 0)
	{
	  cout << "Case #" << tn << ": INSOMNIA\n";
	  continue;
	}
      bool seen[255];
      for (int i = 0; i < 255; i++)
	seen[i] = false;
      long long x = n;
      while (true)
	{
	  // update
	  stringstream ss;
	  ss << x;
	  string s = ss.str();
	  for (int i = 0; i < s.length(); i++)
	    seen[(int)s[i]] = true;
	  // check
	  bool all = true;
	  for (int i = 48; i < 58; i++)
	    if (!seen[i])
	      {
		all = false;
		break;
	      }
	  if (all)
	    {
	      cout << "Case #" << tn << ": " << x << endl;
	      break;
	    }
	  // inc
	  x += n;
	}
    }
  return 0;
}
