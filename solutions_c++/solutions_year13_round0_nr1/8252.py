#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	//variable set
	int numberOfCases;
	string line1, line2, line3, line4, inFileName, outFileName;
	char board [4][4];
	bool is_draw=true;
	bool cutOffScan=false;

	char &rBoardCell_00=board[0][0];
	char &rBoardCell_10=board[1][0];
	char &rBoardCell_20=board[2][0];
	char &rBoardCell_30=board[3][0];
	char &rBoardCell_01=board[0][1];
	char &rBoardCell_11=board[1][1];
	char &rBoardCell_21=board[2][1];
	char &rBoardCell_31=board[3][1];
	char &rBoardCell_02=board[0][2];
	char &rBoardCell_12=board[1][2];
	char &rBoardCell_22=board[2][2];
	char &rBoardCell_32=board[3][2];
	char &rBoardCell_03=board[0][3];
	char &rBoardCell_13=board[1][3];
	char &rBoardCell_23=board[2][3];
	char &rBoardCell_33=board[3][3];



	//get input file name
	cout<<"Enter Input File Name: ";
	cin>>inFileName;
	//get output file name
	cout<<endl<<"Enter Output File Name: ";
	cin>>outFileName;

	//enter line
	cout<<endl;

	//open input file
	ifstream inDoc (inFileName);
	
	//test if file is open
	if (!inDoc.is_open())
	{
		//tell the user name is wrong and return an error code.
		cerr<<"False file name"<<endl;
		inDoc.close();
		cin>>inFileName;
		return 1;
	}

	//open output file
	ofstream outDoc (outFileName);

	//get number of cases
	inDoc>>numberOfCases;

	//start main loop
	for (int caseCounter=1; caseCounter<=numberOfCases; caseCounter++)
	{
		//output case line
		outDoc<<"Case #"<<caseCounter<<": ";

		//set is_draw to true
		is_draw=true;

		//set cutOffScan to false
		cutOffScan=false;

		//take in array lines
		inDoc>>line1;
		inDoc>>line2;
		inDoc>>line3;
		inDoc>>line4;
		
		//row1
		board[0][0]=line1[0];
		board[0][1]=line1[1];
		board[0][2]=line1[2];
		board[0][3]=line1[3];

		//row2
		board[1][0]=line2[0];
		board[1][1]=line2[1];
		board[1][2]=line2[2];
		board[1][3]=line2[3];

		//row3
		board[2][0]=line3[0];
		board[2][1]=line3[1];
		board[2][2]=line3[2];
		board[2][3]=line3[3];

		//row4
		board[3][0]=line4[0];
		board[3][1]=line4[1];
		board[3][2]=line4[2];
		board[3][3]=line4[3];


		//test horizontals
		for (int rowCounter=0; rowCounter<=3; rowCounter++)
		{
			//if all are X or O
			if ((board[rowCounter][ 0]=='O' && board[rowCounter][ 1]=='O' && board[rowCounter][ 2]=='O' && board[rowCounter][ 3]=='O') || (board[rowCounter][ 0]=='X' && board[rowCounter][ 1]=='X' && board[rowCounter][ 2]=='X' && board[rowCounter][ 3]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;
				
				//if x won
				if (board[rowCounter][ 0]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 1
			if ((board[rowCounter][0]=='T' && board[rowCounter][ 1]=='O' && board[rowCounter][ 2]=='O' && board[rowCounter][ 3]=='O') || (board[rowCounter][ 0]=='T' && board[rowCounter][ 1]=='X' && board[rowCounter][ 2]=='X' && board[rowCounter][ 3]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[rowCounter][ 1]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 2
			if ((board[rowCounter][ 0]=='O' && board[rowCounter][ 1]=='T' && board[rowCounter][ 2]=='O' && board[rowCounter][ 3]=='O') || (board[rowCounter][ 0]=='X' && board[rowCounter][ 1]=='T' && board[rowCounter][ 2]=='X' && board[rowCounter][ 3]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[rowCounter][ 0]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 3
			if ((board[rowCounter][ 0]=='O' && board[rowCounter][ 1]=='O' && board[rowCounter][ 2]=='T' && board[rowCounter][ 3]=='O') || (board[rowCounter][ 0]=='X' && board[rowCounter][ 1]=='X' && board[rowCounter][ 2]=='T' && board[rowCounter][ 3]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[rowCounter][ 0]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 4
			if ((board[rowCounter][ 0]=='O' && board[rowCounter][ 1]=='O' && board[rowCounter][ 2]=='O' && board[rowCounter][ 3]=='T') || (board[rowCounter][ 0]=='X' && board[rowCounter][ 1]=='X' && board[rowCounter][ 2]=='X' && board[rowCounter][ 3]=='T'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[rowCounter][ 0]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}
		}

		//Test verticals


		for (int columnCounter=0; columnCounter<=3; columnCounter++)
		{
			//if all are X or O
			if ((board[0][columnCounter]=='O' && board[1][columnCounter]=='O' && board[2][columnCounter]=='O' && board[3][columnCounter]=='O') || (board[0][columnCounter]=='X' && board[1][columnCounter]=='X' && board[2][columnCounter]=='X' && board[3][columnCounter]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;
				
				//if x won
				if (board[0][columnCounter]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 1
			if ((board[0][columnCounter]=='T' && board[1][columnCounter]=='O' && board[2][columnCounter]=='O' && board[3][columnCounter]=='O') || (board[0][columnCounter]=='T' && board[1][columnCounter]=='X' && board[2][columnCounter]=='X' && board[3][columnCounter]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[1][columnCounter]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 2
			if ((board[0][columnCounter]=='O' && board[1][columnCounter]=='T' && board[2][columnCounter]=='O' && board[3][columnCounter]=='O') || (board[0][columnCounter]=='X' && board[1][columnCounter]=='T' && board[2][columnCounter]=='X' && board[3][columnCounter]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[0][columnCounter]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 3
			if ((board[0][columnCounter]=='O' && board[1][columnCounter]=='O' && board[2][columnCounter]=='T' && board[3][columnCounter]=='O') || (board[0][columnCounter]=='X' && board[1][columnCounter]=='X' && board[2][columnCounter]=='T' && board[3][columnCounter]=='X'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[0][columnCounter]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}

			//if T pos 4
			if ((board[0][columnCounter]=='O' && board[1][columnCounter]=='O' && board[2][columnCounter]=='O' && board[3][columnCounter]=='T') || (board[0][columnCounter]=='X' && board[1][columnCounter]=='X' && board[2][columnCounter]=='X' && board[3][columnCounter]=='T'))
			{
				//set is_draw to true
				is_draw=false;
				cutOffScan=true;

				//if x won
				if (board[0][columnCounter]=='X')
				{
					outDoc<<"X won"<<endl;
				}
				else
				{
					//of O won
					outDoc<<"O won"<<endl;
				}
				break;
			}
		}



		//test diagonals
		//upper left to lower right
		//if all X/O
		if (((board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='O' && board[3][3]=='O') || (board[0][0]=='X' && board[1][1]=='X' && board[2][2]=='X' && board[3][3]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][0]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 1
		if (((board[0][0]=='T' && board[1][1]=='O' && board[2][2]=='O' && board[3][3]=='O') || (board[0][0]=='T' && board[1][1]=='X' && board[2][2]=='X' && board[3][3]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[1][1]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 2
		if (((board[0][0]=='O' && board[1][1]=='T' && board[2][2]=='O' && board[3][3]=='O') || (board[0][0]=='X' && board[1][1]=='T' && board[2][2]=='X' && board[3][3]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][0]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 3
		if (((board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='T' && board[3][3]=='O') || (board[0][0]=='X' && board[1][1]=='X' && board[2][2]=='T' && board[3][3]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][0]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 4
		if (((board[0][0]=='O' && board[1][1]=='O' && board[2][2]=='O' && board[3][3]=='T') || (board[0][0]=='X' && board[1][1]=='X' && board[2][2]=='X' && board[3][3]=='T')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][0]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}


		//upper right to lower left
		if (((board[0][3]=='O' && board[1][2]=='O' && board[2][1]=='O' && board[3][0]=='O') || (board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='X' && board[3][0]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][3]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 1
		if (((board[0][3]=='T' && board[1][2]=='O' && board[2][1]=='O' && board[3][0]=='O') || (board[0][3]=='T' && board[1][2]=='X' && board[2][1]=='X' && board[3][0]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[1][2]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 2
		if (((board[0][3]=='O' && board[1][2]=='T' && board[2][1]=='O' && board[3][0]=='O') || (board[0][3]=='X' && board[1][2]=='T' && board[2][1]=='X' && board[3][0]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][3]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 3
		if (((board[0][3]=='O' && board[1][2]=='O' && board[2][1]=='T' && board[3][0]=='O') || (board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='T' && board[3][0]=='X')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][3]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}

		//T pos 4
		if (((board[0][3]=='O' && board[1][2]=='O' && board[2][1]=='O' && board[3][0]=='T') || (board[0][3]=='X' && board[1][2]=='X' && board[2][1]=='X' && board[3][0]=='T')) && cutOffScan==false)
		{
			//set is_draw to true
			is_draw=false;
			cutOffScan=true;

			if (board[0][3]=='O')
			{
				//if O won
				outDoc<<"O won"<<endl;
			}
			else
			{
				//if X won
				outDoc<<"X won"<<endl;
			}
		}



		//if nothing has been triggered, trigger draw.

		if (is_draw==true)
		{
			//check for completion
			for (int rowCounter=0; rowCounter<=3; rowCounter++)
			{
				for (int columnCounter=0; columnCounter<=3; columnCounter++)
				{
					if (board[rowCounter][columnCounter]=='.')
						is_draw=false;
				}
			}
			
			if (is_draw==true)
			{
				outDoc<<"Draw"<<endl;
			}
			else
			{
				outDoc<<"Game has not completed"<<endl;
			}
		}
		//start next case
	}

	//tell the user we're done
	cout<<"Done"<<endl;

	//wait for user response
	cin>>inFileName;

	//close files
	inDoc.close();
	outDoc.close();

	//return and exit
	return 0;
}