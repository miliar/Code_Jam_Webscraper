#include <iostream>
#include <fstream>

using namespace std;

int main()
{
  ifstream myfile ("A-large.in");
  ofstream answer ("1A.out");
  int cases, countX, countO, countT;
  bool empty;
  char array[4][4];
  char winner, current;
  
  myfile >> cases;
  
  for(int c=0; c < cases; ++c)
  {
    empty = false;
	winner = 'D';
    for(int i=0; i < 4; ++i)
	{
	  countX = 0;
	  countO = 0;
	  countT = 0;
	  for(int k=0; k < 4; ++k)
	  {
	    myfile >> current;
		array[i][k] = current;
		if(current == 'X')
		  countX++;
		else if(current == 'O')
		  countO++;
		else if(current == 'T')
		  countT++;
		else if(current == '.')
		  empty = true;
	  }
	  if((countO == 3 && countT == 1) || countO == 4)
	    winner = 'O';
	  else if((countX == 3 && countT == 1) || countX == 4)
	    winner = 'X';
    }
	/**for(int i=0; i < 4; ++i)
	{
	  for(int k=0; k < 4; ++k)
	    answer << array[i][k];
      answer << endl;
	} **/
    for(int i=0; i < 4; ++i)
	{
	  countX = 0;
	  countO = 0;
	  countT = 0;
	  for(int k=0; k < 4; ++k)
	  {
		current = array[k][i];
		if(current == 'X')
		  countX++;
		else if(current == 'O')
		  countO++;
		else if(current == 'T')
		  countT++;
		else if(current == '.')
		  empty = true;
	  }
	  if((countO == 3 && countT == 1) || countO == 4)
	    winner = 'O';
	  else if((countX == 3 && countT == 1) || countX == 4)
	    winner = 'X';
    }
	
	countX = 0;
	countO = 0;
	countT = 0;
	for(int i=0; i < 4; ++i)
	{
	  current = array[i][i];
	  if(current == 'X')
		  countX++;
		else if(current == 'O')
		  countO++;
		else if(current == 'T')
		  countT++;
		else if(current == '.')
		  empty = true;
	}
	if((countO == 3 && countT == 1) || countO == 4)
	  winner = 'O';
    else if((countX == 3 && countT == 1) || countX == 4)
      winner = 'X';
	
	countX = 0;
	countO = 0;
	countT = 0;
	for(int i=0; i < 4; ++i)
	{
	  current = array[i][3-i];
	  if(current == 'X')
		  countX++;
		else if(current == 'O')
		  countO++;
		else if(current == 'T')
		  countT++;
		else if(current == '.')
		  empty = true;
	}
	if((countO == 3 && countT == 1) || countO == 4)
	  winner = 'O';
    else if((countX == 3 && countT == 1) || countX == 4)
      winner = 'X';
	  
	answer << "Case #" << c+1 << ": ";
	if(winner == 'X' || winner == 'O')
	  answer << winner << " won" << endl;
	else if(empty == true)
	  answer << "Game has not completed" << endl;
	else
	  answer << "Draw" << endl;
  }
  
  return 0;
}