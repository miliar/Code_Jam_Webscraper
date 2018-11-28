#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stdio.h>      
#include <math.h>       
#include "BigIntegerLibrary.hh"

using namespace std;

int main(int argc, char* argv[])
{
  int iCases=0;
  char buffer[50];

  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int i=1;i<=iCases;i++)
  {
    int K,C,S;
    cin >> K >> C >> S;

	cout<< "Case #" << i << ":";

	if (S<K)
	{
	  cout << "IMPOSSIBLE";
	}
	else
	{
		for (int p=1;p<=K;p++)
		{
			unsigned long long res=p;
			for (int j=C-1;j>=1;j--)
			{
				unsigned long long power=K;
				for (int n=1;n<j;n++)
					power=power*K;

				res=res+(p-1)*power;
			}

			cout << " " << res;
			//"IMPOSSIBLE";
		}
	}
	cout << endl;
  }
  return 0;
}
