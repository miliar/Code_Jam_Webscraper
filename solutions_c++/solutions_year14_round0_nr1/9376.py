#include <iostream>
#include <string>
#include <fstream>

using namespace std;


int	compare_rows(int row1[4], int row2[4])
{
  int count = 0;
  int res = 0;
  for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
	{
	  if (row1[i] == row2[j])
	    {
	      if (count > 0)
		return -1;
	      count += 1;
	      res = row1[i];
	    }
	}
    }
  return res;
}

void	read_file(string const &filename)
{
  ifstream file(filename);

  int nb_test;

  file >> nb_test;
  for (int i = 0; i < nb_test; ++i)
    {
      int	row[2];
      int	grid[2][4][4];

      for (int i = 0; i < 2; ++i)
	{
	  file >> row[i];
	  for (int j = 0; j < 4; ++j)
	    for (int k = 0; k < 4; ++k)
	      {
		file >> grid[i][j][k];
	      }
	}
      int ret = compare_rows(grid[0][row[0] - 1], grid[1][row[1] - 1]);
      cout << "Case #" << i+1 << ": ";
      if (ret == -1)
	cout << "Bad magician!" << endl;
      else if (ret == 0)
	cout << "Volunteer cheated!" << endl;
      else
	cout << ret << endl;
    }
}

int	main(int ac, char **av)
{
  if (ac != 2)
    {
      cout << "file needed" << endl;
      return 1;
    }
  read_file(av[1]);
  return 0;
}
