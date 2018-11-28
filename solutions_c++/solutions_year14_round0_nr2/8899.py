//by Lilli Christoph
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
// #include <algorithm>
// #include <map>
// #include <cstdlib>
#include <cmath>

using namespace std;

int main(void)
{
  int numCases;
  double r=2.0, c, x, f, n, t1, t2, time;
  int nMin, nMax;

  string inputfile = "B-large.in";
 
  //Load input from file
  ifstream inputFile(inputfile.c_str());
  inputFile >> numCases;

  //Get case data
  for(int i=0; i<numCases; i++)
    {
      inputFile >> c;
      inputFile >> f;
      inputFile >> x;
      n = x/c - r/f - 1.0;
      nMin = (int)n;
      nMax = nMin +1;
      t1 = 0.0;
      if(nMin<=0)
	{
	  nMin=0;
	  nMax=1.0;
	}
      else
	for(int j=0; j<nMin; j++)
	  t1 = t1 + c/(r+(double)j*f);
      t2 = t1 + c/(r+(double)nMin*f) + x/(r+((double)nMin+1.0)*f);
      t1 = t1 + x/(r+(double)nMin*f);
      time = min(t1, t2);

      //OutputResults
      cout << "Case #" << i+1 << ": " <<  std::setprecision(10) <<time << endl;
    }

  return 0;
}
