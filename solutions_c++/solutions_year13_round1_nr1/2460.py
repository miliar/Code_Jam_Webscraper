//Google Code Jam 2013(Round 1A)
//Problem A
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
#include <limits>
#include <math.h>

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
  unsigned long long r = 0;
  unsigned long long t = 0;
  unsigned long long n = 0;
  int i,j;
  
  if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();
      
      for(i = 0; i < T; i++)
	{
	  getline(input,line);
	  ss << line;
	  ss >> r;
	  ss >> t;
	  ss.clear();
	  long long a = floor(sqrt(4*r*r - 4*r + 1 + 8*t));
	  long long b = 1 - 2*r + a;
	  n = floor(b/4);
	  output << "Case #" << i+1 << ": " << n << endl;
	}
      input.close();
      output.close();
    }

  else 
    cout << "Unable to open file" << endl;

  return 0;
}
