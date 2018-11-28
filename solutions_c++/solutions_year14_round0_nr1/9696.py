// Qualification Round Code Jam 2014
// ABHINAV DADHICH

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
  vector<int> line1, line2;
  vector<int>::iterator iterator1, iterator2;

  int T, t, i, j, temp, number, result;
  int ans1, ans2;
  
   if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(t = 1; t <= T; t++)
	{
	  number = 0;
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

	  iterator1 = line1.begin();
	  iterator2 = line2.begin();

	  while(iterator1 != line1.end() && iterator2 != line2.end())
	    {
	      if(*iterator1 < *iterator2)
		++iterator1;
	      else if(*iterator1 == *iterator2)
		{
		  number++;
		  result = *iterator1;
		  ++iterator1; ++iterator2;
		}
	      else
		++iterator2;
	    }

	  if(number == 0)
	    output << "Case #" << t << ": Volunteer cheated!" << endl;
	  else if(number == 1)
	    output << "Case #" << t << ": " << result << endl;
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
