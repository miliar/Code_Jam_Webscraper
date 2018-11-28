//Google Code Jam 2013
//Problem B
//Nishanth Koganti

#include <stdio.h>
#include <memory.h>
#include <string.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
  string line,str;
  stringstream ss;
  ifstream input;
  ofstream output;
  input.open(argv[1]);
  output.open(argv[2]);

  int T;
  int N,M;
  int i,j,k;
  int v;
  bool result;

  if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(int t = 0; t < T; t++)
	{
	  result = true;
	  getline(input,line);
	  ss << line;
	  ss >> N;
	  ss >> M;
	  ss.clear();
	  
	  int grid[N][M];
	  int row[N];
	  int column[M];
	  for(i = 0; i < N; i++)
	    {
	      getline(input,line);
	      ss << line;
	      row[i] = 0;
	      for(j = 0; j < M; j++)
		{
		  ss >> grid[i][j];
		  if(grid[i][j] > row[i])
		    row[i] = grid[i][j];
		}
	      ss.clear();
	    }

	  for(j = 0; j < M; j++)
	    {
	      column[j] = 0;
	      for(i = 0; i < N; i++)
		if(grid[i][j] > column[j])
		  column[j] = grid[i][j];
	    }

	  for(i = 0; i < N; i++)
	    {
	      for(j = 0; j < M; j++)
		{
		  v = grid[i][j];
		  if((v >= row[i]) && (result == true))
		    result = true;
		  else if((v >= column[j]) && (result == true))
		    result = true;
		  else
		    result = false;
		}
	    }

	  if(result == true)
	    str = "YES";
	  else
	    str = "NO";

	  output << "Case #" << t+1 << ": " << str << endl;
	}
      input.close();
      output.close();
    }
  
  else
    cout << "Unable to open file" << endl;

  return 0;
}

	      
