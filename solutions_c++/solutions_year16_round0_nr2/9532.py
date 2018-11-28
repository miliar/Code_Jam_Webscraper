#include <iostream>
#include <string>

using namespace std;

void solve ()
{
  string s;

  cin >> s;
  
  char c = '=';
  int count = 0;
  int last = s.length ();
  
  for (int i = s.length () - 1; i > -1; i--)
    {
      if (i == 0 && s[i] == '+')
	{
	  cout << 0 << endl;
	  return;
	}
      
      if (s[i] == '-')
	{
	  last = i;
	  break;
	}
    }
  
  for (int i = 0; i <= last; i++)	
    if (s[i] != c)
      {
	count++;
	c = s[i];
      }

  cout << count << endl;
}

int main ()
{
  int i = 1;
  int n;

  cin >> n;

  while (n--)
    {
      cout << "Case #" << i++ << ": ";
      solve ();
    }
  
  return 0;
}
