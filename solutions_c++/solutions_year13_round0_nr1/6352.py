#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream input_file("A-large.in");
	ofstream output_file("A-large.out");

	int O_player_moves_rows[4];
	int O_player_moves_cols[4];
	int O_player_moves_ldig;
	int O_player_moves_udig;
	int X_player_moves_rows[4];
	int X_player_moves_cols[4];
	int X_player_moves_ldig;
	int X_player_moves_udig;
	char move;
	bool bPlayerOWins;
	bool bPlayerXWins;
	int numRemainingMoves;

	int numTestCases;

	//get the number of test cases
	input_file >> numTestCases;
	input_file.get();

	cout << "There are " << numTestCases << " test cases." << endl;

	//iterate over the test cases
	for (int t = 0; t<numTestCases; ++t)
	{
		//reset the board
		for (int i = 0; i<4; ++i)
		{
			O_player_moves_rows[i]=0;
			O_player_moves_cols[i]=0;
			X_player_moves_rows[i]=0;
			X_player_moves_cols[i]=0;
		}
		O_player_moves_ldig=0;
		O_player_moves_udig=0;
		X_player_moves_ldig=0;
		X_player_moves_udig=0;

		bPlayerOWins=false;
		bPlayerXWins=false;

		numRemainingMoves=0;

		//get the actual data
		for (int j=0; j<4; ++j)
		{
			for (int i = 0; i<4; ++i)
			{
				move = input_file.get();
				//cout << move;
				switch(move)
				{
				case 'X':
					X_player_moves_rows[j]++;
					X_player_moves_cols[i]++;
					if (i==j)
					{
						X_player_moves_ldig++;
					} else if ((i+j)==3){
						X_player_moves_udig++;
					}
					//cout << "X";
					break;
				case 'O':
					O_player_moves_rows[j]++;
					O_player_moves_cols[i]++;
					if (i==j)
					{
						O_player_moves_ldig++;
					} else if ((i+j)==3){
						O_player_moves_udig++;
					}
					//cout << "O";
					break;
				case 'T':
					X_player_moves_rows[j]++;
					X_player_moves_cols[i]++;
					O_player_moves_rows[j]++;
					O_player_moves_cols[i]++;
					if (i==j)
					{
						X_player_moves_ldig++;
						O_player_moves_ldig++;
					} else if ((i+j)==3){
						X_player_moves_udig++;
						O_player_moves_udig++;
					}
					//cout << "T";
					break;
				case '.':
					numRemainingMoves++;
					//cout << ".";
					break;
				default:
					break;
				}
			}
			input_file.get();
			//cout << endl;
		}
		input_file.get();

		for (int i = 0; (i<4) && (!bPlayerOWins && !bPlayerXWins); ++i)
		{
			if ((O_player_moves_rows[i]==4) ||
				(O_player_moves_cols[i]==4))
			{
				bPlayerOWins=true;
			}
			if ((X_player_moves_rows[i]==4) ||
				(X_player_moves_cols[i]==4))
			{
				bPlayerXWins=true;
			}
		}
		if (!bPlayerOWins && !bPlayerXWins)
		{
			if ((O_player_moves_ldig==4) ||
				(O_player_moves_udig==4))
			{
				bPlayerOWins=true;
			}
			if ((X_player_moves_ldig==4) ||
				(X_player_moves_udig==4))
			{
				bPlayerXWins=true;
			}
		}
/*
		cout << "O_player_moves_ldig: " << O_player_moves_ldig << endl;
		cout << "O_player_moves_udig: " << O_player_moves_udig << endl;
		cout << "X_player_moves_ldig: " << X_player_moves_ldig << endl;
		cout << "X_player_moves_udig: " << X_player_moves_udig << endl;
		cout << "bPlayerOWins: " << bPlayerOWins << endl;
		cout << "bPlayerXWins: " << bPlayerXWins << endl;
		cout << "Num remaining moves: " << numRemainingMoves << endl;
*/
		output_file << "Case #" << t +1 << ": ";

		if (bPlayerOWins){
			output_file << "O won" << endl;
		} else if (bPlayerXWins){
			output_file << "X won" << endl;
		} else if (numRemainingMoves==0){
			output_file << "Draw" << endl;
		} else {
			output_file << "Game has not completed" << endl;
		}
	}

	input_file.close();
	output_file.close();

	return 0;
}
