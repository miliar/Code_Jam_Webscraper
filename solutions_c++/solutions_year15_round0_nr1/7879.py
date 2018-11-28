#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
  int T, Smax, friends, standing;
  int Shy[1001];
  string data;
  
  cin >> T;
  
  for (int i = 0; i < T; ++i)
  {
    friends = 0;
    standing = 0;

    cin >> Smax >> data;
    for (int j = 0; j <= Smax; ++j)
    {
      Shy[j] = data[j] - '0';
    }

    for (int S = 0; S <= Smax; ++S)
    {
      int x = 0;
      if (standing < S && Shy[S] > 0)
      {
	x = S - standing;
      }
      if (x > 0)
      {
	friends += x;
	standing += x;
      }      

      standing += Shy[S];
    }
    cout << "Case #" << i+1 << ": " << friends << "\n";
  }
  return 0;
}
