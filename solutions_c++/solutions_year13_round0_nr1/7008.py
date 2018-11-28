#include <iostream>
#include <fstream>

using namespace std;
int Win(char** board, char c);
int main(int argc, char** argv)
{
//    cout << "Hello World!!";    
      int T, i; // number of test cases
      // ifstream infile("TTTT.in");
      ifstream infile("A-large.in");
      infile >> T;
      char* board[4];
      for (i=0;i<4;i++)
      {
          board[i] = new char;    
      }
      for (i=0;i<T;i++)
      {
          string res = "Draw";
          int noDot = 1;
          for (int p = 0; p<4;p++)
          {
              for(int q=0;q<4;q++)
              {
                      infile >> board[p][q];        
                      if (board[p][q] == '.')
                      {
                          noDot = 0;
                      }
              }    
          }
          if (Win(board, 'X') !=0)
          {
             res = "X won";               
          }
          else if (Win(board, 'O') != 0)
          {
               res = "O won";
          }
          else if (noDot == 0 )
          {
               res = "Game has not completed";
          }     
          
          
          cout << "Case #" << i+1 << ": " << res << endl;    
      }
      for(i=0;i<4;i++)
      {
          delete board[i];
      }
}     

int Win(char** board, char c)
{
    int ret = 0;
    int i=0;
    for (i=0;i<4;i++)
    {
        int inter = 1;
        for (int j=0;j<4;j++)
        {
            inter = inter * ((board[i][j] == c || board[i][j] =='T' )? 1: 0);
        }
        ret = ret + inter;    
    }
    
    for (int j=0;j<4;j++)
    {
        int inter = 1;
        for (int i=0;i<4;i++)
        {
            inter = inter * ((board[i][j] == c || board[i][j] =='T' )? 1: 0);
        }
        ret = ret + inter;    
    }
    
    int inter = 1;
    for(i=0;i<4;i++)
    {
        inter = inter * ((board[i][i] == c || board[i][i] == 'T')? 1 : 0);                
    }
    ret = ret + inter;
    
    inter = 1;
    for(i=0;i<4;i++)
    {
        inter = inter * ((board[i][3-i] == c || board[i][3-i] == 'T' ) ? 1:0);
    }
    ret = ret + inter;
    return ret;    
}
