#include <iostream> 
#include <vector>
#include <string>

using namespace std;

int main()
{
	vector<int> xVec(10,0);
	vector<int> oVec(10,0);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		for (int v = 0; v < xVec.size(); v++)
		{
			xVec[v] = 0; oVec[v] = 0;
		}
		string str;
		bool hasDot = false;
		bool xIsWon = false;
		bool oIsWon = false;
		for (int j = 0; j < 4; j++)
		{
			cin >> str;
			for (int k = 0; k < 4 && !xIsWon && !oIsWon; k++)
			{
				if (str[k] == 'X') 
				{
					xVec[j] += 1;
					xVec[k + 4] += 1;
					if (k == j) xVec[8] += 1;
					if (k + j == 3) xVec[9] += 1;
					if (xVec[j] == 4 || xVec[k+4] == 4 || xVec[8] == 4 || xVec[9] == 4)
						xIsWon = true;
				}
				if (str[k] == 'O')
				{
					oVec[j] += 1;
					oVec[k + 4] += 1;
					if (k == j) oVec[8] += 1;
					if (k + j == 3) oVec[9] += 1;
					if (oVec[j] == 4 || oVec[k+4] == 4 || oVec[8] == 4 || oVec[9] == 4)
						oIsWon = true;
				}
				if (str[k] == 'T')
				{
					xVec[j] += 1;     
					oVec[j] += 1;
					xVec[k + 4] += 1; 
					oVec[k + 4] += 1;
					if (k == j) xVec[8] += 1;
					if (k == j) oVec[8] += 1;
					if (k + j == 3) xVec[9] += 1;
					if (k + j == 3) oVec[9] += 1;
					if (oVec[j] == 4 || oVec[k+4] == 4 || oVec[8] == 4 || oVec[9] == 4)
						oIsWon = true;
					if (xVec[j] == 4 || xVec[k+4] == 4 || xVec[8] == 4 || xVec[9] == 4)
						xIsWon = true;
				}
				if (!hasDot && str[k] == '.')
				{
					hasDot = true;
				}
			}
		}

		if (xIsWon){
			cout << "Case #" << i+1 << ": X won" << endl;
			continue;
		}else if (oIsWon)
		{
			cout << "Case #" << i+1 << ": O won" << endl;
			continue;
		}
		if (hasDot){
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
		}else{
			cout << "Case #" << i+1 << ": Draw" << endl;
		}

	}
	return 0;
}

