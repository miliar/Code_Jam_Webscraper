#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;
	cin.ignore();

	for (int i = 1; i <= numCases; i++)
	{
		cout << "Case #" << i << ": ";

		string line;
		getline(cin, line);
		bool isHappy = true;
		int numFlips = 0;
		for (int i = line.length() - 1; i >= 0; i--)
		{
			if (isHappy && line[i] == '-')
			{
				isHappy = false;
				numFlips++;
			}
			else if(!isHappy && line[i] == '+')
			{
				isHappy = true;
				numFlips++;
			}
		}

		cout << numFlips << endl;
	}
	return 0;
}