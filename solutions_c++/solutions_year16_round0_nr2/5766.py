#include <iostream>

using namespace std;

int numOfFlips(string s)
{
  int flips = 0;
  char lastChar = s[0];
  for(int i = 1; i<s.length(); i++)
  {
    if(s[i] != lastChar)
    {
      flips++;
      lastChar = s[i];
    }
  }
  if(s[s.length()-1] == '-')
    flips++;

  return flips;
}

int main()
{
  int t;
  string s;
  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    cin >> s;
    cout << "Case #" << i << ": " << numOfFlips(s) << endl;
  }
}