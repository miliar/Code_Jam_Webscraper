

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>    
using namespace std;

int main() {

	string inputName = "A-large.in";
	string outputName = "A-large.out";
	
	ifstream inputFile;
	ofstream outputFile;

	inputFile.open(inputName);
	outputFile.open(outputName);

	int T;
	inputFile >> T;
	int N;

	for (int test = 1; test <= T; test++)
	{
		string audience;
		inputFile >> N;
		inputFile >> audience;
		
		unsigned int updatedAudience = audience[0] - '0';
		unsigned int friendsNeeded = 0, totalFriends =0;
		

		for (int n = 1; n<=N; n++)
		{
			int current = audience[n] - '0';
			if (current > 0)
			{
				friendsNeeded = 0;
				if (n > updatedAudience)
				{
					friendsNeeded = n - updatedAudience;
					totalFriends += friendsNeeded;
				}
				updatedAudience += current + friendsNeeded;
				if (updatedAudience > N)
					break;
			}
		}
		outputFile << "Case #" << test << ": " << totalFriends << endl;

	}

	outputFile.close();
	inputFile.close();

	return EXIT_SUCCESS;
}
