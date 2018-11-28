#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <set>

using namespace std;

class TicTacToeTomek
{
public:
  enum State{
    XWON,
    OWON,
    DRAW,
    INCOMPLETE
  };
  
  TicTacToeTomek(string s);
  State getResult();

private:
  int data[16];
};

TicTacToeTomek::TicTacToeTomek(string s)
{
  for(unsigned i = 0; i < s.length(); i++) {
    if (s.at(i) == 'X')
      data[i] = 17;
    else if (s.at(i) == 'O')
      data[i] = 69;
    else if (s.at(i) == 'T')
      data[i] = 1;
    else
      data[i] = 0;
  }
}

TicTacToeTomek::State TicTacToeTomek::getResult()
{
  set<int> myset;

  for (unsigned i = 0; i < 16; i+=4)
    myset.insert(data[i] + data[i+1] + data[i+2] + data[i+3]);
  for (unsigned i = 0; i < 4; i++)
    myset.insert(data[i] + data[i+4] + data[i+8] + data[i+12]);

  myset.insert(data[0] + data[5] + data[10] + data[15]);
  myset.insert(data[3] + data[6] + data[9] + data[12]);
  
  if (myset.find(68) != myset.end()) 
    return XWON;
  else if (myset.find(276) != myset.end())
    return OWON;
  else if (myset.find(52) != myset.end())
    return XWON;
  else if (myset.find(208) != myset.end())
    return OWON;
  else {
    for (unsigned i = 0; i < 16; i++)
      if (data[i] == 0)
	return INCOMPLETE;
    return DRAW;
  }
}

int main(int argc, char* argv[])
{
  ifstream inFile;
  inFile.open(argv[1]);
  if (!inFile) {
    cout<<"Unable to open : "<<argv[1]<<endl;
    return 0;
  }

  string strLine;
  getline(inFile, strLine);
  int TCCount = atoi(strLine.c_str());
  for(unsigned i = 0; i < TCCount; i++) {
    string temp = "";
    getline(inFile, strLine);
    temp += strLine;
    getline(inFile, strLine);
    temp += strLine;
    getline(inFile, strLine);
    temp += strLine;
    getline(inFile, strLine);
    temp += strLine;
    getline(inFile, strLine);
    TicTacToeTomek t(temp);
    string result = "Case #";
    ostringstream convert;
    convert << (i+1);
    result += convert.str();
    result += ": ";
    switch(t.getResult()) {
    case TicTacToeTomek::XWON:
      result += "X won";
      break;
    case TicTacToeTomek::OWON:
      result += "O won";
      break;
    case TicTacToeTomek::DRAW:
      result += "Draw";
      break;
    case TicTacToeTomek::INCOMPLETE:
      result += "Game has not completed";
      break;
    }
    cout<<result<<endl;
  }

  inFile.close();
  return 0;
}
