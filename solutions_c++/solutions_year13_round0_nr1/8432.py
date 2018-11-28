#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char ** argv, char * arge[]) try
{
	//stack <char *> wordStack;	
	ifstream inputFile(argv[1]);	
	if (inputFile.is_open())
  {
		//get the first line for N number of test cases;
		int n = 0;
		inputFile >> n;
		//cout << "num of line : " << n << endl; 
		inputFile.get();// go ahead of '\n'
		int numOfCases = 0;	
		char ** FourByFour = 0;
		FourByFour = new char * [4];
		for (int i=0; i < 4; ++i)
		{
			FourByFour[i] = new char[4];
		}

		string message[4];
		message[0] = "X won";
		message[1] = "O won";
		message[2] = "Draw";
		message[3] = "Game has not completed"; 

    do { //for each test case
			if (numOfCases++ >= n ) break;
			int totalX = 0;
			int totalO = 0;
			int totalDot = 0;
			int row = 0;
			int col = 0;
			int indexOfMessage = -1;
			bool gotAnswer = false;
			bool isTglobal = false;
			bool isDotInLine = false;
			bool isTInLine = false;
			bool isDotInCol[4] = {false};
			bool isDiagonalStillValid = true;
			int totalNumOfChars = 0;

			do {
				gotAnswer = false;
		  	int c = inputFile.get();
				if ( (char)(c) == '\n') //read a line. last line must always be empty before EOF
				{
				  //Test for each line
					col = 0;
					switch(++row)
					{
						case 1: //only first row. if all X OR all O OR 3 X / O with one T
							if (isTInLine)
							{
								isTglobal = true;	
							}
							if (isDotInLine) break;
							if (isTInLine)
							{
								//isTglobal = true;
								if ((FourByFour[0][0] == 'X' || FourByFour[0][0] == 'T') && 
								    (FourByFour[0][1] == 'X' || FourByFour[0][1] == 'T') && 
								    (FourByFour[0][2] == 'X' || FourByFour[0][2] == 'T') &&
								    (FourByFour[0][3] == 'X' || FourByFour[0][3] == 'T'))
								{
									gotAnswer = true;
									cout << "Case #" << numOfCases << ": " << message[0] << endl;
								}
								else if ((FourByFour[0][0] == 'O' || FourByFour[0][0] == 'T') && 
								    (FourByFour[0][1] == 'O' || FourByFour[0][1] == 'T') && 
								    (FourByFour[0][2] == 'O' || FourByFour[0][2] == 'T') &&
								    (FourByFour[0][3] == 'O' || FourByFour[0][3] == 'T'))
								{
									gotAnswer = true;
									cout << "Case #" << numOfCases << ": " << message[1] << endl;
								}
							} else //No 'T'
							{
								if ((FourByFour[0][0] == FourByFour[0][1]) && 
								    (FourByFour[0][1] == FourByFour[0][2]) &&
								    (FourByFour[0][2] == FourByFour[0][3]))
								{
									gotAnswer = true;
									if (FourByFour[0][0] == 'X')
									{
										cout << "Case #" << numOfCases << ": " << message[0].c_str() << endl;
									}
									else
									{
										cout << "Case #" << numOfCases << ": " << message[1].c_str() << endl;
									}
								}
							}
							break;
						case 2: //Only second row AND this row is enough to prove should we proceed or not
								if (isDotInLine == false)
								{
									if (isTglobal || (isTInLine == false)) // that means we already have a T in the board earlier. Then only test for 'X' or 'O'
									{
										if ((FourByFour[1][0] == 'O') && 
										    (FourByFour[1][1] == 'O') && 
										    (FourByFour[1][2] == 'O') && 
										    (FourByFour[1][3] == 'O'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[1].c_str() << endl; 
										}
										else if ((FourByFour[1][0] == 'X') && 
										    (FourByFour[1][1] == 'X') && 
										    (FourByFour[1][2] == 'X') && 
										    (FourByFour[1][3] == 'X'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[0].c_str() << endl; 
										}
									}
									else 
									{
										isTglobal = true;
										if ((FourByFour[1][0] == 'X' || FourByFour[1][0] == 'T') && 
										    (FourByFour[1][1] == 'X' || FourByFour[1][1] == 'T') && 
										    (FourByFour[1][2] == 'X' || FourByFour[1][2] == 'T') &&
										    (FourByFour[1][3] == 'X' || FourByFour[1][3] == 'T'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[0] << endl;
										}
										else if ((FourByFour[1][0] == 'O' || FourByFour[1][0] == 'T') && 
										    (FourByFour[1][1] == 'O' || FourByFour[1][1] == 'T') && 
										    (FourByFour[1][2] == 'O' || FourByFour[1][2] == 'T') &&
										    (FourByFour[1][3] == 'O' || FourByFour[1][3] == 'T'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[1] << endl;
										}
									}
								}
								if (isTInLine)
								{
									isTglobal = true;
								}
							break;
						case 3: //Only third row.
								if (isDotInLine == false)
								{
									if (isTglobal || (isTInLine == false)) // that means we already have a T in the board earlier. Then only test for 'X' or 'O'
									{
										if ((FourByFour[2][0] == 'O') && 
										    (FourByFour[2][1] == 'O') && 
										    (FourByFour[2][2] == 'O') && 
										    (FourByFour[2][3] == 'O'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[1].c_str() << endl; 
										}
										else if ((FourByFour[2][0] == 'X') && 
										    (FourByFour[2][1] == 'X') && 
										    (FourByFour[2][2] == 'X') && 
										    (FourByFour[2][3] == 'X'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[0].c_str() << endl; 
										}
									}
									else 
									{
										isTglobal = true;
										if ((FourByFour[2][0] == 'X' || FourByFour[2][0] == 'T') && 
										    (FourByFour[2][1] == 'X' || FourByFour[2][1] == 'T') && 
										    (FourByFour[2][2] == 'X' || FourByFour[2][2] == 'T') &&
										    (FourByFour[2][3] == 'X' || FourByFour[2][3] == 'T'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[0] << endl;
										}
										else if ((FourByFour[2][0] == 'O' || FourByFour[2][0] == 'T') && 
										    (FourByFour[2][1] == 'O' || FourByFour[2][1] == 'T') && 
										    (FourByFour[2][2] == 'O' || FourByFour[2][2] == 'T') &&
										    (FourByFour[2][3] == 'O' || FourByFour[2][3] == 'T'))
										{
											gotAnswer = true;
											cout << "Case #" << numOfCases << ": " << message[1] << endl;
										}
									}
								}
								if (isTInLine)
								{
									isTglobal = true;
								}
							break;
						case 4: //This row, all columns and both diagonals whether game is valid or drawn
							if (totalX < 3 || ((totalX == 3) && (isTInLine == false)))
							{
								gotAnswer = true;
								cout << "Case #" << numOfCases << ": " << message[3] << endl;
								break;
							}
							if (totalO < 2 || ((totalO == 2) && (isTInLine == false)))
							{
								gotAnswer = true;
								cout << "Case #" << numOfCases << ": " << message[3] << endl;
								break;
							}
							//Check for columns now
							for (int i=0; i < 4; ++i)
							{
								if (isDotInCol[i]) continue;
								if ((FourByFour[0][i] == 'O' || FourByFour[0][i] == 'T') &&
								    (FourByFour[1][i] == 'O' || FourByFour[1][i] == 'T') &&
								    (FourByFour[2][i] == 'O' || FourByFour[2][i] == 'T') &&
								    (FourByFour[3][i] == 'O' || FourByFour[3][i] == 'T'))
								{
									gotAnswer = true;
									cout << "Case #" << numOfCases << ": " << message[1] << endl;
									break;
								}
								if ((FourByFour[0][i] == 'X' || FourByFour[0][i] == 'T') &&
								    (FourByFour[1][i] == 'X' || FourByFour[1][i] == 'T') &&
								    (FourByFour[2][i] == 'X' || FourByFour[2][i] == 'T') &&
								    (FourByFour[3][i] == 'X' || FourByFour[3][i] == 'T'))
								{
									gotAnswer = true;
									cout << "Case #" << numOfCases << ": " << message[0] << endl;
									break;
								}
							}
							//if (isDotInLine) //diagonals only
							//{
									if ((FourByFour[0][0] == 'X' || FourByFour[0][0] == 'T') &&
									    (FourByFour[1][1] == 'X' || FourByFour[1][1] == 'T') &&
									    (FourByFour[2][2] == 'X' || FourByFour[2][2] == 'T') &&
									    (FourByFour[3][3] == 'X' || FourByFour[3][3] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[0] << endl;
										break;
									}
									if ((FourByFour[0][0] == 'O' || FourByFour[0][0] == 'T') &&
									    (FourByFour[1][1] == 'O' || FourByFour[1][1] == 'T') &&
									    (FourByFour[2][2] == 'O' || FourByFour[2][2] == 'T') &&
									    (FourByFour[3][3] == 'O' || FourByFour[3][3] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[1] << endl;
										break;
									}
									if ((FourByFour[0][3] == 'X' || FourByFour[0][3] == 'T') &&
									    (FourByFour[1][2] == 'X' || FourByFour[1][2] == 'T') &&
									    (FourByFour[2][1] == 'X' || FourByFour[2][1] == 'T') &&
									    (FourByFour[3][0] == 'X' || FourByFour[3][0] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[0] << endl;
										break;
									}
									if ((FourByFour[0][3] == 'O' || FourByFour[0][3] == 'T') &&
									    (FourByFour[1][2] == 'O' || FourByFour[1][2] == 'T') &&
									    (FourByFour[2][1] == 'O' || FourByFour[2][1] == 'T') &&
									    (FourByFour[3][0] == 'O' || FourByFour[3][0] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[1] << endl;
										break;
									}
						//	}
							//else // check for row
							if (!isDotInLine) 
							{
									if ((FourByFour[3][0] == 'X' || FourByFour[3][0] == 'T') &&
									    (FourByFour[3][1] == 'X' || FourByFour[3][1] == 'T') &&
									    (FourByFour[3][2] == 'X' || FourByFour[3][2] == 'T') &&
									    (FourByFour[3][3] == 'X' || FourByFour[3][3] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[0] << endl;
									}
									else if ((FourByFour[3][0] == 'O' || FourByFour[3][0] == 'T') &&
									    (FourByFour[3][1] == 'O' || FourByFour[3][1] == 'T') &&
									    (FourByFour[3][2] == 'O' || FourByFour[3][2] == 'T') &&
									    (FourByFour[3][3] == 'O' || FourByFour[3][3] == 'T'))
									{
										gotAnswer = true;
										cout << "Case #" << numOfCases << ": " << message[1] << endl;
									}
							}
							if (gotAnswer == false)
							{
								gotAnswer	= true;
								if (totalDot > 0 )
								{
									cout << "Case #" << numOfCases << ": " << message[3] << endl;
								}
								else
								{
									cout << "Case #" << numOfCases << ": " << message[2] << endl;
								}
							}
							break;
					} //switch (++row)
					if (gotAnswer) // move lines ahead
					{
						//read rest of the lines to move to other test case
						for (int i=4; i >= row; --i)
						{
		  				while ((c = inputFile.get()) != '\n');
						}
					}
					isDotInLine = false;
					isTInLine = false;
				} //if EOL
				if (row >= 4 || gotAnswer) break;
				switch (char(c))
				{
					case 'T':
						isTInLine= true;
						FourByFour[row][col++] = 'T';
						++totalNumOfChars;
						break;
					case '.':
						isDotInCol[col] = true;
						FourByFour[row][col++] = '.';
						++totalDot;
						isDotInLine = true;
						++totalNumOfChars;
						break;
					case 'X':
						FourByFour[row][col++] = 'X';
						++totalX;
						++totalNumOfChars;
						break;
					case 'O':
						FourByFour[row][col++] = 'O';
						++totalO;
						++totalNumOfChars;
						break;
				}
			} while (true);
    } while(true);
    inputFile.close();
	}
	return 0;
} catch (...)
{
	cerr << "Uncaught exception..." << endl;
}
