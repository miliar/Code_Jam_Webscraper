#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string my_to_string(long long int n)
{
  stringstream ss;
  ss << n;
  return ss.str();
}

int solve()
{
  long long int n;
  string s;
  int digit_flag[10] = {0};
  
  cin >> n;
  for(long long int i = 1; i < 1000; i++)
    {
      s = my_to_string(i*n);
      for(int j = 0; j < s.length(); j++)
	{
	  digit_flag[s[j]-'0'] = 1;
	}
      for(int j = 0; j < 10; j++)
	{
	  if(digit_flag[j] == 0)
	    {
	      break;
	    }
	  if(j == 9)
	    {
	      cout << s << endl;
	      return 0;
	    }
	}
    }
  cout << "INSOMNIA" << endl;
  
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
