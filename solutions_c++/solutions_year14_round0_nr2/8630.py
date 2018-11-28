// ProgrammingCompetition.cpp : Defines the entry point for the console application.
//

#include "windows.h"

#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <string>
#include <sstream>

using namespace std;

double compute(double C, double F, double X, double rate){

	if(X<C)
		return X/rate;

	double time = C/rate;

	X=X-C;
	double buy = ((X+C)/(rate+F));

	double dont_buy = (X)/rate;
	
	if( dont_buy < buy )
		return time + compute(C,F,X,rate);
	else
		return time + compute(C,F,X+C,rate+F);

}

int main () {
  ifstream ifs("C:\\input.in");
  ofstream output;
  output.open("C:\\output.txt",std::ofstream::out);
  //ifs.open("input.txt");
  string l1, l2;
  getline(ifs, l1);
  stringstream ss1(l1);
  int no_of_cases;
  double C,F,X;
  ss1 >> no_of_cases;

 
  double ans;

  for(int i=0;i<no_of_cases;i++)
  {
	 getline(ifs,l2);
	 stringstream ss2(l2);
	 ss2>>C>>F>>X;

	 ans = compute(C,F,X,2); //recursive function call to compute value

	 stringstream ss;  //for correct precision
	 ss.precision(7);
	 ss<<fixed;


	 ss<<"Case #"<<i+1<<": "<<(double)ans<<"\n";
	 output<<ss.str();//<<"Case #"<<i+1<<": "<<(double)ans<<"\n";
	 ss<<"";
	 ss.clear();
  }
  ifs.close();
  output.close();
  return 0;
}
