#include <stdlib.h>
#include <string>
#include <assert.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

int main()
{
	int testCases;
	cin >> testCases;

	cin.ignore(10000, '\n');

	for (int i = 1; i <= testCases; i++)
	{
		string P;

		getline(cin, P);
		
		int size = P.size();
		string pancakes;

		for (int j = 0; j < size; j++)
		{
			if (j != 0 && P[j] == P[j - 1])
				continue;

			pancakes += P[j];
		}
		
		int num;

		if (pancakes[pancakes.size() - 1] == '+')
			num = pancakes.size() - 1;
		else
			num = pancakes.size();

		cout << "Case #" << i << ": " << num << endl;
	}
}