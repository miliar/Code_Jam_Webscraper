#include <iostream>
#include <fstream>
using namespace std;

double win_time(double C, double F, double X, double sp = 2.0, double t = 0.0)
{
	double temp_time;
	double signal;
	signal = F * C + C * sp - F * X;
	if(signal > 0.0)
	  return(t + X / sp);
	temp_time = C / sp;
	win_time(C, F, X, sp + F, t + temp_time);
}

int main()
{
	int iter_num;
	double C, F ,X;
    ifstream f2("e:\\B-small-attempt2.in");
	ofstream f1("e:\\output.txt");
    f2.setf(ios::fixed, ios::floatfield);
    f2.precision(8);
	f2>>iter_num;
    f1.setf(ios::fixed, ios::floatfield);
    f1.precision(8);
	for(int iter = 0; iter < iter_num; iter++){
		f2>>C;
		f2>>F;
		f2>>X;
		f1<<"Case #"<<iter + 1<<": "<<win_time(C,F,X)<<endl;	
	}
	return 0;
}

