#include<fstream>
#include<string>
#include<set>
#include <iomanip>

using namespace std;

	fstream fin("e:/1.in");
	fstream fout("e:/1.out");

double calc()
{
	double result;
	double c,f,x;
	double a = 2;
	result = 0;
	fin >> c >> f >>x;
	while ((x-c) * (a+f) > a * x)
	{
		result += c / a;
		a = a + f;
	}
	result += x/ a;
	return result;
}

int main()
{

	int t;
	fin >> t;	
	for (int i=0; i<t; i++)
	{		
		double result;
		result = calc();
		fout <<"Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<result<<endl;
	}
	fin.close();
	fout.close();
}