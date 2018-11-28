#include "Parser.h"

#include <cstdlib>
#include <fstream>
#include <istream>
#include <sstream>

Parser::Parser()
{
}

std::vector<int> * Parser::load(const std::string& filename)
{
  std::vector<int> * answerdList =  new std::vector<int>();
  std::vector<int> tmpList;
  std::vector<int> tmpList2;

  std::ifstream file(filename.c_str());
  if(!file)
  {
    std::cerr << "Error: Cannot open file: " << filename << std::endl; 
    exit(1);
  }

  std::string line;
  getline(file, line);
  std::stringstream s(line);

  int testCaseNumber;
  s >> testCaseNumber;

  for(int i=0; i<testCaseNumber; i++)
  {
    tmpList.clear();
    tmpList2.clear();
    for(int j=0; j<2; j++)
    {
      int n;

      getline(file, line);
      {
        std::stringstream s(line);
        s >> n;
      }
      for(int k=1; k<n; k++)
      {
        getline(file, line);
      }

      getline(file, line);
      std::stringstream s(line);

      if(j == 0)
      {
        for(int k=0; k<4; k++)
        {
          int card;
          s >> card;
          tmpList.push_back(card);
        }
      }
      else
      {
        for(int k=0; k<4; k++)
        {
          int card;
          s >> card;
          for(int l=0; l<4; l++)
          {
            if(card == tmpList[l])
            {
              tmpList2.push_back(card);
              std::cout << card << std::endl;
            }
          }
        }
        if(tmpList2.size() == 0)
        {
          answerdList->push_back(-1);
        }
        else if(tmpList2.size() > 1)
        {
          answerdList->push_back(0);
        }
        else
        {
          answerdList->push_back(tmpList2[0]);
        }
       }

      for(int k=n; k<4; k++)
      {
        getline(file, line);
      }
    }
  }
  return answerdList;
}

