#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

typedef std::vector<std::string> StringVector;

//Since Input in small , going for brute force , else would have apply backtracking
std::string solve_game(const StringVector& gameState)
{
	bool isEmpty = false;
	bool solution_found = false;

	for(short i = 0;i<4;++i) //Check in each row
	{
		if(gameState[i][0] == 'X' || (gameState[i][0] == 'T' && gameState[i][1] == 'X'))
		{
			solution_found = true;
			for(short j = 1;j<4;++j)
			{
				if(gameState[i][j] == 'X' || gameState[i][j] == 'T') ;
				else
				{
					solution_found = false;
					break;
				}
			}

			if(solution_found == true)
			{
				return "X won";
			}
		}
		else if(gameState[i][0] == 'O' || (gameState[i][0] == 'T' && gameState[i][1] == 'O') )
		{
			solution_found = true;
			for(short j = 1;j<4;++j)
			{
				if(gameState[i][j] == 'O' || gameState[i][j] == 'T') ;
				else
				{
					solution_found = false;
					break;
				}
			}

			if(solution_found == true)
			{
				return "O won";
			}
		}
	}

	for(short i = 0;i<4;++i) //Check in each column
	{
		if(gameState[0][i] == 'X' || (gameState[0][i] == 'T' && gameState[1][i] == 'X'))
		{
			solution_found = true;
			for(short j = 1;j<4;++j)
			{
				if(gameState[j][i] == 'X' || gameState[j][i] == 'T') ;
				else
				{
					solution_found = false;
					break;
				}
			}

			if(solution_found == true)
			{
				return "X won";
			}
		}
		else if(gameState[0][i] == 'O' || (gameState[0][i] == 'T' && gameState[1][i] == 'O'))
		{
			solution_found = true;
			for(short j = 1;j<4;++j)
			{
				if(gameState[j][i] == 'O' || gameState[j][i] == 'T') ;
				else
				{
					solution_found = false;
					break;
				}
			}

			if(solution_found == true)
			{
				return "O won";
			}
		}
	}

	// Check for diagonals

	//First Diagonal
	if((gameState[0][0] == 'X' || gameState[0][0] == 'T' ) && (gameState[1][1] == 'X' || gameState[1][1] == 'T' ) 
		&& (gameState[2][2] == 'X' || gameState[2][2] == 'T' ) && (gameState[3][3] == 'X' || gameState[3][3] == 'T' ))
	{
		return "X won";
	}

	if((gameState[0][0] == 'O' || gameState[0][0] == 'T' ) && (gameState[1][1] == 'O' || gameState[1][1] == 'T' ) 
		&& (gameState[2][2] == 'O' || gameState[2][2] == 'T' ) && (gameState[3][3] == 'O' || gameState[3][3] == 'T' ))
	{
		return "O won";
	}

	//Second Diagonal
	if((gameState[3][0] == 'X' || gameState[3][0] == 'T' ) && (gameState[2][1] == 'X' || gameState[2][1] == 'T' ) 
		&& (gameState[1][2] == 'X' || gameState[1][2] == 'T' ) && (gameState[3][0] == 'X' || gameState[3][0] == 'T' ))
	{
		return "X won";
	}

	if((gameState[3][0] == 'O' || gameState[3][0] == 'T' ) && (gameState[2][1] == 'O' || gameState[2][1] == 'T' ) 
		&& (gameState[1][2] == 'O' || gameState[1][2] == 'T' ) && (gameState[3][0] == 'O' || gameState[3][0] == 'T' ))
	{
		return "O won";
	}

	for(short i = 0;i<4;++i)
	{
		for(short j = 0;j<4;++j)
		{
			if(gameState[i][j] == '.')
			{
				isEmpty = true;
				break;
			}
		}
	}
	
	if(isEmpty == true)
	{
		return "Game has not completed";
	}
	else
	{
		return "Draw";
	}
}

int main(void)
{
	short T;
	StringVector gameState;
	std::string inputBuff;

	std::cin>>T;

	for(short i = 1;i<=T;++i)
	{
		gameState.clear();
		for(short j= 0;j<4;++j)
		{
			std::cin>>inputBuff;
			gameState.push_back(inputBuff);
		}

		//std::cin>>inputBuff; //Empty Line

		std::cout<<"Case #"<<i<<": "<<solve_game(gameState)<<std::endl;

		/*for(short j= 0;j<4;++j)
		{
			std::cout<<gameState[j]<<std::endl;
		}*/
	}
	//system("pause");
	return 0;
}
