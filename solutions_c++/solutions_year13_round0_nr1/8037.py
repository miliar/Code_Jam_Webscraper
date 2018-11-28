#include "iostream"\

using namespace std;
char check(char board[4][4])
{
  char c;
  int I,J;
  int cnt;
  int flag =0;
  for(int i=0;i<4;i++)
  {
    J=0;
    c = board[i][J];
    cnt = 1;
    while(c == 'T')
    {
      c = board[i][++J];
      cnt++;
    }
    for(int j=J+1;j<4;j++)
    {
      if(c == '.' || board[i][j] == '.')
      {
	flag =1;
	break;
      }
      else if(board[i][j] == c || board[i][j] == 'T')
	cnt ++;
      else
	continue;
    }
    if(cnt >= 4)
    {
      return c;
    }
  }
  
  // columns 
  for(int j = 0;j < 4;j ++)
  {
    I = 0;
    c = board[I][j];
    cnt = 1;
    while(c == 'T')
    {
      c = board[++I][j];
      cnt++;

    }
    for(int i=I+1;i<4;i++)
    {
     if(c == '.' || board[i][j] == '.')
      {
	flag =1;
	break;
      }
     else if(board[i][j] == c || board[i][j] == 'T')
	cnt ++;
      else
	continue;
    }
    if(cnt == 4)
    {
      return c;
    }
  }
  // Diagonal left-right
  I=0;J=0;
  c = board[I][J];
  cnt = 1;
  while(c == 'T')
    {
      c = board[++I][++J];
      cnt++;
    }
  for(int i = I+1,j=J+1; i < 4;i++,j++)
  {
    if(board[i][j] == c || board[i][j] == 'T')
	cnt ++;
    else
      break;
  }
  if(cnt == 4)
  {
      return c;
  }
  // Diagonal right - left
  I=0;J=3;
  c = board[I][J];
  cnt = 1;
  while(c == 'T')
    {
      c = board[--I][--J];
      cnt++;
    }
  for(int i = I+1,j=J-1; i < 4;i++,j--)
  {
    if(board[i][j] == c || board[i][j] == 'T')
	cnt ++;
    else
      break;
  }
  if(cnt == 4)
  {
      return c;
  }
  if(flag ==1)
    return 'I';
  return 'D';
}
int main()
{
  char *result;
  char board[4][4];
  int C;
  cin >> C;
  result = new char[C];
  for(int x = 0;x <C;x++)
  {
    for(int i=0;i<4;i++)
    {
      for(int j=0;j<4;j++)
      {
	cin >> board[i][j];
      }
    }
    result[x] = check(board);
    cout << endl;
  }
  for(int x = 0;x <C;x++)
  {
    cout << "Case #"<<x+1<<": ";
    if(result[x] == 'D')
      cout<<"Draw";
    else if(result[x] == 'I' || result[x] == '.')
      cout<<"Game has not completed";
    else
      cout << result[x]<<" won";
    cout <<endl;
  }
  return 0;
}
