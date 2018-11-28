#include <iostream>

using namespace std;

int main()
{
	int T, answer1, answer2;
	cin>>T;
	int firstArrangement[4][4], secondArrangement[4][4];

	for (int i = 1; i <= T; ++i)
	{
		cin>>answer1;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin>>firstArrangement[j][k];
			}
		}

		cin>>answer2;
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin>>secondArrangement[j][k];
			}
		}

		int index=0;
		int type=0; //0 cheated, 1 bad magic, 2 all good
		bool found=false;
		answer1--;
		answer2--;


		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				if (firstArrangement[answer1][j] == secondArrangement[answer2][k])
				{
					if(found == true)
					{
						type=1;
						break;
					}
					else
					{
						type=2;
						index=j;
						found=true;
					}
				}
			}
		}

		switch ( type )
		{
			case 0:
				cout<<"Case #"<< i <<": Volunteer cheated!\n";
				break;
			case 1:
				cout<<"Case #"<< i <<": Bad magician!\n";
				break;
			case 2:
				cout<<"Case #"<< i <<": "<< firstArrangement[answer1][index] <<"\n";
				break;

		}

	}
	return 0;
}