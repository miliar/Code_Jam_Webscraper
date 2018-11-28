#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>

using namespace std;

void main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int N;
	char arr[4][4];
	bool IsPoint = false;

	cin >> N;

	/*for(int i = 0; i < N; i++)
	{
		arr[i] = new char[N];
	}*/

	for(int i = 0; i < N; i++)
	{
		IsPoint = false;

		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				cin >> arr[j][k];
				if(arr[j][k] == '.')
					IsPoint = true;
			}
		}

		if(((arr[0][0] == 'T' || arr[0][0] == 'X') && (arr[0][1] == 'T' || arr[0][1] == 'X') && (arr[0][2] == 'T' || arr[0][2] == 'X') && (arr[0][3] == 'T' || arr[0][3] == 'X'))
			|| ((arr[1][0] == 'T' || arr[1][0] == 'X') && (arr[1][1] == 'T' || arr[1][1] == 'X') && (arr[1][2] == 'T' || arr[1][2] == 'X') && (arr[1][3] == 'T' || arr[1][3] == 'X'))
			|| ((arr[2][0] == 'T' || arr[2][0] == 'X') && (arr[2][1] == 'T' || arr[2][1] == 'X') && (arr[2][2] == 'T' || arr[2][2] == 'X') && (arr[2][3] == 'T' || arr[2][3] == 'X'))
			|| ((arr[3][0] == 'T' || arr[3][0] == 'X') && (arr[3][1] == 'T' || arr[3][1] == 'X') && (arr[3][2] == 'T' || arr[3][2] == 'X') && (arr[3][3] == 'T' || arr[3][3] == 'X')))
		cout << "Case #" << i + 1 << ": X won" << endl;
		else
			if(((arr[0][0] == 'T' || arr[0][0] == 'O') && (arr[0][1] == 'T' || arr[0][1] == 'O') && (arr[0][2] == 'T' || arr[0][2] == 'O') && (arr[0][3] == 'T' || arr[0][3] == 'O'))
			|| ((arr[1][0] == 'T' || arr[1][0] == 'O') && (arr[1][1] == 'T' || arr[1][1] == 'O') && (arr[1][2] == 'T' || arr[1][2] == 'O') && (arr[1][3] == 'T' || arr[1][3] == 'O'))
			|| ((arr[2][0] == 'T' || arr[2][0] == 'O') && (arr[2][1] == 'T' || arr[2][1] == 'O') && (arr[2][2] == 'T' || arr[2][2] == 'O') && (arr[2][3] == 'T' || arr[2][3] == 'O'))
			|| ((arr[3][0] == 'T' || arr[3][0] == 'O') && (arr[3][1] == 'T' || arr[3][1] == 'O') && (arr[3][2] == 'T' || arr[3][2] == 'O') && (arr[3][3] == 'T' || arr[3][3] == 'O')))
			cout << "Case #" << i + 1 << ": O won" << endl;
			else
				if(((arr[0][0] == 'T' || arr[0][0] == 'O') && (arr[1][0] == 'T' || arr[1][0] == 'O') && (arr[2][0] == 'T' || arr[2][0] == 'O') && (arr[3][0] == 'T' || arr[3][0] == 'O'))
			    || ((arr[0][1] == 'T' || arr[0][1] == 'O') && (arr[1][1] == 'T' || arr[1][1] == 'O') && (arr[2][1] == 'T' || arr[2][1] == 'O') && (arr[3][1] == 'T' || arr[3][1] == 'O'))
			    || ((arr[0][2] == 'T' || arr[0][2] == 'O') && (arr[1][2] == 'T' || arr[1][2] == 'O') && (arr[2][2] == 'T' || arr[2][2] == 'O') && (arr[3][2] == 'T' || arr[3][2] == 'O'))
			    || ((arr[0][3] == 'T' || arr[0][3] == 'O') && (arr[1][3] == 'T' || arr[1][3] == 'O') && (arr[2][3] == 'T' || arr[2][3] == 'O') && (arr[3][3] == 'T' || arr[3][3] == 'O')))
				cout << "Case #" << i + 1 << ": O won" << endl;
				else
					if(((arr[0][0] == 'T' || arr[0][0] == 'X') && (arr[1][0] == 'T' || arr[1][0] == 'X') && (arr[2][0] == 'T' || arr[2][0] == 'X') && (arr[3][0] == 'T' || arr[3][0] == 'X'))
			        || ((arr[0][1] == 'T' || arr[0][1] == 'X') && (arr[1][1] == 'T' || arr[1][1] == 'X') && (arr[2][1] == 'T' || arr[2][1] == 'X') && (arr[3][1] == 'T' || arr[3][1] == 'X'))
			        || ((arr[0][2] == 'T' || arr[0][2] == 'X') && (arr[1][2] == 'T' || arr[1][2] == 'X') && (arr[2][2] == 'T' || arr[2][2] == 'X') && (arr[3][2] == 'T' || arr[3][2] == 'X'))
			        || ((arr[0][3] == 'T' || arr[0][3] == 'X') && (arr[1][3] == 'T' || arr[1][3] == 'X') && (arr[2][3] == 'T' || arr[2][3] == 'X') && (arr[3][3] == 'T' || arr[3][3] == 'X')))
					cout << "Case #" << i + 1 << ": X won" << endl;
					else
						if(((arr[0][0] == 'T' || arr[0][0] == 'X') && (arr[1][1] == 'T' || arr[1][1] == 'X') && (arr[2][2] == 'T' || arr[2][2] == 'X') && (arr[3][3] == 'T' || arr[3][3] == 'X'))
							|| ((arr[0][3] == 'T' || arr[0][3] == 'X') && (arr[1][2] == 'T' || arr[1][2] == 'X') && (arr[2][1] == 'T' || arr[2][1] == 'X') && (arr[3][0] == 'T' || arr[3][0] == 'X')))
							cout << "Case #" << i + 1 << ": X won" << endl;
						else
							if(((arr[0][0] == 'T' || arr[0][0] == 'O') && (arr[1][1] == 'T' || arr[1][1] == 'O') && (arr[2][2] == 'T' || arr[2][2] == 'O') && (arr[3][3] == 'T' || arr[3][3] == 'O'))
								|| ((arr[0][3] == 'T' || arr[0][3] == 'O') && (arr[1][2] == 'T' || arr[1][2] == 'O') && (arr[2][1] == 'T' || arr[2][1] == 'O') && (arr[3][0] == 'T' || arr[3][0] == 'O')))
							cout << "Case #" << i + 1 << ": O won" << endl;
							else
								if(IsPoint)
									cout << "Case #" << i + 1 << ": Game has not completed" << endl;
								else
									cout << "Case #" << i + 1 << ": Draw" << endl;
	}


}