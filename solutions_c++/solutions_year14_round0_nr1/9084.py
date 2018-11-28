//assuming the input and out filenames are input & output
#include <set>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

void ReadFromInputAndProcess()
{
  unsigned caseN;
  unsigned NumTestCases;
  ofstream output;
  output.open("output");
  //read from 1st line of the file
  ifstream input;
  string line;
  input.open("input");
  getline(input, line);
  istringstream iss(line);
  iss >> NumTestCases;
  cout << "NumTestCases: " << NumTestCases << endl;

 caseN=1;
  set<int> RowInFirstGuess, RowInSecondGuess;
  unsigned FirstGuessRow, SecondGuessRow;
  while(caseN <= NumTestCases)
    {
      RowInFirstGuess.clear();
      RowInSecondGuess.clear();
      //read FirstGuessRow
      getline(input, line);
      istringstream iss(line);
      iss >> FirstGuessRow;
      cout << "FirstGuessRow: " << FirstGuessRow << endl;
      for(unsigned i=1; i< 5; ++i)
	{
	  //read a line
	  getline(input, line);
	  if(i==FirstGuessRow)
	    {
	      //set value RowInFirstGuess
	      int a, b, c, d;
	      istringstream iss(line);
	      iss >> a >> b >> c >> d;
	      cout << "a: " << a << " b: " << b << " c: " << c << " d: " << d << endl;
	      RowInFirstGuess.insert(a);
	      RowInFirstGuess.insert(b);
	      RowInFirstGuess.insert(c);
	      RowInFirstGuess.insert(d);
	    }
	}

      //read SecondGuessRow
      getline(input, line);
      istringstream iss2(line);
      iss2 >> SecondGuessRow;
      cout << "SecondGuessRow: " << SecondGuessRow << endl;
      for(unsigned j=1; j<5; ++j)
	{
	  //read a line
	  getline(input, line);
	  if(j==SecondGuessRow)
	    {
	      //set value RowInSecondGuess
	      int a, b, c, d;
	      istringstream iss(line);
	      iss >> a >> b >> c >> d;
	      cout << "a: " << a << " b: " << b << " c: " << c << " d: " << d << endl;
	      RowInSecondGuess.insert(a);
	      RowInSecondGuess.insert(b);
	      RowInSecondGuess.insert(c);
	      RowInSecondGuess.insert(d);
	    }
	}

      //print result
      vector<int> v(4);
      vector<int>::iterator it = set_intersection(RowInFirstGuess.begin(), RowInFirstGuess.end(), RowInSecondGuess.begin(), RowInSecondGuess.end(), v.begin());
      v.resize(it-v.begin());
      cout << "v.size(): " << v.size() << endl;
      ostringstream ss, ss2;
      ss << caseN;
      ss2 << v[0];
      if(v.size()==1)
	{
	  output << "Case #"+ss.str()+": "<< ss2.str() << endl;
	}
      else if(v.size() > 0)
	{
	  output << "Case #"+ss.str()+": Bad magician!" << endl;
	}
      else
	{
	  output << "Case #"+ss.str()+": Volunteer cheated!" << endl;
	}
      ++caseN;
    }
}

int main()
{
  ReadFromInputAndProcess();

  return 1;
}
