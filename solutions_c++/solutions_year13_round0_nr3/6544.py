#include <iostream>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <math.h>

using namespace std;

void runCommandLoop();
int runChecks(long lBound, long hBound);
bool checkFair(long i);
bool checkSquare(long i);
string intToStr(long i);
void print(int outputNum, int output);

int main()
{
  runCommandLoop();
  return 0;
}

void runCommandLoop()
{
  int nInput, lBound, hBound, output;
  
  cin >> nInput;
  for(int i = 0; i < nInput; i++)
  {
    cin >> lBound >> hBound;
    output = runChecks(lBound, hBound);
    print(i+1, output);
  }
}

void print(int outputNum, int output)
{  
  cout << "Case #" << outputNum << ": " << output << endl;
}

int runChecks(long lBound, long hBound)
{
  int count = 0;
  
  for(long i = lBound; i < hBound+1; i++)
  {
    if(checkFair(i) && checkSquare(i))
    {
      count++;
    }
  }
  return count;
}

bool checkFair(long i)
{
  string fair = intToStr(i);
  int nChar = fair.length();
  for(int j = 0; j < nChar; j++)
  {
    if(j >= (nChar-1) - j)
    {
      break;
    }
    if(fair[j] != fair[(nChar-1) - j])
    {
      return false;
    }
  }
  return true;
}

bool checkSquare(long i)
{
  double junk;
  long double fract = modf(sqrt(i), &junk);
  if(fract == 0)
  {
    return checkFair(sqrt(i));
  }
  return false;
}

string intToStr(long i)
{
  stringstream ss;
  ss << i;
  string s = ss.str();
  return s;
}



