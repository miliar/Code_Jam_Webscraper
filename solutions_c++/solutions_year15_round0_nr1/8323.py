#include<iostream>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

int calculate(size_t value, string line)
{
  int count = 0;
  int ret = 0;
  for(size_t uiCount = 0; uiCount <= value; ++uiCount)
  {
    if(count >= uiCount)
    {
      count = count + (line[uiCount] - 48);
    }
    else
    {
      int diff = uiCount - count;
      count = count + diff + (line[uiCount] - 48);
      ret = ret + diff;
    }
  }
  return ret;
}
int main()
{
  ifstream infile("input"); 
  string line;
  int lineNo = 0;
  size_t testCount = 0;
  size_t caseNo = 0;
  size_t value;
  bool cont = true;
  int ret = 0;
  while(getline(infile,line) && cont)
  {
    stringstream lineStream(line);
    ++lineNo;
    --testCount;
    if(lineNo == 1)
    { 
      lineStream >> value;
      testCount = value;
    } 
    else
    { 
      lineStream >> value;
      size_t uiSize = line.size();
      for(size_t uiCount = 0; uiCount != uiSize; ++uiCount)
      {
        if(line[uiCount] == ' ')
          ret = calculate(value, line.substr(uiCount + 1));
      }
      ++caseNo;
      cout<<"Case #"<<caseNo<<": "<<ret<<endl;
    } 
    cont = testCount;
  }
  return 0;
}
