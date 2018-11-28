#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <map>
#include <cmath>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
   
	ifstream cin("A-small-attempt0.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{

		map<int, bool> row;

		int a;
		cin >> a;

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				int x;
				cin >> x;
				if (j + 1 == a)
				{
					row[x] = true;
				}
			}

		}

		int b;
		cin >> b;

		int found_count = 0;
		int found = -1;

		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				int x;
				cin >> x;
				if (j + 1 == b)
				{
					if (row[x])
					{
						found_count++;
						found = x;
					}
				}
			}
		}

		if (found_count == 0)
		{
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else if (found_count > 1)
		{
			cout << "Case #" << i << ": Bad magician!" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << found << endl;
		}
	}


}