#include <iostream>
#include <string>
using namespace std;

void flip(char& happy)
{
  if (happy=='+')
    happy='-';
  else
    happy='+';
}

int main()
{
  int T; cin >> T;
  for (int i=1; i<=T; i++)
    {
      string pancakes; cin >> pancakes;
      char happy='+';
      int flips=0;
      for (int a=pancakes.length()-1; a>=0; a--)
	{
	  if (pancakes.at(a)!=happy)
	    {
	      flips++;
	      flip(happy);
	    }
	}
      cout << "Case #" << i << ": " << flips << endl;
    }
}
