#include <iostream>
#include <sstream>

using namespace std;
#define MAXSIZE 1500

int main()
{
	int T;
	string line;
	getline(std::cin, line);
	std::istringstream stream(line);
	stream >> T;

	for(int i = 1; i <= T; i++)
	{
		int nFriends = 0;
		int totalStand = 0;
		int input[MAXSIZE] = {0};
		int SMax = 0;
		
		getline(std::cin, line);
		std::istringstream stream(line);
		stream >> SMax;
		for (int j=0; j <= SMax; j++) {
			char inp;
			stream >> inp;
			input[j] = inp - '0';
		}

		totalStand += input[0];
		for(int j = 1; j <= SMax; j++)
		{
			if(input[j] != 0 && j > totalStand)
			{
				nFriends += (j - totalStand);
				totalStand += nFriends;
			}
			totalStand += input[j];

			if (totalStand >= SMax)
				break;
		}
		cout << "Case #" << i << ": " << nFriends << endl;
	}
}