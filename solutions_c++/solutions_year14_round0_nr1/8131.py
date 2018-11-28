#include <iostream>
#include <string>

using namespace std;

void read_config(int* buff);

int main(int argc, char* argv[])
{
  int T;
  cin >> T;
  
  int first = 0;
  int second = 0;

  int row1[4];
  int row2[4];
  int tmp;
  int cnt;
  for (int ii = 1; ii <= T; ++ii)
  {
    read_config(row1);
    read_config(row2);

    cnt = 0;
    int num = 0;
    for (int jj = 0; jj < 4; ++jj)
    {
      for (int kk = 0; kk < 4; ++kk)
      {
	if (row1[jj] == row2[kk])
	{
	  ++cnt;
	  num = row1[jj];
	  break;
	}
      }
    }

    if (cnt == 1)
    {
      cout << "Case #" << ii << ": " << num << endl;
    }
    else if (cnt == 0)
    {
      cout << "Case #"<< ii << ": Volunteer cheated!" << endl;
    }
    else
    {
      cout << "Case #" << ii << ": Bad magician!" << endl;
    } 
  }
}

void read_config(int* buff)
{
  int first;
  int tmp;
  cin >> first;
  for (int rr = 0; rr < 4; ++rr)
  {
    if (rr == first-1)
    {
      for (int jj = 0; jj < 4; ++jj)
      {
	cin >> tmp;
	buff[jj] = tmp;
      } 
    } 
    else
    {
      for (int jj = 0; jj < 4; ++jj)
      {
	cin >> tmp;
      } 
    } 
  }
}
