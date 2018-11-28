#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

double C, F, X;

inline double twodec(double n) { return floor(n*1000000+0.5)/1000000; }

double GetLeastTime()
{
  double d = X*F/C-F;
  
  double speed=2.0;
  double time=0;

  cout << "X: " << X << " F: " << F << " C: " << C << " d: " << d << endl;
  while(d-speed > 0.0000001)
    {
      time+=C/speed;
      speed+=F;
    }
    
    time += X/speed;

    return time;
}

int main()
{
  fstream input;
  ofstream output;
  string line;
  unsigned caseN;
  input.open("input");
  output.open("output");
  getline(input, line);
  istringstream iss(line);
  iss >> caseN;

  for(int i=1; i<=caseN; ++i)
    {
      getline(input, line);
      istringstream iss(line);
      iss >> C >> F >> X;

      //original speed is 2
      double time = GetLeastTime();
     
      output << "Case #" << i <<": "<<std::fixed<<setprecision(7)<<time<< endl;
    }

  input.close();
  output.close();

  return 1;
}
