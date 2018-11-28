#include <iostream>
#include <fstream>
#include <string>


using namespace std;



int main(void)
{
	ifstream inFile("in.in");
	ofstream outFile("out.txt");

	int cases;
	inFile >> cases;

	for (int c = 1; c <= cases; ++c)
	{
		int Smax;
		inFile >> Smax;
		int *audience = new int[Smax + 1];
		char temp[2];
		temp[1] = 0;
		for (int i = 0; i < Smax + 1; ++i)
		{
			inFile >> temp[0];
			audience[i] = atoi(temp);
		}
		int peopleStanding = audience[0];
		int toInvite = 0;
		for (int i = 1; i < Smax+1; ++i)
		{
			if (peopleStanding >= i)
				peopleStanding += audience[i];
			else
			{
				toInvite += i - peopleStanding;
				peopleStanding = i+audience[i];
			}
		}
		outFile << "Case #" << c << ": " << toInvite << endl;
	}
	inFile.close();
	outFile.close();
	system("pause");

}