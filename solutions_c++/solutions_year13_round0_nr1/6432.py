#include <iostream>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;

#define get std::cin

char matrix [5][5];
bool ifanydot()
{
  bool dot = false;
  for(int i=0; i<4;++i)
  {
    for(int j=0; j<4;++j)
    {
      if(matrix[i][j] == '.')
      {
        dot = true;
      }
    }
  }
  return dot;
}

bool ifwon(char * player)
{
  bool gorizon = true;
  bool vert = true;
  bool diag1 = true;
  bool diag2 = true;

  for(int i=0; i<4;++i)
  {
    for(int j=0; j<4;++j)
    {

      char val = matrix[i][j];
      gorizon &= ( val== *player) || (val == 'T');
      val = matrix[j][i];
      vert &= ( val == *player) || (val == 'T');

    }
    char val;
    val = matrix[i][i];
    diag1 &= ( val == *player) || (val == 'T');

    val = matrix[i][3-i];
    diag2 &= ( val == *player) || (val == 'T');

    if(gorizon || vert)
    {
      return true;
    }
    gorizon = true;
    vert = true;
  }
  if(diag1 || diag2)
  {
    return true;
  }
  return false;
}

int main()
{
  std::ifstream inFile;
  inFile.open("/home/dez/src/jam-0/A-large.in", std::ios::in);
  int testCases(0);
  inFile >> testCases;
  for(int j = 1; j<= testCases; ++j)
  {
    std::string line;
    std::getline(inFile,line);
    for(int i = 0; i<4; ++i)
    {

      std::getline(inFile,line);
      strcpy(&matrix[i][0], line.c_str());
    }
    if(ifwon("X"))
    {
      std::cout << "Case #" << j <<": X won\n";
    }else
      if(ifwon("O"))
    {
      std::cout << "Case #" << j <<": O won\n";
    }else if(ifanydot())
    {
      std::cout << "Case #" << j <<": Game has not completed\n";
    }else{
      std::cout << "Case #" << j <<": Draw\n";
    }
  }
  return 0;
}

