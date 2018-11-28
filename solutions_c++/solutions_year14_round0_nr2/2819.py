#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int t;
	double *result;
	fin>>t;
	result = new double[t];
	for (int i=0;i<t;i++)
	{
		double C,F,X;
		fin>>C>>F>>X;
		double cookie_p_s = 2.0;
		result[i] = X/cookie_p_s;
		double cur_zero = 0;
		double cur_fin = 0;
		while(true)
		{
			double cur = C/cookie_p_s;
			cookie_p_s += F;
			cur_zero += cur;
			cur_fin = X/cookie_p_s;
			if((cur_zero + cur_fin) > result[i])
				break;
			else
				result[i] = cur_zero + cur_fin;
		}
	}
	for (int i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<result[i]<<endl;
	}
}