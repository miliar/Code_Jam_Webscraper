#include <iostream>
#include <fstream>

using namespace std;

enum RESULT { X, D, O, G };

RESULT result(char flag){
	if (flag == 'X')
	{
		return X;
	}
	else
		return O;
}


RESULT determine(char board[][4]){
	bool Complete = true;


	for (int i = 0; i < 4; ++i)
	{
		char flag = board[i][0] == 'T' ? board[i][1] : board[i][0];
		bool ok = true;

		for (int j = 0; j < 4; ++j)
		{
			if (flag=='.' || (flag != board[i][j] && board[i][j] != 'T'))
			{
				ok = false;
				if(flag == '.')
				Complete = false;
				break;
			}
			if(board[i][j] == '.'){
				ok = false;
				Complete = false;
				break;
			}
		}

		if (ok)
		{
			return result(flag);
		}
	}



	for (int i = 0; i < 4; ++i)
	{
		char flag = board[0][i] == 'T' ? board[1][i] : board[0][i];
		bool ok = true;

		for (int j = 0; j < 4; ++j)
		{
			if (flag=='.' || (flag != board[j][i] && board[j][i] != 'T'))
			{
				ok = false;
				if(flag == '.')
				Complete = false;
				break;
			}
			if(board[j][i] == '.'){
				ok = false;
				Complete = false;
				break;
			}
		}

		if (ok)
		{
			return result(flag);
		}
	}

	char flag;
	flag = board[0][0] == 'T' ? board[1][1] : board[0][0];
	
	bool ok = true;
	for (int i = 1; i < 4; ++i)
	{
		if(flag=='.' || (flag != board[i][i] && board[i][i] != 'T')){
			ok = false;
			if(flag == '.'){
				Complete = false;
			}
			break;
		}
		if (board[i][i] == '.')
		{
			ok = false;
			Complete = false;
			break;
		}
	}
	if (ok)
	{
		return result(flag);
	}


	flag = board[0][3];
	if (flag == 'T')
	{
		flag = board[1][2];
	}
	ok = true;
	for (int i = 1; i < 4; ++i)
	{
		if(flag == '.' || flag != board[i][3-i] && board[i][3-i] != 'T'){
			ok = false;
			if(flag == '.'){
				Complete = false;
			}
			break;
		}
		if (board[i][3-i] == '.')
		{
			ok = false;
			Complete = false;
			break;
		}
	}
	if (ok)
	{
		return result(flag);
	}

	if(!Complete)
		return G;
	else
		return D;
}

int main(int argc, char const *argv[])
{
	string line;
	ifstream inputf("A-small-attempt0.in");
	ofstream outputf("A-small-attempt0.out");
	if (inputf.is_open())
	{
		getline(inputf,line);
		int nbCase = atoi(line.c_str());

		for (int c = 0; c < nbCase; ++c)
		{
			char board[4][4];
			for (int i = 0; i < 4; ++i)
			{
				getline(inputf,line);
				for (int k = 0; k < 4; ++k)
				{
					board[i][k] = line[k];
				}
			}
			getline(inputf, line);
			RESULT r = determine(board);

			if (r == X)
			{
				outputf<< "Case #" << c+1 << ": X won" << endl;
			}
			if (r == O)
			{
				outputf<< "Case #" << c+1 << ": O won" << endl;
			}
			if (r == G)
			{
				outputf<< "Case #" << c+1 << ": Game has not completed" << endl;
			}
			if (r == D)
			{
				outputf<< "Case #" << c+1 << ": Draw" << endl;
			}
		}

		inputf.close();
		outputf.close();
	}
	return 0;
}