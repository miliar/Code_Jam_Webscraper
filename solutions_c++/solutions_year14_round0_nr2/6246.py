#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
  ifstream input("B-large.in");
  ofstream output;
  output.open("output.txt");

  output << fixed << setprecision(7);
  
  string caseString;
  getline(input, caseString);
  int cases = atoi(caseString.c_str());
  for (int i = 0; i < cases; i++)
    {
      //debug
      cout << "Case: " << i+1 << endl; 
      
      string condition;
      getline(input, condition);
      stringstream ss(condition);
      double C;
      ss >> C;
      double F;
      ss >> F;
      double X;
      ss >> X;

      double totalN = 0;
      double n = 0;
      double rate = 2.0;
      double base = F * (X - C) / C;

      for (double j = 2; j < base; j+=F)
	{
	  totalN += C / j;
	  rate += F;
	}
      totalN += X / rate;
      output << "Case #" << i+1 << ": " << totalN << endl;
    }
}
