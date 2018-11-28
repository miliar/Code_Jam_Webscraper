#include <fstream>
#include <string>

using namespace std;

unsigned short int stateA[4][4], stateB[4][4], guessA, guessB, output, foundCount;

int main()
{
	ifstream ins("input.in");
	ofstream outs("output.out");
	size_t casesCount;
	ins >> casesCount;
	for (size_t caseNo = 1; caseNo <= casesCount; caseNo++)
	{
		outs <<"Case #" << caseNo << ": ";
		ins >> guessA;
		for (unsigned short int i = 0; i < 4; i++)
			for (unsigned short int j = 0; j < 4; ins >> stateA[i][j++]);
		ins >> guessB;
		for (unsigned short int i = 0; i < 4; i++)
			for (unsigned short int j = 0; j < 4; ins >> stateB[i][j++]);
		foundCount = 0;
		for (unsigned short int i = 0; i < 4; i++)
		{
			for (unsigned short int j = 0; j < 4; j++)
			{
				if(stateA[guessA - 1][i] == stateB[guessB - 1][j])
				{
					foundCount++;
					output = stateA[guessA - 1][i];
				}
			}
		}
		if(foundCount == 0)
			outs << "Volunteer cheated!" << endl;
		else if(foundCount == 1)
			outs << output << endl;
		else
			outs << "Bad magician!" << endl;
	}
	ins.close();
	outs.close();
	return 0;
}