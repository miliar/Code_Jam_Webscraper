#include <iostream>
#include <string>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++)
    {
      long long ans = 0;
      string input;
      cin >> input;
      if(input.size() == 1)
	{
	  if(input[0] == '-')
	    cout << "Case #" << i << ": " << 1 << endl;
	  else
	    cout << "Case #" << i << ": " << 0 << endl;
	  continue;
	}
      for(int j = 0; j < input.size()-1; j++)
	if(input[j] != input[j+1])
	  ans++;
      if(input[input.size()-1] == '-')
	ans++;
      cout << "Case #" << i << ": " << ans << endl;
    }
}
