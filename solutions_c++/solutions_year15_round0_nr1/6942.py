#include <iostream>

using namespace std;

int main()
{
  int T, Smax, n, c;
  string p;
  
  cin >> T;
  for(int i = 1; i <= T; i++)
  {
    cin >> Smax;
    cin >> p;

    n = c = 0;
    for(int j = 0; j <= Smax; j++)
    {
      if(c < j)
      {
	n += j - c;
	c += j - c;
      }
      c += p[j] - '0';
    }
    
    cout << "Case #" << i << ": " << n << endl;    
  }

  return 0;
}
