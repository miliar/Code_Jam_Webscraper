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
		int answer1, answer2;
		int numbers1[4], numbers2[4], fake[4];

		cin >> answer1;

		for (int i = 1; i <= 4; i++)
		{
			int *p = (i == answer1 ? numbers1 : fake);
			for (int k = 0; k < 4; k++)
				cin >> *(p + k);
		}

		cin >> answer2;

		for (int i = 1; i <= 4; i++)
		{
			int *p = (i == answer2 ? numbers2 : fake);
			for (int k = 0; k < 4; k++)
				cin >> *(p + k);
		}

		int found = 0;
		int value = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (numbers1[i] == numbers2[k])
				{
					found++;
					value = numbers1[i];
				}
			}
		}

		cout << "Case #" << numCase << ": ";
		if (found == 0)
			cout << "Volunteer cheated!";
		else  if (found == 1)
			cout << value;
		else
			cout << "Bad magician!";
		cout << "\n";

		numCase++;
	}
	return 0;
}
