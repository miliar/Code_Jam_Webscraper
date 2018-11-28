#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

double howLong(double c, double f, double x) 
{ 
  double sp = 2;  
  double time = 0; 
  while(true)
  {
      if(c / sp + x / (sp + f) > x / sp)
      {
          time += x / sp;
          break;
      } 
    time += c / sp; 
    sp += f;
  } 
  return time; 
} 

int main()
{
	/* code */
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	//cout<<t<<endl;
	fout<<setprecision(7)<<fixed;
	for (int i=0; i<t; i++)
	{
		double c, f, x;
		fin >> c >> f >> x;
		double res = howLong(c, f, x);
		fout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}