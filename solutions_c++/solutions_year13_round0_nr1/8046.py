#include "StdAfx.h"
#include "ReadInputFile.cpp"
#include <iostream>
#include <fstream>

using namespace std;

class TicTacToeSolver 
{
	ReadInputFile rf;
	

public :

	void SolveTicTacToe ( int argc, _TCHAR* argv[] )
	{		
		std::string input = std::string (argv[2]);
		std::string output = std::string (argv[3]);
				
		std::ofstream outfile (output);

		rf.init(input);

		int total_num_test_case = 0;
		if ( !rf.ReadNumberOfTestCases(total_num_test_case) )
			return;

		int current_case_number = 0;

		int num_ = 4;

		std::vector<std::string> cases;
		while (rf.ReadNextTestCase(num_, cases))
		{
			// std::cout << " In a whilie loop " << std::endl;
			std::cout << "cases size " << cases.size()<< std::endl;

			current_case_number++;
			bool result = false;
			bool game_uncomplete = false;
			int row_total = 0;
			int col_total = 0;
			int diagonal_total_1 = 0;
			int diagonal_total_2 = 0;

			std::string winner;

			for ( int i = 0; i < num_; i++ )
			{
				result = false;
				row_total = 0;
				col_total = 0;				

				for ( int j = 0; j < num_; j++ )
				{
					// std::cout << "j: " << j << std::endl;

					if ( cases[i][j] == 'X')
						row_total += 10;

					else if ( cases[i][j] == 'O' )
						row_total += 0;

					else if ( cases[i][j] == 'T' )
						row_total += 100;

					else if ( cases[i][j] == '.' )
						row_total += 1000;

					// std::cout << "row_total: " << row_total << std::endl;

					if ( cases[j][i] == 'X')
						col_total += 10;

					else if ( cases[j][i] == 'O' )
						col_total += 0;

					else if ( cases[j][i] == 'T' )
						col_total += 100;

					else if ( cases[j][i] == '.' )
						col_total += 1000;

					// std::cout << "col_total: " << col_total << std::endl;

					if ( i == j )
					{
						if ( cases[i][i] == 'X')
							diagonal_total_1 += 10;

						else if ( cases[i][i] == 'O' )
							diagonal_total_1 += 0;

						else if ( cases[i][i] == 'T' )
							diagonal_total_1 += 100;

						else if ( cases[i][i] == '.' )
							diagonal_total_1 += 1000;

						// std::cout << "diagonal_total_1: " << diagonal_total_1 << std::endl;

						if ( cases[i][num_ - i - 1] == 'X')
							diagonal_total_2 += 10;

						else if ( cases[i][num_ - i - 1] == 'O' )
							diagonal_total_2 += 0;

						else if ( cases[i][num_ - i - 1] == 'T' )
							diagonal_total_2 += 100;

						else if ( cases[i][num_ - i - 1] == '.' )
							diagonal_total_2 += 1000;
					}

					// std::cout << "diagonal_total_1: " << diagonal_total_1 << std::endl;
					// std::cout << "diagonal_total_2: " << diagonal_total_2 << std::endl;
				}

				std::cout << "Row_total: " << row_total << std::endl;

				if ( row_total > 1000 || col_total > 1000 )
					game_uncomplete = true;

				if ( (row_total == 0) || (row_total == 100) || (col_total == 0) || (col_total == 100) )
				{
					result = true;					
					winner = "O";
					break;
				}
				else if ( (row_total == 40) || (row_total == 130) || (col_total == 40) || (col_total == 130) )
				{
					result = true;					
					winner = "X";
					break;
				}
			}

			if ( (diagonal_total_1 == 0) || (diagonal_total_1 == 100) || (diagonal_total_2 == 0) || (diagonal_total_2 == 100) )
			{
				result = true;					
				winner = "O";
				// break;
			}
			else if ( (diagonal_total_1 == 40) || (diagonal_total_1 == 130) || (diagonal_total_2 == 40) || (diagonal_total_2 == 130) )
			{
				result = true;					
				winner = "X";
				// break;
			}

			if ( result == true )
			{
				outfile << "Case #" << current_case_number << ": " << winner << " won" << std::endl;			
			}
			else 
			{
				if (game_uncomplete == false)
					outfile << "Case #" << current_case_number << ": " << "Draw" <<  std::endl;
				else
					outfile << "Case #" << current_case_number << ": " << "Game has not completed" <<  std::endl;
			}
			cases.clear();

			rf.ReadEmptyLine ();
		}

		rf.CloseFile();
	}	

};

