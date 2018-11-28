//Google Code Jam 2013
//Problem C
//Nishanth Koganti

#include <stdio.h>
#include <memory.h>
#include <string.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

bool ispal(unsigned long long a)
{
  unsigned long long b = 0;
  unsigned long long temp = a;
  while(temp > 0)
    {
      b = b*10 + temp%10;
      temp = temp/10;
    }
  if(a == b)
    return true;
  else
    return false;
}

bool isrootpal(unsigned long long a)
{
  unsigned long long root = 1;
  while((root*root) < a)
    root++;
  if((root*root) != a)
    return false;
  
  unsigned long long b = 0;
  unsigned long long temp = root;
  while(temp > 0)
    {
      b = b*10 + temp%10;
      temp = temp/10;
    }
  if(root == b)
    return true;
  else
    return false;
}

int main(int argc, char** argv)
{
  string line,str;
  stringstream ss;
  ifstream input;
  ofstream output;
  input.open(argv[1]);
  output.open(argv[2]);

  int T;
  unsigned long long A,B;
  unsigned long long a;
  unsigned long long N;
  bool pal,rootpal;

  if(input.is_open())
    {
      getline(input,line);
      ss << line;
      ss >> T;
      ss.clear();

      for(int t = 0; t < T; t++)
	{
	  getline(input,line);
	  ss << line;
	  ss >> A;
	  ss >> B;
	  ss.clear();
	  
	  a = A;
	  N = 0;
	  while(a <= B)
	    {
	      pal = ispal(a);
	      rootpal = isrootpal(a);
	      if(pal && rootpal)
		N++;
	      a++;
	    }

	  output << "Case #" << t+1 << ": " << N << endl;
	}
      input.close();
      output.close();
    }

  else 
    cout << "Unable to open file";
  
  return 0;
}
