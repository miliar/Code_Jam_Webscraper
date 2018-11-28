#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
  ifstream input("A-small-attempt1.in");
  ofstream output;
  output.open("answer.txt");

  string cases_str;
  getline(input, cases_str);
  int cases = atoi(cases_str.c_str());

  //debug
  cout << cases << endl;
  for (int i = 0; i < cases; i++)
    {
      //debug
      cout << "case: " << i << endl;
      
      string firstRowIndex_str;
      getline(input, firstRowIndex_str);
      int firstRowIndex = atoi(firstRowIndex_str.c_str());

      cout << "first " << firstRowIndex << endl;
      vector<int> firstRow;
      for (int j = 1; j <= 4; j++)
	{
	  if (j == firstRowIndex)
	    {
	      string line;
	      getline(input, line);
	      //debug
	      cout << line << endl;
	      stringstream ss(line);
	      int num;
	      while (ss >> num)
		{
		  firstRow.push_back(num);
		}
	    } 
	  else 
	    {
	      string dummy;
	      getline(input, dummy);
	      //debug;
	      cout << "dummy: " << dummy << endl;
	    }
	}
      string secondRowIndex_str;
      getline(input, secondRowIndex_str);
      int secondRowIndex = atoi(secondRowIndex_str.c_str());

      cout << "second " << secondRowIndex << endl;
      
      vector<int> secondRow;
      for (int j = 1; j <= 4; j++)
	{
	  if (j == secondRowIndex)
	    {
	      string line;
	      getline(input, line);
	      cout << line << endl;
	      int num;
	      stringstream ss(line);
	      while (ss >> num)
		{
		  secondRow.push_back(num);
		}
	    } 
	  else 
	    {
	      string dummy;
	      getline(input, dummy);
	      //debug;
	      cout << "dummy: " << dummy << endl;
	    }
	}
      int identical = 0;
      int theNum;
      for (int j = 0; j < 4; j++)
	{
	  if (find(secondRow.begin(), secondRow.end(),
		   firstRow.at(j)) != secondRow.end())
	    {
	      theNum = firstRow.at(j);
	      identical++;
	    }
	  if (identical > 1)
	    {
	      break;
	    }
	}
      if (identical == 1)
	{
	  output << "Case #" << i+1 << ": " << theNum << endl;
	  cout << "THE NUM: " << theNum << endl;
	}
      else if (identical == 0)
	{
	  output << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
	}
      else 
	{
	  output << "Case #" << i+1 << ": " << "Bad magician!" << endl;
	}
    }
}
