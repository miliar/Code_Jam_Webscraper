#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int testCase = 0;

	ifstream infile;
	ofstream outfile;

	infile.open("A-large.in", ios::in);
	outfile.open("result_large.out", ios::out);

	infile >> testCase;

	for(int i = 0; i < testCase; i++)
	{
		char board[4][4] = {0,};
		int score[3][4] = {0, };
		bool isFull = true;

		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				infile >> board[j][k];
				score[0][j] += board[j][k];
				score[1][k] += board[j][k];
			}
		}

		for(int j = 0; j < 4; j++)
		{
			score[2][0] += board[j][j];
			score[2][1] += board[3-j][j];
		}

		outfile << "Case #" << i + 1 << ": ";

		try{
			for(int j = 0; j < 3; j++)
			{
				for(int k = 0; k < 4; k++)
				{
					switch(score[j][k])
					{
					case 352:
					case 348:
						throw 352;
						break;
					case 316:
					case 321:
						throw 316;
						break;
					default:
						if(score[j][k] && score[j][k] < 315)
						{
							isFull = false;
						}
					}
				}
			}
		}catch(int exp){
			if(exp == 352)
				outfile << "X won" << endl;
			else if(exp == 316)
				outfile << "O won" << endl;

			continue;
		}

		if(isFull)
		{
			outfile << "Draw" << endl;
		}else{
			outfile << "Game has not completed" << endl;
		}
	}

	infile.close();
	outfile.close();

	return 0;
}