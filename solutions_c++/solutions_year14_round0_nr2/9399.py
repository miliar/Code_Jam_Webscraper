#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
using namespace std;

int T;
double C,F,X;

double getTime(int numFarms)
{
	double prod = 2;
	double time = 0;

	for (int i=0; i<numFarms; i++){
		time += C/prod;
		prod += F;
	}
	
	time += X/prod;
	return time;
}


int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("Sevag_probB_out.txt");

	cin>>T;

	for (int t=1; t<=T; t++)
	{
		cin>>C>>F>>X;
		
		double best=1000000000;
		int numFarms=0;
		double ans = getTime(numFarms++);
		while (ans<best){
			best = ans;
			ans = getTime(numFarms++);
		}

		cout<<fixed<<setprecision(7)<<"Case #"<<t<<": "<<best<<endl;
	}

	return 0;
}
