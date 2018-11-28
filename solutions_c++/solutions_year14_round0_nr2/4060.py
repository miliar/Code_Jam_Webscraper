#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ofstream outfile;
	outfile.open("outputCookiesL.out");
	ifstream infile;
	infile.open("B-large.in");
	int testCase;
	infile>>testCase;
	for(int i=1;i<=testCase;++i) {
		//cout<<i<<endl;
		double C,F,X;	
		double rate = 2.0;
		double time = 0.0;
		infile>>C>>F>>X;
		while(true) {
			if(X<=C)
			{time+=(X/rate); break;}
			double tempT = C/rate;
			double temp1 = (X-C)/rate;
			double temp2 = (X)/(rate+F);
			if(temp1>temp2) 
			{	rate += F; time+=tempT;}
			else 
			{time+=(X/rate); break;}
		}
		outfile<<"Case #"<<i<<": "<<std::fixed << std::setprecision(7)<<time<<endl;
	}
}
