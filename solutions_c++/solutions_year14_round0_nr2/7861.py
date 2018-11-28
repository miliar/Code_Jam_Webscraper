#include <iostream>
#include <fstream>

using namespace std;

void main(){

	short int T = 0;

	ifstream input("B-large.in");
	ofstream output("output.txt");

	input>>T;

	for(short int i = 0; i < T; i++){

		double C = 0, F = 0, X = 0;
		input>>C;
		input>>F;
		input>>X;
		double persecond = 2;
		double totaltime = C/persecond + X/(persecond + F), time = X/persecond;
		while (totaltime < time)
		{
			persecond += F;
			totaltime -= X/persecond;
			
			time = totaltime + X/persecond;
			totaltime += C/persecond+X/(persecond+F);
		}
		output.setf(std::ios::fixed);
		output.precision(7);
		output<<"Case #"<<i+1<<": "<<time<<endl;
	};
	system("pause");
}