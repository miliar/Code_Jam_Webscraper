#include <stdlib.h>
#include <string>
#include <assert.h>
#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
#include <sstream>

using namespace std;

int findMax(vector<int> members, int& anotherMax, bool& third)
{
	int max = -1;
	int maxInd;
	int secondMaxInd = -1;
	bool first = false;
	for (int j = 0; j < members.size(); j++)
	{
		if (first && members[j] == max)
		{
			secondMaxInd = j;
			first = false;
		}
		if (members[j] > max) 
		{
			max = members[j];
			maxInd = j;
			secondMaxInd = -1;
			first = true;
		}		
	}

	third = false;
	if (max == 1 && secondMaxInd != -1)
	{
		for (int j = 0; j < members.size(); j++)
		{
			if (j == maxInd || j == secondMaxInd)
				continue;

			if (members[j] == 1)
				third = true;
		}
	}

	anotherMax = secondMaxInd;
	return maxInd;
}

int main()
{
	int testCases;
	cin >> testCases;

	for (int i = 1; i <= testCases; i++)
	{
		int N;
		cin >> N;

		vector<int> members;

		for (int j = 0; j < N; j++)
		{
			int P;
			cin >> P;

			members.push_back(P);
		}		

		int max1;
		int max2;

		bool thirdOne;

		string evac;

		cout << "Case #" << i << ":";

		while (true)
		{
			max1 = findMax(members, max2, thirdOne);

			if (members[max1] == 0)
				break;

			evac += 'A' + max1;
			members[max1]--;

			if (max2 != -1 && !thirdOne)
			{
				evac += 'A' + max2;
				members[max2]--;
			}

			cout << " " << evac;
			evac = "";
		}

		cout << endl;
	}
}