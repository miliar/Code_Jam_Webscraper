#include <fstream>
using namespace std;

int cards[5][5];
int firstround[5];
int secondround[5];

int main()
{
	ofstream fout("A-small-attempt0.out");
    ifstream fin("A-small-attempt0.in");

	int t, count = 0;
	fin >> t;
	while(count++ < t)
	{
		for(int i = 0; i < 5; i++)
			for(int j = 0; j < 5; j++)
				cards[i][j] = 0;

		int row;
		fin >> row;
		for(int i = 1; i < 5; i++)
			for(int j = 1; j < 5; j++)
				fin >> cards[i][j];

		for(int j = 1; j < 5; j++)
			firstround[j] = cards[row][j];

		fin >> row;
		for(int i = 1; i < 5; i++)
			for(int j = 1; j < 5; j++)
				fin >> cards[i][j];

		for(int j = 1; j < 5; j++)
			secondround[j] = cards[row][j];

		bool one = false;
		bool multi = false;
		int selected;

		for(int i = 1; i < 5; i++)
		{
			int card = firstround[i];
			for(int j = 1; j < 5; j++)
			{
				if(card == secondround[j])
				{
					if(one == true)
					{
						multi = true;
						break;
					}
					else
					{
						one = true;
						selected = card;
					}
				}
			}

			if(multi == true)
				break;
		}

		if(one == false)
			fout << "Case #" << count << ": Volunteer cheated!" << endl;
		else if(multi == true)
			fout << "Case #" << count << ": Bad magician!" << endl;
		else
			fout << "Case #" << count << ": " << selected << endl;
	}
	return 0;
}
