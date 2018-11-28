#include <iostream>

using namespace std;

int main()
{
  int T; cin >> T;
  for (int i=1;i<=T;i++)
    {
      int K, C, S;
      cin >> K >> C >> S;

      cout << "Case #" << i << ": ";
      if (C==1 && S>=K)
	{
	  for (int a=1;a<K;a++)
	    cout << a << " ";
	  cout << K << endl;
	}
      else if (S<K)
	{
	  cout << "IMPOSSIBLE" << endl;
	}
      else
	{
	  for (int a=2;a<K;a++)
	    cout << a << " ";
	  cout << K << endl;
	}
    }
}
