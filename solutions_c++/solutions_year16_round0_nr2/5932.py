#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>

using namespace std;

void printAll (string i) {  // function:
  std::cout << ' ' << i;
  }

vector<string> split(const string &s, char delim) {
  stringstream ss(s);
  string item;
  vector<string> elems;
  while (getline(ss, item, delim)) {
    elems.push_back(item);
  }
  return elems;
}

int main(int argc, char* argv[])
{
  /**
   * Static
   */
  if(argc != 2)
    {
      cerr << "argc != 2" << '\n';
      return 0;
    }

  ifstream infile;
  infile.open (argv[1]);

  string inputLine;
  uint16_t numCases;
  getline(infile, inputLine);
  stringstream ss(inputLine);

  //int L, D;

  //ss >> L;
  //ss >> D;
  ss >> numCases;

  /**
   * Fileread
   */
  //int value;
  //vector<vector<int> > data;
  //string substring;
  vector <string> stringVec, alienDict;
  //vector <vector <string> > string2DVec;

  while(getline(infile, inputLine))
    {
      stringVec.push_back(inputLine);
    }
  /*
  cout << "stringVec: " << endl;
  for_each (stringVec.begin(), stringVec.end(), printAll);
  cout << endl;
  */
  infile.close();

  /**
   * Problem
   */
  char prevSymbol;
  int stringLength, flips;
  for (int caseNumber = 0; caseNumber < numCases; caseNumber++)
    {
      prevSymbol = '0';
      stringLength = 0;
      flips = 0;

      for (auto c : stringVec[caseNumber])
        {
          if (c == prevSymbol || prevSymbol == '0')
            {
              ++stringLength;
              prevSymbol = c;
            }
          else
            {
              stringVec[caseNumber].replace(0, stringLength, stringLength, c);
              ++flips;
              prevSymbol = c;
            }
        }
      if (stringLength > 0 && prevSymbol == '-')
        {
          ++flips;
        }

      cout << "Case #" << caseNumber+1 << ": ";
      cout << flips << endl;
    }
  
  return 0;
}
