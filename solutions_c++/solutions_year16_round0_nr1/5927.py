#include <stdlib.h>
#include <string>
#include <assert.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

bool check(vector<bool> number)
{
	for (int x = 0; x < number.size(); x++)
	{
		if (number[x] == true)
			continue;
		return false;
	}
	return true;
}

int main()
{
	int testCases;
	cin >> testCases;

	for (int i = 1; i <= testCases; i++)
	{
		int N;
		cin >> N;

		if (N == 0)
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;;
		}

		vector<bool> number(10, false);

		int lastNum;

		for (int j = 1; !check(number); j++)
		{
			lastNum = j*N;
			int x = j*N;
			while (x > 0)
			{
				int num = x % 10;
				number[num] = true;
				x = x / 10;
			}
		}

		cout << "Case #" << i << ": " << lastNum << endl;
	}
}