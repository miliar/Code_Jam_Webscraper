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
		int S;
		char arr[1000] = {0};

		cin >> S;
		cin >> arr;

		int friends = 0;
		int stoodup = arr[0] - '0';
		for (int Si = 1; Si < S + 1; Si++)
		{
			if (stoodup < Si)
			{
				friends += Si - stoodup;
				stoodup = Si;
			}
			stoodup += arr[Si] - '0';
		}

 		cout << "Case #" << numCase << ": ";
		cout << friends;
 		cout << "\n";

		numCase++;
	}
	return 0;
}
