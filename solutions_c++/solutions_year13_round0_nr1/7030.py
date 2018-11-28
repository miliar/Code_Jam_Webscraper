#include <iostream>
#include<fstream>




using namespace std;

char board[4][4];

int main()

{

	ifstream fin("input.in");
	ofstream fout("output.in");

	int T;
	fin >> T; 

	int t= 1;
	while(T--)
	{

		bool isdot = false;

		for(int i =0 ; i<4 ; i++)
		{

			for(int j =0 ; j< 4 ; j++)
			{

				fin >> board[i][j] ; 
				if(board[i][j] =='.')
					isdot = true;
			}
		}


		char win = 'C';

		if(win =='C')
		{
			for(int i=0; i< 4; i++)
			{
				char now = board[i][0];
				if(now== '.')
					continue;
				if(now=='T')
					now = board[i][1];
				if(now== '.')
					continue;
				int j;
				for(j =1; j<4; j++)
				{
					if((board[i][j] != now )&& (board[i][j] != 'T'))
						break;
				}
				if(j==4)
					win = now;
			}
		}

		if(win =='C')
		{
			for(int i=0; i< 4; i++)
			{
				char now = board[0][i];
				if(now== '.')
					continue;
				if(now=='T')
					now = board[1][i];
				if(now== '.')
					continue;
				int j;
				for(j =1; j<4; j++)
				{
					if((board[j][i] != now )&& (board[j][i] != 'T'))
						break;
				}
				if(j==4)
					win = now;
			}
		}

		if(win =='C')
		{

			char now = board[0][0];
			if(now != '.'){
				if(now=='T')
					now = board[1][1];
				if(now != '.'){
					int i, j;
					for( i=1; i< 4; i++)
					{

						if((board[i][i] != now )&& (board[i][i] != 'T'))
							break;


					}
					if(i==4)
						win = now;
				}
			}
		}

		if(win =='C')
		{
			char now = board[0][3];
			if(now != '.'){
				if(now=='T')
					now = board[1][2];
				if(now != '.'){
					int i, j;
					for( i=1, j=2; i< 4; i++,j--)
					{

						if((board[i][j] != now )&& (board[i][j] != 'T'))
							break;

					}

					if(i==4)
						win = now;
				}
			}
		}	



		if(win == 'O')
			fout << "Case #" << t << ": " << "O won" <<endl;
		else if(win == 'X')
			fout << "Case #" << t << ": " << "X won" <<endl;
		else if(win =='C')
		{
			if(isdot)
				fout<<  "Case #" << t << ": Game has not completed" << endl;
			else
				fout<< "Case #" << t << ": Draw" << endl;
		}



		t++;
	}

	fin.close();
	fout.close();

}

