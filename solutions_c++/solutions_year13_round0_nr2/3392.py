#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
  ifstream in_file;
  ofstream out_file;
  string read;
  int read_number;

  int nb_test;
  int patterns_lawn[100][100];
  int N = 0;
  int M = 0;
  bool possible;
  bool line_possible = true;
  bool colunns_possible = true;;

  if (argc != 3)
    {
      cout << "Wrong number of arguments" << endl;
      return 1;
    }

  in_file.open(argv[1]);
  out_file.open(argv[2]);

  if (in_file.is_open() == false || out_file.is_open() == false)
    {
      cout << "File cannot be open" << endl;
      return 1;
    }

  in_file >> read_number;
  nb_test = read_number;

  for (int i = 0; i < nb_test; i++)
    {
      in_file >> read_number;
      N = read_number;
      in_file >> read_number;
      M = read_number;

      for (int x = 0; x < N; x++)
	for (int y = 0; y < M; y++)
	  in_file >> patterns_lawn[x][y];

      for (int x = 0; x < N; x++)
	{
	  for (int y = 0; y < M; y++)
	    {
	      colunns_possible = true;
	      line_possible = true;

	      for (int z = 0; z < M; z++)
		if (patterns_lawn[x][z] > patterns_lawn[x][y])
		  {
		    colunns_possible = false;
		    break;
		  }
	      
	      for (int z = 0; z < N; z++)
		if (patterns_lawn[z][y] > patterns_lawn[x][y])
		  {
		    line_possible = false;
		    break;
		  }

	      if (colunns_possible == false && line_possible == false)
		  break;
	    }
	  if (colunns_possible == false && line_possible == false)
	    break;
	}
      
      out_file << "Case #" << i + 1 << ": ";
      if (colunns_possible == false && line_possible == false)
	{
	  out_file << "NO" << endl;
	}
      else
	out_file << "YES" << endl;
    }
  
  in_file.close();
  out_file.close();

  return 0;
}
