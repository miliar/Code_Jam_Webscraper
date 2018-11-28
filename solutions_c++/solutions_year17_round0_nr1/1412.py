#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;


int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		int K;
		char S[1024];

		cin >> S >> K;

		int len = strlen(S);
		bool impossible = false;
		int flips = 0;

		for(int i = 0; i <= len; i++)
		{
			if(S[i] == '-')
			{
				if(i + K <= len)
				{
					for(int n = i; n < i + K; n++)
					{
						S[n] = (S[n] == '-' ? '+' : '-');
					}
					flips++;
				}
				else
				{
					impossible = true;
					break;
				}
			}
		}

 		cout << "Case #" << numCase << ": ";

		if(impossible)
			cout << "IMPOSSIBLE";
		else
			cout << flips;
 		cout << "\n";

		numCase++;
	}
	return 0;
}
