#include <iostream>
#include <fstream>
#include <iomanip>      //包含此头文件
#include <vector>
using namespace std;

vector<double> result;

void calc(double C, double F, double X)
{
	double rate=2, ret=0; 
	if(X < C)
	{
		result.push_back(X/rate);
		return;
	}
	else{
		while(X/(rate+F) < (X-C)/rate)
		{
			ret += C/rate;
			rate +=F;
		}
		ret += X/rate;
		result.push_back(ret);
	}
}
int main()
{
	ifstream infile;
	infile.open("B-large.in");
	int T;
	double C, F, X;
	infile>>T;
	while(T--)
	{
		infile>>C>>F>>X;
		calc(C,F,X);
	}
	infile.close();
	ofstream outfile;
	outfile.open("B-large.out");
	for(int i=0;i<result.size();i++)
		outfile<<"Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<result[i]<<endl;
	outfile.close();
	return 0;
}