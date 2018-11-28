#include <iostream>
using namespace std;
int main()
{
	int nCase = 0;	
	int maze1[4][4] = {0};
	int maze2[4][4] = {0};
	int ans1 = 0;
	int ans2 = 0;

	cin >> nCase;
	for (int i=0; i<nCase; i++)
	{
		cin >> ans1;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				cin >> maze1[j][k];
			}	
		}

		cin >> ans2;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				cin >> maze2[j][k];
			}	
		}
		
		int answer = 0;
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				if (maze1[ans1-1][j] == maze2[ans2-1][k])
				{
					if (answer == 0)
					{
						answer = maze1[ans1-1][j];
					}
					else
					{
						answer = -1;
					}
				}
			}

			if (answer == -1)
			{
				break;
			}
		}

		cout << "Case #" << i+1 << ": ";
		if (answer == 0)
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if (answer == -1)
		{
			cout << "Bad magician!" << endl;
		}
		else
		{
			cout << answer << endl;
		}
	}

	return 0;
}