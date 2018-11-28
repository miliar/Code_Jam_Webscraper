#include <iostream>
#include <sstream>
using namespace std;

string my_to_string(long long int n)
{
  stringstream ss;
  ss << n;
  return ss.str();
}

long long int to_base2(long long int x, long long int base)
{
  long long int formed = 0;
  for(long long int i = 1; x != 0; i*=10)
    {
      formed += (x % base)*i;
      x /= base;
    }
  return formed;
}

long long int to_base(long long int x, long long int base)
{
  string s;
  long long int res = 0;
  x = to_base2(x, 2);
  s = my_to_string(x);
  long long int mul = 1;
  for(int i = s.length()-1; i >= 0; i--)
    {
      res += (s[i] - '0')*mul;
      mul *= base;
    }
  
  return res;
}


long long int can_divide(long long int x)
{
  for(long long int i = 2; i*i <= x ; i++)
    {
      if(x%i == 0)
	{
	  return i;
	}
    }
  return -1;
}

int solve()
{
  int n, m;
  cin >> n >> m;
  for(long long int i = ((1 << (n-1)) | 1);; i+=2)
    {
      long long int base_num[11], k_num[11];
      for(int j = 2; j <= 10; j++)
	{
	  base_num[j] = to_base(i, j);
	  k_num[j] = can_divide(base_num[j]);
	  if(k_num[j] == -1)
	    {
	      break;
	    }
	  if(j == 10)
	    {
	      cout << base_num[10];
	      for(int k = 2; k <= 10; k++)
		{
		  cout << " " << k_num[k];
		}
	      cout << endl;
	      m--;
	      if(m == 0)
		{
		  return 0;
		}
	    }
	}
    }
  
  
  return 0;
}


int main()
{
  int t;
  
  cin >> t;
  for(int i = 0; i < t; i++)
    {
      cout << "Case #" << i+1 << ":" << endl;
      solve();
    }
  return 0;
}
