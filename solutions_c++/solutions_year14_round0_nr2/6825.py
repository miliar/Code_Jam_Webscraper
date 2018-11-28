#include <iostream>
#include <fstream>
#include <iomanip>

double time(double c,double f,double x)
{
	double times=0.0;
	double rate=2.0;
	long count=0;
	double time1,time2;
	time1=x/(rate*1.0000000);
	time2=c/(rate*1.0000000) + x/((rate+f)*1.0000000);
	if(time1<time2)
	return x/(rate*1.0000000);
	else
	times+=c/(rate*1.0000000);
	time1=(x-c)/(rate*1.0000000);
	time2=x/((rate+f)*1.0000000);
	while(time1>time2)
	{
		rate+=f;
		time1=(x-c)/(rate*1.0000000);
		time2=x/((rate+f)*1.0000000);
		times+=c/(rate*1.0000000);
	}
	times+=time1;
	return times;
}
	

using namespace std;

int main()
{
	int t;
	double C,F,X;
	double res;
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("jam2output.txt");
	input>>t;
	output.precision(7);
	for(int i=0;i<t;i++)
	{
		input>>C>>F>>X;
		res=time(C,F,X);
		output<<"Case #"<<i+1<<": "<<fixed<<res<<'\n';
	}
	return 0;
}

