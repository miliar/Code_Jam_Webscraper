
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
class Board
{//  
private:
	char Matrix[4][4]; //4*4 matrix to represent the chess board

	int winner()
	{
		/*
		return values
		1 x win 
		0 o win
		3 draw 
		2 not completed
		*/
		int xcount =  0;
		int Tcount = 0;
		int ocount = 0;
		for(int i = 0 ; i < 4 ; i++)
		{
			for(int j = 0 ; j < 4 ; j++)
			{
				if(Matrix[i][j] == 'X')
				{
					/////////////////////////////////////////////////////
					// x
					// row
					xcount = 0;
					Tcount = 0;
					for(int k = 0 ; k < 4 ; k++)
					{
						if(Matrix[i][k] == 'X')
							xcount ++;
						if(Matrix[i][k] == 'T')
							Tcount ++;			
					}
					if((xcount == 4 && Tcount == 0) || (xcount == 3 && Tcount == 1))
						return 1;			

					// coloum
					xcount = 0;
					Tcount = 0;
					for(int k = 0 ; k < 4 ; k++)
					{
						if(Matrix[k][j] == 'X')
							xcount ++;
						if(Matrix[k][j] == 'T')
							Tcount ++;
					}
					if((xcount == 4 && Tcount == 0) || (xcount == 3 && Tcount == 1))
						return 1;			

					// diagonal
					xcount = 1;
					Tcount = 0;
					for(int k =i+1,l =j+1;(k<4 && l<4);k++,l++)
					{
						if(Matrix[k][l] =='X')
							xcount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					for(int k =i-1,l = j-1;(k>=0 && l>=0);k--,l--)
					{
						if(Matrix[k][l] =='X')
							xcount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					if((xcount == 4 && Tcount == 0) || (xcount == 3 && Tcount == 1))
						return 1;			
					///////////////// other diagonal
					xcount = 1;
					Tcount = 0;
					for(int k =i-1,l =j+1;(k>4 && l<4);k--,l++)
					{
						if(Matrix[k][l] =='X')
							xcount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					for(int k =i+1,l = j-1;(k<4 && l>=0);k++,l--)
					{
						if(Matrix[k][l] =='X')
							xcount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					if((xcount == 4 && Tcount == 0) || (xcount == 3 && Tcount == 1))
						return 1;			

				}
				//// o 
				else if(Matrix[i][j] == 'O')
				{
					/////////////////////////////////////////////////////
					// o
					// row
					ocount = 0;
					Tcount = 0;
					for(int k = 0 ; k < 4 ; k++)
					{
						if(Matrix[i][k] == 'O')
							ocount ++;
						if(Matrix[i][k] == 'T')
							Tcount ++;			
					}
					if((ocount == 4 && Tcount == 0) || (ocount == 3 && Tcount == 1))
						return 0;			

					// coloum
					ocount = 0;
					Tcount = 0;
					for(int k = 0 ; k < 4 ; k++)
					{
						if(Matrix[k][j] == 'O')
							ocount ++;
						if(Matrix[k][j] == 'T')
							Tcount ++;
					}
					if((ocount == 4 && Tcount == 0) || (ocount == 3 && Tcount == 1))
						return 0;			

					// diagonal
					ocount = 1;
					Tcount = 0;
					for(int k =i+1,l =j+1;(k<4 && l<4);k++,l++)
					{
						if(Matrix[k][l] =='O')
							ocount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					for(int k =i-1,l = j-1;(k>=0 && l>=0);k--,l--)
					{
						if(Matrix[k][l] =='O')
							ocount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					if((ocount == 4 && Tcount == 0) || (ocount == 3 && Tcount == 1))
						return 0;			
					///////////////// other diagonal
					ocount = 1;
					Tcount = 0;
					for(int k =i-1,l =j+1;(k<4 && l<4);k--,l++)
					{
						if(Matrix[k][l] =='O')
							ocount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					for(int k =i+1,l = j-1;(k<4 &&l >=0);k++,l--)
					{
						if(Matrix[k][l] =='O')
							ocount++;

						if(Matrix[k][l] =='T')
							Tcount++;
					}
					if((ocount == 4 && Tcount == 0) || (ocount == 3 && Tcount == 1))
						return 0;			

				}
			}
		}
		//a draw or not completed
		for(int i = 0 ; i<4 ; i++)
		{
			for(int j = 0 ; j< 4 ; j++)
			{
				if(Matrix[i][j] == '.')
					return 2; // not completed

			}
		}
		return 3 ; // draw

	}

public:
	Board(string row[])
	{
		//intialize the input 
		for(int i=0 ; i<4 ; i++)
		{
			for(int j=0 ; j<4 ;j++)
			{
				Matrix[i][j]=row[i][j];
			}
		}


	}
	string isValid()
	{
		int i  = winner();
		string x ;
		if(i == 1 ) x="X won";
		else if ( i == 0) x = "O won";
		else if ( i == 2) x = "Game has not completed";
		else if ( i == 3) x = "Draw";
		return x;
	}
	void printMatrix()
	{
		// to print the matrix 
		for(int i=0 ;i< 4 ;i++)
		{
			for(int j=0 ;j< 4;j++)
			{
				cout<<Matrix[i][j]<<" ";
			}
			cout<<endl;
		}

	}
};


int main()
{
	string infile_name = "D:\\A-small-practice.in";
	fstream infile(infile_name,fstream::in);
	fstream outfile("D:\\output1.out",fstream::out);
	string temp , state ;
	getline(infile,temp);
	int num_test_cases = atoi(temp.c_str());
	string board[4];
	for(int i = 1 ; i <= num_test_cases ; i++)
	{
		for(int j = 0 ; j < 4 ; j++)
		{
			getline(infile,temp);
			board[j] = temp;
		}	
		Board TTT (board);
		state = TTT.isValid();
		outfile<<"Case #"<<i<<": "<<state<<endl;
		getline(infile,temp);//remove the empty line
	}
	return 0;
}
