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

  int T, t, i, j, temp, num, res;
  int ans1, ans2;
  vector<int> line1, line2;
  vector<int>::iterator it1, it2;


   if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(t = 1; t <= T; t++)
	{
	  num = 0;
	  line1.clear();
	  line2.clear();

	  getline(input,line);
	  ss << line;
	  ss >> ans1;
	  ss.clear();

	  for(i = 1; i <= 4; i++)
	    { 
	      getline(input,line);
	      if(i == ans1)
		{
		  ss << line;
		  for(j = 0; j < 4; j++)
		    {
		      ss >> temp;
		      line1.push_back(temp);
		    }
		  ss.clear();
		}
	    }

	  getline(input,line);
	  ss << line;
	  ss >> ans2;
	  ss.clear();

	  for(i = 1; i <= 4; i++)
	    { 
	      getline(input,line);
	      if(i == ans2)
		{
		  ss << line;
		  for(j = 0; j < 4; j++)
		    {
		      ss >> temp;
		      line2.push_back(temp);
		    }
		  ss.clear();
		}
	    }

	  sort(line1.begin(),line1.end());
	  sort(line2.begin(),line2.end());

	  it1 = line1.begin();
	  it2 = line2.begin();

	  while(it1 != line1.end() && it2 != line2.end())
	    {
	      if(*it1 < *it2)
		++it1;
	      else if(*it1 == *it2)
		{
		  num++;
		  res = *it1;
		  ++it1; ++it2;
		}
	      else
		++it2;
	    }

	  if(num == 0)
	    output << "Case #" << t << ": Volunteer cheated!" << endl;
	  else if(num == 1)
	    output << "Case #" << t << ": " << res << endl;
	  else
	    output << "Case #" << t << ": Bad magician!" << endl; 
	}
      input.close();
      output.close();
    }
  
  else
    cout << "Unable to open file" << endl;
  
  return 0;
}
