#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	int rowFirst = -1, rowSecond = -1;
	int gridFirst[16];
	int gridSecond[16];

	for (int i = 0; i < T; i++)
	{
		cin >> rowFirst;
		for (int j = 0; j < 16; j++) cin >> gridFirst[j];

		cin >> rowSecond;
		for (int j = 0; j < 16; j++) cin >> gridSecond[j];

		int answer = -1, possibles = 0;
		for (int f = 0; f < 4; f++)
			for (int s = 0; s < 4; s++)
				if (gridFirst[f+rowFirst*4-4] == gridSecond[s+rowSecond*4-4]) 
				{
					answer = gridFirst[f+rowFirst*4-4];
					possibles++;
				}

		cout << "Case #" << (i+1) << ": ";

		if (possibles == 0)
			cout << "Volunteer cheated!" << endl;
		else if (possibles == 1)
			cout << answer << endl;
		else
			cout << "Bad magician!" << endl;
	}

	return 0;
}