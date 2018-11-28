#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int countSubstr(string name, int n);
bool hasEnoughConsonants(string name, int n);

int main(int argc, char * argv[])
{
  if(argc < 2)
    return 1;
  
  fstream input(argv[1]);
  char szLine[2000001] = "";
  string line;
  int spacePos;
  int n;
  int i = 1;
  
  if(input.fail())
  {
    cout <<"failed";
  }
  else
  {
    input.getline(szLine, 2000001);
    
    while(!input.eof())
    {
      input.getline(szLine, 2000001);
      line = szLine;
      
      if(line == "")
        break;
      
      spacePos = line.find(' ');
      n = atoi(line.substr(spacePos).c_str());
      
      
      
      printf("Case #%d: %d\n", i, countSubstr(line.substr(0, spacePos), n));
      
      i++;
    }
    
    
    input.close();
  }
  return 0;
}

const string vowels = "aeiou";

int countSubstr(string name, int n)
{
  int count = 0;
  int i, j, k, l;
  int length = name.length();
  string sub;
  
  for(i = 0; i < length; i++)
  {
    for(j = i + n; j < length + 1; j++)
    {
      if(hasEnoughConsonants(name.substr(i, j - i), n))
        count++;
    }
  }
  
  return count;
}

bool hasEnoughConsonants(string name, int n)
{
  int count = 0;
  int i = 0;
  int length = name.length();
  
  while(i < length)
  {
    if(vowels.find(name[i]) !=-1)
      count = 0;
    else
      count++;
    
    if(count >= n)
      return true;
      
    i++;
  }
  
  return false;
}

