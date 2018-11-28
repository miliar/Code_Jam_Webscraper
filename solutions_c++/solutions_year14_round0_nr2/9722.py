//Google Code Jam: Qualification Round 2014
//Nishanth Koganti

#include <stdio.h>
#include <memory.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>
 
using namespace std;

string line;
stringstream ss;
ifstream input;
ofstream output;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;	  

int main(int arc, char** argv)
{
  input.open(argv[1]);
  output.open(argv[2]);

  int T, t, farms;
  double C, F, x;
  double minT, time;

   if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(t = 1; t <= T; t++)
	{
	  getline(input,line);
	  ss << line;
	  ss >> C;
	  ss >> F;
	  ss >> x;
	  ss.clear();

	  minT = x/2.0;
	  farms = 0;

	  while(true)
	    { 
	      time = 0.0;
	      farms++;
	      for(int i = 0; i < farms; i++)
		{
		  time += C/(2+i*F);
		}
	      time += x/(2+farms*F);
	      if(time < minT)
		minT = time;
	      else
		break;
	    }

	  cout << t << endl;
	  output << "Case #" << t <<  ": " << setprecision(15) << minT << endl; 
	}
      input.close();
      output.close();
    }
  
  else
    cout << "Unable to open file" << endl;
  
  return 0;
}
