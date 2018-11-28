
#include <iostream>
#include<fstream>
//#include<ostream>
using namespace std;

//#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif

	int run = 0;
	cin>>run;
	bool itrFlg = false;
	int iter = 0;
	while(run--)
	{
		if(itrFlg)
			cout<<endl;
		itrFlg = true;

		char row[4][4];
		int Tloc[1][2];
		char diag[4];
		char diag1[4];
		int i,j;
		char c;
		char win = '0';
		bool emptyflg = false;
		bool Tflg = false;
		fflush(stdin);

		for(i=0;i<4;i++) // Taking input
		{
			for(j=0;j<4;j++)
			{
				cin>>c;
				row[i][j] = c;
				if(c == 'T')// storing T position & enabling Tflg
				{
					Tloc[0][0] = i;
					Tloc[0][1] = j;
					Tflg = true;
				}
				else if(c == '.') // enabling emptyflg
					emptyflg = true;
				
				if(i==j)
					diag[i] = c;

				if( (i==0) && (j==3) )
					diag1[0] = c;
				else if( (i==1) && (j==2) )
					diag1[1] = c;
				else if( (i==2) && (j==1) )
					diag1[2] = c;
				else if( (i==3) && (j==0) )
					diag1[3] = c;
			}
		}

		for(i=0;i<4;i++) // Checking rows for win
		{
			if(row[i][0] == 'X')
			{
				if( (row[i][1] == 'X') && (row[i][2] == 'X') && (row[i][3] == 'X') )
				{
					win = 'X';
					break;
				}
			}
			else if(row[i][0] == 'O')
			{
				if( (row[i][1] == 'O') && (row[i][2] == 'O') && (row[i][3] == 'O') )
				{
					win = 'O';
					break;
				}
			}

		}
		
		if(win == '0') 
		{
			for(i=0;i<4;i++) // checking Coloumns for win
			{
				if(row[0][i] == 'X')
				{
					if( (row[1][i] == 'X') && (row[2][i] == 'X') && (row[3][i] == 'X') )
					{
						win = 'X';
						break;
					}
				}
				else if(row[0][i] == 'O')
				{
					if( (row[1][i] == 'O') && (row[2][i] == 'O') && (row[3][i] == 'O') )
					{
						win = 'O';
						break;
					}
				}

			}
		}

		if(win == '0') // checking Diag for win
		{
			if(diag[0] == 'X')
			{
				if( (diag[1] == 'X') && (diag[2] == 'X') && (diag[3] == 'X') )
				{
					win = 'X';
				}
			}
			else if(diag[0] == 'O')
			{
				if( (diag[1] == 'O') && (diag[2] == 'O') && (diag[3] == 'O') )
				{
					win = 'O';
				}
			}
		}

		if(win == '0') // checking Diag for win
		{
			if(diag1[0] == 'X')
			{
				if( (diag1[1] == 'X') && (diag1[2] == 'X') && (diag1[3] == 'X') )
				{
					win = 'X';
				}
			}
			else if(diag1[0] == 'O')
			{
				if( (diag1[1] == 'O') && (diag1[2] == 'O') && (diag1[3] == 'O') )
				{
					win = 'O';
				}
			}
		}

		if(win == '0' && Tflg) // if T is there 
		{
			switch(Tloc[0][1])
			{
				case 0:
					if(row[Tloc[0][0]][1] == 'X')
					{
						if( (row[Tloc[0][0]][2] == 'X') && (row[Tloc[0][0]][3] == 'X') ) // T is at [0]
						{
							win = 'X';
						}
					}
					else if(row[Tloc[0][0]][1] == 'O')
					{
						if( (row[Tloc[0][0]][2] == 'O') && (row[Tloc[0][0]][3] == 'O') ) // T is at [0]
						{
							win = 'O';
						}
					}
					break;

				case 1:
					if(row[Tloc[0][0]][0] == 'X')
					{
						if( (row[Tloc[0][0]][2] == 'X') && (row[Tloc[0][0]][3] == 'X') ) // T is at [1]
						{
							win = 'X';
						}
					}
					else if(row[Tloc[0][0]][0] == 'O')
					{
						if( (row[Tloc[0][0]][2] == 'O') && (row[Tloc[0][0]][3] == 'O') ) // T is at [1]
						{
							win = 'O';
						}
					}
					break;

				case 2:
					if(row[Tloc[0][0]][0] == 'X')
					{
						if( (row[Tloc[0][0]][1] == 'X') && (row[Tloc[0][0]][3] == 'X') ) // T is at [2]
						{
							win = 'X';
						}
					}
					else if(row[Tloc[0][0]][0] == 'O')
					{
						if( (row[Tloc[0][0]][1] == 'O') && (row[Tloc[0][0]][3] == 'O') ) // T is at [2]
						{
							win = 'O';
						}
					}
					break;

				case 3:
					if(row[Tloc[0][0]][0] == 'X')
					{
						if( (row[Tloc[0][0]][1] == 'X') && (row[Tloc[0][0]][2] == 'X') ) // T is at [3]
						{
							win = 'X';
						}
					}
					else if(row[Tloc[0][0]][0] == 'O')
					{
						if( (row[Tloc[0][0]][1] == 'O') && (row[Tloc[0][0]][2] == 'O') ) // T is at [3]
						{
							win = 'O';
						}
					}
					break;
			}
		}

		if(win == '0' && Tflg) // if T is there in Dia
		{
			if(Tloc[0][0] == Tloc[0][1])
			{
				switch(Tloc[0][0])
				{
				case 0:
					if(diag[1] == 'X')
					{
						if( (diag[2] == 'X') && (diag[3] == 'X') )
						{
							win = 'X';
						}
					}
					else if(diag[1] == 'O')
					{
						if( (diag[2] == 'O') && (diag[3] == 'O') )
						{
							win = 'O';
						}
					}
					break;
				
				case 1:
					if(diag[0] == 'X')
					{
						if( (diag[2] == 'X') && (diag[3] == 'X') )
						{
							win = 'X';
						}
					}
					else if(diag[0] == 'O')
					{
						if( (diag[2] == 'O') && (diag[3] == 'O') )
						{
							win = 'O';
						}
					}
					break;
				
				case 2:
					if(diag[0] == 'X')
					{
						if( (diag[1] == 'X') && (diag[3] == 'X') )
						{
							win = 'X';
						}
					}
					else if(diag[0] == 'O')
					{
						if( (diag[1] == 'O') && (diag[3] == 'O') )
						{
							win = 'O';
						}
					}
					break;
				
				case 3:
					if(diag[1] == 'X')
					{
						if( (diag[2] == 'X') && (diag[0] == 'X') )
						{
							win = 'X';
						}
					}
					else if(diag[1] == 'O')
					{
						if( (diag[2] == 'O') && (diag[0] == 'O') )
						{
							win = 'O';
						}
					}
					break;
				}
			}
		}

		if(win == '0' && Tflg)
		{
			if( (Tloc[0][0] == 0) && (Tloc[0][1] == 3) && (diag1[0] == 'T') ) //Diag1[0]
			{
				if(diag1[1] == 'X')
				{
					if( (diag1[2] == 'X') && (diag1[3] == 'X') )
					{
						win = 'X';
					}
				}
				else if(diag1[1] == 'O')
				{
					if( (diag1[2] == 'O') && (diag1[3] == 'O') )
					{
						win = 'O';
					}
				}
			}
			else if( (Tloc[0][0] == 1) && (Tloc[0][1] == 2) && (diag1[1] == 'T') )
			{
				if(diag1[0] == 'X')
				{
					if( (diag1[2] == 'X') && (diag1[3] == 'X') )
					{
						win = 'X';
					}
				}
				else if(diag1[0] == 'O')
				{
					if( (diag1[2] == 'O') && (diag1[3] == 'O') )
					{
						win = 'O';
					}
				}
			}
			else if( (Tloc[0][0] == 2) && (Tloc[0][1] == 1) && (diag1[2] == 'T') )
			{
				if(diag1[1] == 'X')
				{
					if( (diag1[0] == 'X') && (diag1[3] == 'X') )
					{
						win = 'X';
					}
				}
				else if(diag1[1] == 'O')
				{
					if( (diag1[0] == 'O') && (diag1[3] == 'O') )
					{
						win = 'O';
					}
				}
			}
			else if( (Tloc[0][0] == 3) && (Tloc[0][1] == 0) && (diag1[3] == 'T') )
			{
				if(diag1[1] == 'X')
				{
					if( (diag1[2] == 'X') && (diag1[0] == 'X') )
					{
						win = 'X';
					}
				}
				else if(diag1[1] == 'O')
				{
					if( (diag1[2] == 'O') && (diag1[0] == 'O') )
					{
						win = 'O';
					}
				}
			}
		}

		//Result Display
		cout<<"Case #"<<++iter<<": ";
		if(win == '0' && emptyflg)
			cout<<"Game has not completed";
		else if( win == '0' && !emptyflg)
			cout<<"Draw";
		else if( win == 'X')
			cout<<"X won";
		else if( win == 'O')
			cout<<"O won";

		
		//logs
	}

	return 0;
}
//logs
		/*for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cout<<row[i][j];
			}
			cout<<endl;
		}
		cout<<endl;*/