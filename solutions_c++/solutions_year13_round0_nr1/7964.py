#include <iostream>
#include <string>
#include <vector>
#include <iterator>
#include <fstream>
#include <stdlib.h>
#include <string.h>
using namespace std;
int caseno = 1;

inline int is_player_won(int board[4][4])
{
        int moves = 0;
	for(int i=0 ;i < 4; i++)
	{
		char player = board[i][0];
		bool won = true;
		if(player != '.') moves++;
		if(player == '.')
			won = false;
		for(int j = 1; j < 4; j++)
		{
			if(player == 'T' || player == '.')
			    player = board[i][j];
			if(!(board[i][j] == player || board[i][j] == 'T'))
			 won = false;
			if(board[i][j] != '.')
				moves++;
		}
		if(won && player != 'T' && player != '.') {
		 cout<<"Case #"<<caseno<<":"<<" "<<player<<" won"<<endl;	   
		 return 0;
		}
	}

	for(int i=0 ;i < 4; i++)
	{
		char player = board[0][i];
		bool won = true;
		if(player == '.')
			continue;
		for(int j = 1; j < 4; j++)
		{
			if(player == 'T')
			    player = board[j][i];
			if(!(board[j][i] == player || board[j][i] == 'T')) {
			 won = false;
			 break;
			}
		}
		if(won && player != 'T' && player != '.') {
		 cout<<"Case #"<<caseno<<":"<<" "<<player<<" won"<<endl;	   
		 return 0;
		}
	}
	char player = board[0][0];
	bool won = true;
	if(player != '.') {
	for(int i =1 ; i<4; ++i)
	{
		if(player == 'T' || player == '.')
                            player = board[i][i];
		if(!(board[i][i] == player || board[i][i] == 'T')) {
                         won = false;	
			 break;
		}
	} 	
	if(won && player != 'T' && player != '.') {
                 cout<<"Case #"<<caseno<<":"<<" "<<player<<" won"<<endl;
                 return 0;
        }
	}
	won = true;
	int c= 2;
	player = board[0][3];
	if(player != '.') {
	for(int i =1 ; i<4; ++i)
        {
                if(player == 'T' || player == '.')
                            player = board[i][c];
                if(!(board[i][c] == player || board[i][c] == 'T')) {
                         won = false;   
			 break;
		}
		c--;	
        }       
        if(won && player != 'T' && player != '.') {
                 cout<<"Case #"<<caseno<<":"<<" "<<player<<" won"<<endl;
                 return 0;
        }

	}

	if(moves == 16)	
	 cout<<"Case #"<<caseno<<":"<<" Draw"<<endl;
	else
	 cout<<"Case #"<<caseno<<":"<<" Game has not completed"<<endl;
}

 
void run_test(int board[4][4])
{
	is_player_won(board);	
	#if 0
	for(int i =0 ; i< 4; ++i) {
	for(int j =0; j < 4 ; j++)
	cout<<(char)board[i][j];
	cout<<endl;
	}
	cout<<endl;
	#endif
}

int main(int argc,char **argv)
{
  int total_test_cases = 0;
  const char *file = argv[1];
  ifstream in_stream;
  in_stream.open(file);
  string line;
  std::getline(in_stream, line);
  total_test_cases = atoi(line.c_str());
  int board[4][4] = {0};
  int r = 0;
  while(std::getline(in_stream, line))
  {
     
    if(line.size() < 4)
    {
	run_test(board);
	r = 0;
	memset(&board,0,sizeof board);
	caseno++;
	if(caseno > total_test_cases)
		break;
    }
    else
    {
	board[r][0] = line[0]; 
	board[r][1] = line[1]; 
	board[r][2] = line[2]; 
	board[r][3] = line[3];
	r++; 
    }
  }
  if(r == 4)
   {

	run_test(board);
  }
 

 return 0;
}
