#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define X_won "X won"
#define O_won "O won"
#define Draw  "Draw"
#define play  "Game has not completed"

#define CASE "Case #"

int any_body_won = 0;                     // 0 if no body is winning, 1 if somebody won , 2 if game has not completed

string row1, row2, row3, row4;
string table;

string result;

void solve_row(int index)
{ 
  if(any_body_won == 1) return;
  for(int i=0; i<4; i++)
  {
    if(table[4*index + i] == '.')
    {
      result = play;
      any_body_won = 2;
      return;
    }
  }
  
  int start_index, end_index;
  if(table[4*index] == 'T')
  {
    start_index = 4*index + 1;
    end_index = 3;
  }
  else
  {
    start_index = 4*index;
    end_index = 4;
  }
  
     for(int i=0; i<end_index; i++)
      {
	if(table[start_index] == table[start_index + i] || table[start_index + i] == 'T');                     
	else                                                                // row is full but no body won
        {
	 //result = play;
	 break;
	}
	if(i==(end_index-1))
	{
	  if(table[start_index] == 'X') (result = X_won);
	  else if(table[start_index] == 'O') (result = O_won);
	  any_body_won = 1;
        }
      }
}

void solve_col(int index)
{
  if(any_body_won == 1) return;
    for(int j=0; j<4; j++)
    {
      if(table[4*j + index] == '.')
      {
	result = play;
	any_body_won = 2;
	return;
      }
    }
  
  int start_index;
  if(table[index] == 'T') start_index = 1;
  else start_index = 0;
  
     for(int i=start_index; i<4; i++)
      {
	if(table[4*start_index + index] == table[4*i + index] || table[4*i + index] == 'T');                     
	else                                                                // row is full but no body won
        {
	 //result = play;
	 break;
	}
	if(i==3)
	{
	  if(table[4*start_index + index] == 'X') (result = X_won);
	  else if(table[4*start_index + index] == 'O') (result = O_won);
	  any_body_won = 1;
        }
      }
}

void solve_main_diag()
{
  if(any_body_won == 1) return;
    for(int j=0; j<4; j++)
    {
      if(table[5*j] == '.')
      {
	result = play;
	any_body_won = 2;
	return;
      }
    }
  
  int start_index;
  if(table[0] == 'T') start_index = 5;
  else start_index = 0;
  
     for(int i=0; i<4; i++)
      {
	if(table[start_index] == table[5*i] || table[5*i] == 'T');                     
	else                                                                // row is full but no body won
        {
	 //result = play;
	 break;
	}
	if(i==3)
	{
	  if(table[start_index] == 'X') (result = X_won);
	  else if(table[start_index] == 'O') (result = O_won);
	  any_body_won = 1;
        }
      }
}

void solve_off_diag()
{
  if(any_body_won == 1) return;
    for(int j=0; j<4; j++)
    {
      if(table[3*j + 3] == '.')
      {
	result = play;
	any_body_won = 2;
	return;
      }
    }
  
  int start_index;
  if(table[3] == 'T') start_index = 6;
  else start_index = 3;
  
     for(int i=0; i<4; i++)
      {
	if(table[start_index] == table[3*i + 3] || table[3*i + 3] == 'T');                     
	else                                                                // row is full but no body won
        {
	 //result = play;
	 break;
	}
	if(i==3)
	{
	  if(table[start_index] == 'X') (result = X_won);
	  else if(table[start_index] == 'O') (result = O_won);
	  any_body_won = 1;
        }
      }
}



int main(int argc, char* argv[])
{
  int T;
  string empty_line;
  
  ifstream in_file(argv[1]);          //A-small-attempt0.in
  ofstream out_file("Output");
  
  if(!in_file.is_open())
  {
    cout<<"Cannot open outfile"<<endl;
  }
  
  
  in_file>>T;
  
  for(int i=0; i<T; i++)
  { 
      any_body_won = 0;
      
      in_file>>row1;
      in_file>>row2;
      in_file>>row3;
      in_file>>row4;
      //in_file>>empty_line;
      table = row1 + row2 + row3 + row4;
            
      solve_row(0);
      solve_row(1);
      solve_row(2);
      solve_row(3);
            
      solve_col(0);
      solve_col(1);
      solve_col(2);
      solve_col(3);
      
      solve_main_diag();
      solve_off_diag();
      
      if(any_body_won == 0) result = Draw;
      
      out_file<<CASE<<(i+1)<<": "<<result<<endl;
      
      
  }
  return 0;
}