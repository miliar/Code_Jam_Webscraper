#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string CheckDraw(char board[4][4], int dot)
{
		int rx,cx,d1x,d2x,
			ro,co,d1o,d2o,
			rt,ct,d1t,d2t;
		rx=cx=d1x=d2x=ro=co=d1o=d2o=rt=ct=d1t=d2t=0;
		for(int i=0; i<4; i++)
		{
			//d1
			switch(board[i][i])
				{
				case 'X': d1x++;
					break;
				case 'O': d1o++;
					break;
				case 'T' : d1t++;
			}

			//d2
			switch(board[i][3-i])
				{
				case 'X': d2x++;
					break;
				case 'O': d2o++;
					break;
				case 'T' : d2t++;
				}

			rx=ro=rt=cx=co=ct=0;
			for(int j=0; j<4; j++)
			{
				//row
				switch(board[i][j])
				{
				case 'X': rx++;
					break;
				case 'O': ro++;
					break;
				case 'T' : rt++;
				}
				//col
				switch(board[j][i])
				{
				case 'X': cx++;
					break;
				case 'O': co++;
					break;
				case 'T' : ct++;
				}
			}
			
			if((rx==4-rt)||(cx==4-ct))
				return "X won";
			else if((ro==4-rt)||(co==4-ct))
				return "O won";

		}

			if((d1x==4-d1t)||(d2x==4-d2t)||(d2x==4-d2t)||(d2x==4-d2t))
				return "X won";
			else if((d1o==4-d1t)||(d2o==4-d2t)||(d2o==4-d2t)||(d2o==4-d2t))
				return "O won";
			else if(dot==0)
				return "Draw";
			else
				return "Game has not completed";
}

void main(int argc, char* argv[])
{
	int N;
	string str;
	string::iterator si;
	ifstream ifile;

	if(argc<=1)
		ifile.open("../A-small-attempt0.in");
	else
		ifile.open(argv[1]);
	if(!ifile.is_open())
	{
		cout << "File not Found! in " << endl; 
		exit(-1);
	}
	
	ifile >> N;
	char board[4][4];
	string result;
	for(int n=1; n<=N; n++)
	{
		int dot=0;
		result=' ';
		for(int i=0;i<4;i++)
		{
			for(int j=0; j<4; j++)
			{
				char c;
				ifile >> c;
				board[i][j] = c;
				if(c=='.')
					dot++;
			}
		}
		
		cout << "Case #" << n << ": " << CheckDraw(board,dot) << endl;
	}

	ifile.close();
}