#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int testcase, tnum = 0;
	cin >> testcase;

	vector<string> game;
	string tmpstr;

	fstream file("Output.txt", iostream::out);

	int j;
	bool result = false;
	while (tnum < testcase)
	{
		game.clear();

		for (int i = 0; i < 4; ++i)
		{
			cin >> tmpstr;
			game.push_back(tmpstr);
		}
		
		for (int i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				if (game[i][j] == 'X' || game[i][j] == 'T')
					continue;
				break;
			}
			
			if (j == 4)
			{
				//cout << "Case #" << tnum+1 << ": X won" << endl;
				file << "Case #" << tnum+1 << ": X won" << endl;
				result = true;
				break;
			}
		}

		if (!result)
		{
			for (int i = 0; i < 4; ++i)
			{
				for (j = 0; j < 4; ++j)
				{
					if (game[i][j] == 'O' || game[i][j] == 'T')
						continue;
					break;
				}
				
				if (j == 4)
				{
					//cout << "Case #" << tnum+1 << ": O won" << endl;
					file << "Case #" << tnum+1 << ": O won" << endl;
					result = true;
					break;
				}
			}
		}

		if (!result)
		{
			for (int i = 0; i < 4; ++i)
			{
				for (j = 0; j < 4; ++j)
				{
					if (game[j][i] == 'X' || game[j][i] == 'T')
						continue;
					break;
				}
				
				if (j == 4)
				{
					//cout << "Case #" << tnum+1 << ": X won" << endl;
					file << "Case #" << tnum+1 << ": X won" << endl;
					result = true;
					break;
				}
			}
		}

		if (!result)
		{
			for (int i = 0; i < 4; ++i)
			{
				for (j = 0; j < 4; ++j)
				{
					if (game[j][i] == 'O' || game[j][i] == 'T')
						continue;
					break;
				}
				
				if (j == 4)
				{
					//cout << "Case #" << tnum+1 << ": O won" << endl;
					file << "Case #" << tnum+1 << ": O won" << endl;
					result = true;
					break;
				}
			}
		}


		if (!result)
		{
			for (j = 0; j < 4; ++j)
			{
				if (game[j][j] == 'X' || game[j][j] == 'T')
					continue;
				break;
			}
			
			if (j == 4)
			{
				//cout << "Case #" << tnum+1 << ": X won" << endl;
				file << "Case #" << tnum+1 << ": X won" << endl;
				result = true;
			}
		}

		if (!result)
		{
			for (j = 0; j < 4; ++j)
			{
				if (game[j][j] == 'O' || game[j][j] == 'T')
					continue;
				break;
			}
			
			if (j == 4)
			{
				//cout << "Case #" << tnum+1 << ": O won" << endl;
				file << "Case #" << tnum+1 << ": O won" << endl;
				result = true;
			}
		}

		if (!result)
		{
			for (j = 0; j < 4; ++j)
			{
				if (game[j][3-j] == 'X' || game[j][3-j] == 'T')
					continue;
				break;
			}
			
			if (j == 4)
			{
				//cout << "Case #" << tnum+1 << ": X won" << endl;
				file << "Case #" << tnum+1 << ": X won" << endl;
				result = true;
			}
		}

		if (!result)
		{
			for (j = 0; j < 4; ++j)
			{
				if (game[j][3-j] == 'O' || game[j][3-j] == 'T')
					continue;
				break;
			}
			
			if (j == 4)
			{
				//cout << "Case #" << tnum+1 << ": O won" << endl;
				file << "Case #" << tnum+1 << ": O won" << endl;
				result = true;
			}
		}

		if (!result)
		{
			int count = 0;
			for (int i = 0; i < 4; ++i)
			{
				for (j = 0; j < 4; ++j)
				{
					if (game[i][j] == '.')
						count++;
				}
			}

			if (count)
				//cout << "Case #" << tnum+1 << ": Game has not completed" << endl;
				file << "Case #" << tnum+1 << ": Game has not completed" << endl;
			else
				//cout << "Case #" << tnum+1 << ": Draw" << endl;
				file << "Case #" << tnum+1 << ": Draw" << endl;
		}

		++tnum;
		result = false;
	}
}