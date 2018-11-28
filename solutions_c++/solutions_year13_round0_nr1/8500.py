#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Board
{// chess Board class
private:
	char Matrix[4][4]; //$*4 matrix to represent the chess board
	string Result; //string to check if scenario or not
	int X_win;
	int O_win;
	int dot;
	//private method to check if the scenario 
	//return Result :string to tell who won the game scenario 
	
	string check_scenario()
	{
		X_win = 0;
		O_win = 0;
		int dot = 0;
		for(int i = 0;i<4;i++)
		{
			for(int j = 0;j<4;j++)
			{
				if(Matrix[i][j] =='.')dot++;

				//============cheking for X==================================================================
				if(Matrix[i][j] =='x' ||Matrix[i][j] =='X' ||Matrix[i][j] =='T' ||Matrix[i][j] =='t')
				{
					//check the row-----------------------------
					for(int k =j+1;k<4;k++)
					{
						if(Matrix[i][k] =='x' || Matrix[i][k]=='X' ||Matrix[i][k]=='T' ||Matrix[i][k] == 't')
						{
							X_win++;
						}
						else break;
					
					}
					for(int k =j-1;k>=0;k--)
					{
						if(Matrix[i][k] =='x' || Matrix[i][k]=='X' ||Matrix[i][k]=='T' ||Matrix[i][k] == 't')
						{
							X_win++;
						}
						else break;
					}
					if(X_win == 3) break;
					else X_win =0;
					
					//----------------------------------------

					//check the column-----------------------------
					for(int k =i+1;k<4;k++)
					{
						if(Matrix[k][j] =='x' || Matrix[k][j] =='X' || Matrix[k][j] =='T' || Matrix[k][j] =='t')
						{
							X_win ++;
						}
						else break;
					}
					for(int k =i-1;k>=0;k--)
					{
						if(Matrix[k][j] =='x' || Matrix[k][j] =='X' || Matrix[k][j] =='T' || Matrix[k][j] =='t')
						{
							X_win ++;
						}
						else break;
					}
					if(X_win == 3) break;
					else X_win =0;
					//----------------------------------------
					
					//check the 1st diagonal-----------------------
					for(int k =i+1,l =j+1;(k<4&&l<4);k++,l++)
					{
						if(Matrix[k][l] =='X' || Matrix[k][l] =='x' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							X_win ++;
						}
						else break;
					}
					for(int k =i-1,l = j-1;(k>=0&&l>=0);k--,l--)
					{
						if(Matrix[k][l] =='X' || Matrix[k][l] =='x' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							X_win ++;
						}
						else break;
					}
					if(X_win == 3) break;
					else X_win =0;
					//----------------------------------------
					//check the 2nd diagonal-----------------------
					for(int k =i-1,l =j+1;(k>=0&&l<4);k--,l++)
					{
						if(Matrix[k][l] =='X' || Matrix[k][l] =='x' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							X_win ++;
						}
						else break;
					}
					for(int k =i+1,l = j-1;(k<4&&l>=0);k++,l--)
					{
						if(Matrix[k][l] =='X' || Matrix[k][l] =='x' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							X_win ++;
						}
						else break;
					}
					if(X_win == 3) break;
					else X_win =0;
					//----------------------------------------
										
				}//end of if(X)
				//=======================================================================================
				
				
				//==================checking for O=======================================================
				if(Matrix[i][j] =='o' ||Matrix[i][j] =='O' ||Matrix[i][j] =='T' ||Matrix[i][j] =='t')
				{
					//check the row-----------------------------
					for(int k =j+1;k<4;k++)
					{
						if(Matrix[i][k] =='o' || Matrix[i][k]=='O' ||Matrix[i][k]=='T' ||Matrix[i][k] == 't')
						{
							O_win++;
						}
						else break;
					
					}
					for(int k =j-1;k>=0;k--)
					{
						if(Matrix[i][k] =='o' || Matrix[i][k]=='O' ||Matrix[i][k]=='T' ||Matrix[i][k] == 't')
						{
							O_win++;
						}
						else break;
					}
					if(O_win == 3) break;
					else O_win =0;
					//----------------------------------------

					//check the column-----------------------------
					for(int k =i+1;k<4;k++)
					{
						if(Matrix[k][j] =='o' || Matrix[k][j] =='O' || Matrix[k][j] =='T' || Matrix[k][j] =='t')
						{
							O_win ++;
						}
						else break;
					}
					for(int k =i-1;k>=0;k--)
					{
						if(Matrix[k][j] =='o' || Matrix[k][j] =='O' || Matrix[k][j] =='T' || Matrix[k][j] =='t')
						{
							O_win ++;
						}
						else break;
					}
					if(O_win == 3) break;
					else O_win =0;
					//----------------------------------------
					
					//check the 1st diagonal-----------------------
					for(int k =i+1,l =j+1;(k<4&&l<4);k++,l++)
					{
						if(Matrix[k][l] =='O' || Matrix[k][l] =='o' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							O_win ++;
						}
						else break;
					}
					for(int k =i-1,l = j-1;(k>=0&&l>=0);k--,l--)
					{
						if(Matrix[k][l] =='O' || Matrix[k][l] =='o' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							O_win ++;
						}
						else break;
					}
					if(O_win == 3) break;
					else O_win =0;
					//----------------------------------------
					//check the 2nd diagonal-----------------------
					for(int k =i-1,l =j+1;(k>=0&&l<4);k--,l++)
					{
						if(Matrix[k][l] =='O' || Matrix[k][l] =='o' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							O_win ++;
						}
						else break;
					}
					for(int k =i+1,l = j-1;(k<4&&l>=0);k++,l--)
					{
						if(Matrix[k][l] =='O' || Matrix[k][l] =='o' || Matrix[k][l] =='T' || Matrix[k][l] =='t')
						{
							O_win ++;
						}
						else break;
					}
					if(O_win == 3) break;
					else O_win =0;
					//----------------------------------------
										
				}//end of if(O)
			}
			
		
		}//end of for(i)
	
	if(X_win==3 ) Result ="X won";
	else if(O_win==3) Result ="O won";
	else if(dot > 0) Result = "Game has not completed";
	else Result = "Draw";
	return Result;
	
	}
	
public:
	Board(string row[])
	{
	//intialize the input 
		for(int i=0 ;i<4 ;i++)
		{
			for(int j=0 ;j<4;j++)
			{
				Matrix[i][j]=row[i][j];
			}
		}
		
	}
	string checkResult()
	{
		// return a string of is valid or not
		return (this->check_scenario());
	}
	void printMatrix()
	{
		// to print the matrix 
		for(int i=0 ;i<4 ;i++)
		{
			for(int j=0 ;j<4;j++)
			{
				cout<<Matrix[i][j]<<" ";
			}
			cout<<endl;
		}
	
	}
	void ClearMatrix()
	{
		for(int i=0 ;i<4 ;i++)
		{
			for(int j=0 ;j<4;j++)
			{
				Matrix[i][j]='.';
			}
		}
	}
};

int main()
{
	
	string in_file_name ;  //input file destination
	string out_file_name ; //output file destination
	/*
	in_file_name = "D:\\data1.txt";
	out_file_name = "D:\\data2.txt";*/
	/*
	*this can be uncommented to and input the destinations directly
	*/
	/*cout<<"please enter the input file destination "<<endl;
	getline(cin,in_file_name);
	cout<<"please enter the input file destination "<<endl;
	getline(cin,out_file_name);*/
	//user input using the console
	string temp;
	fstream in_file( "D:\\A-small-attempt0.in",fstream::in);  //input file 
	fstream out_file("D:\\Tic_output.txt",fstream::out);  //output file

	getline(in_file,temp);  // get the first line 
	int no_config = atoi(temp.c_str()); // convert it to integer
	// convert the string to int
	string row[4];
	string the_output;
	for(int i=0 ;i<no_config;i++)
	{
		for(int j=0 ; j<4 ;j++)
		{
			getline(in_file,temp);
			if(temp == "" )getline(in_file,temp);
			row[j] = temp;
		}
			Board x(row);
			x.printMatrix();
			out_file<<"Case #"<<(i+1)<<": "<<x.checkResult()<<endl;
			//print to the file
			cout<<endl;
	}
	in_file.close(); //close the files
	out_file.close();
	return 0;
}