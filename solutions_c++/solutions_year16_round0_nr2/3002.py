#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

typedef map<string,int> Dirs;

int main(int argc, char* argv[])
{
  int iCases=0;
 
  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int i=1;i<=iCases;i++)
  {
    string PanStack;
    cin >> PanStack;
    unsigned long long flips=0;

	bool startsWithMinus=((*PanStack.c_str())=='-');
	int prevSymbol=0;
	if (!startsWithMinus)
		prevSymbol=1;

	int minusChains=0;

	if (PanStack.length()==1)
	{
		if (prevSymbol==1) 
		{
		  flips=0;
		}
		else
		{
		  flips=1;
		}
	}
	else
	{
		for (unsigned int k=1;k<PanStack.length();k++)
		{
			  char stateChar=(*(PanStack.c_str()+k));
			  int symbol=0;
			  if (stateChar=='-') 
				  symbol=0;
			  if (stateChar=='+')
				  symbol=1;

			  if (prevSymbol==0 && symbol==1)
				  minusChains++;

			  prevSymbol=symbol;
		}
		if (prevSymbol==0)
			minusChains++;

		flips=minusChains*2;
		if (startsWithMinus)
			flips--;
	}
    cout<< "Case #" << i << ": " << flips << endl;

  }
  return 0;
}
