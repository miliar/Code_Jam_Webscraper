// Code Jam 2015: Qualification Round
// Author: Nishanth 
// Date: 2015/4/10

#include <map>
#include <limits>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
  ifstream input;
  ofstream output;
  string line,str;
  stringstream ss;
  
  input.open(argv[1]);
  output.open(argv[2]);

  int T,Smax;
  int stand,ans;
  string sequence;
  
  if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();
      
      for(int t = 0; t < T; t++)
	{
	  getline(input,line);
	  ss << line;
	  ss >> Smax;
	  ss >> sequence;
	  ss.clear();
	  
	  ans = 0; stand = 0;

	  for(int n = 0; n <= Smax; n++)
	    {
	      if(stand<n)
		{
		  ans = ans+n-stand;
		  stand = stand+n-stand;
		}
	      stand = stand-48+(int) sequence[n];
	    }
	  
	  output << "Case #" << t+1 << ": " << ans << endl;
	}
      input.close();
      output.close();
    }

  else 
    cout << "Unable to open file" << endl;

  return 0;
}
