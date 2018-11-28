#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

string inFile = "large.in";
string outFile = "large.out";
enum ResultsEnum {X, O, DRAW, NOT_DONE, RESULT_SIZE};
string Results[RESULT_SIZE] = {"X won", "O won", "Draw", "Game has not completed"};
ResultsEnum Check(const vector<string>& board);

int main()
{
  int test = 0;
  vector<string> board(4);
  board[0].resize(4); board[1].resize(4);
  board[2].resize(4); board[3].resize(4);
  ifstream in;
  in.open(inFile);
  if(in) {
    string line;
    int totalTests;
    in>>totalTests;
    int count = 0;
    ofstream out(outFile);
    while(count < totalTests)
    {
      in>>board[0]>>board[1]>>board[2]>>board[3];
     /* getline(in, board[0]);
      getline(in, board[1]);
      getline(in, board[2]);
      getline(in, board[3]);
      getline(in, line);*/
      out << "Case #" << count+1 <<": ";
      out << Results[Check(board)] << endl;
      ++count;
    }
    out.close();
  }
  in.close();
  return 0;
}

ResultsEnum Check(const vector<string>& board)
{
  int xcount=0, ocount=0, tcount=0;
  int filled = 0;
  for(int i=0; i<4; ++i)
  {
    // check by row
    xcount=0; ocount=0; tcount=0;
    for(int j=0; j<4; ++j)
    {
      ++filled;
      if(board[i][j]=='X')
        ++xcount;
      else if(board[i][j]=='O')
        ++ocount;
      else if(board[i][j]=='T')
        ++tcount;
      else
        --filled;
    }
    if(xcount==4 || xcount+tcount==4)
      return X;
    else if(ocount==4 || ocount+tcount==4)
      return O;

    // check by col
    xcount=0; ocount=0; tcount=0;
    for(int j=0; j<4; ++j)
    {
      if(board[j][i]=='X')
        ++xcount;
      else if(board[j][i]=='O')
        ++ocount;
      else if(board[j][i]=='T')
        ++tcount;
    }
    if(xcount==4 || xcount+tcount==4)
      return X;
    else if(ocount==4 || ocount+tcount==4)
      return O;
  }

  //check diagonal
  xcount=0; ocount=0; tcount=0;
  for(int i=0; i<4; ++i)
  {
    if(board[i][i] == 'X')
      ++xcount;
    else if(board[i][i] == 'O')
      ++ocount;
    else if(board[i][i] == 'T')
      ++tcount;
  }
  if(xcount==4 || xcount+tcount==4)
      return X;
  else if(ocount==4 || ocount+tcount==4)
      return O;

  //check diagonal
  xcount=0; ocount=0; tcount=0;
  for(int i=0; i<4; ++i)
  {
    if(board[i][3-i] == 'X')
      ++xcount;
    else if(board[i][3-i] == 'O')
      ++ocount;
    else if(board[i][3-i] == 'T')
      ++tcount;
  }
  if(xcount==4 || xcount+tcount==4)
      return X;
  else if(ocount==4 || ocount+tcount==4)
      return O;

  if(filled == 16)
    return DRAW;
  else 
    return NOT_DONE;
}