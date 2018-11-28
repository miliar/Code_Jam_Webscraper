#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
double c,f,x;
double func(double bal,double rate)
{
	double t=0;
	while(x/rate>=x/(rate+f)+c/rate)
	{
		t+=c/rate;
		rate+=f;
	}
	t+=x/rate;
	return t;
}
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("Output2.txt");
	int T;
	fin>>T;
	for(int i=0;i<T;i++)
	{
	fin>>c>>f>>x;
	fout.setf(ios::fixed);
	fout.setf(ios::showpoint);
	fout.precision(7);
	fout<<"Case #"<<i+1<<": "<<func(0.0,2.0)<<endl;
	}
	
}


