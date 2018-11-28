#include <iostream>
#include <string>
#include <vector>

/*
	Inputs:
	-Number of test cases
	-The maximum possible shyness
	-A number with each digit containing the number of kth shy people, where k is the index of a digit.

	Outputs:
	"Case #x: y"
	where x is the test case and y is the minimum number of friends you must invite.
*/

using namespace std;

int main(int argc, char* argv[])
{
	unsigned int testCases = 0;
	cin >> testCases;

	vector<unsigned int> friends;

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		unsigned int maxShy = 0;
		cin >> maxShy;

		string shynesses;
		cin >> shynesses;

		unsigned int peopleCount = 0;

		unsigned int friendCount = 0;

		for (unsigned int shyness = 0; shyness < shynesses.size(); shyness += 1)
		{
			unsigned int count = 0;
			count = shynesses[shyness] - '0';

			if (count > 0)
			{
				if (peopleCount >= shyness)
				{
					peopleCount += count;
				}
				else
				{
					friendCount += (shyness - peopleCount);
					peopleCount += count + (shyness - peopleCount);
				}
			}
		}

		friends.push_back(friendCount);
	}

	for (unsigned int tc = 0; tc < testCases; tc += 1)
	{
		cout << "Case #" << tc + 1 << ": " << friends[tc] << endl;
	}
}

