#include <iostream>

using namespace std;

bool saw[10];
bool check();

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++)
    {
      long long N;
      cin >> N;
      if(N == 0)
	{
	  cout << "Case #" << i << ": "<< "INSOMNIA\n";
	  continue;
	}
      long long a = 1;
      long long ans = 0;
      long long count = 0;
      for(int i = 0; i < 10; i++)
	saw[i] = false;
      while(!check())
	{
	  count++;
	  int dummy = N * a;
	  ans = dummy;
	  a++;
	  while(dummy >= 10)
	    {
	      saw[dummy%10] = true;
	      dummy /= 10;
	    }
	  saw[dummy] = true;
	  if(count > 9999999999)
	    {
	      cout << "Case #" << i << ": "<< "INSOMNIA\n";
	      break;
	    }
	}
      if(count < 9999999999)
	cout << "Case #" << i << ": "<< ans << endl;
    }
}

bool check()
{
  for(int i = 0; i < 10; i++)
    if(!saw[i])
      return false;
  return true;
}
