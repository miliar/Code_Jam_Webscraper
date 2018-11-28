#include <iostream>
#include <string>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int c = 1; c <= T; c++)
    {
      string S;
      cin >> S;
      string N = "";
      N += S[0];
      for (int i = 1; i < S.size(); i++)
	{
	  if (S[i] >= N[0])
	    {
	      N = S[i] + N;
	    } 
	  else
	    {
	      N = N + S[i];
	    }
	}
      cout << "Case #" << c << ": " << N << endl;
    }
}
