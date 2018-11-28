#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>

using namespace std;


int main(int argc, char* argv[] )
{
	ifstream input;
	char* buffer = new char[50];
	input.open(argv[1]);

	ofstream output;
	output.open("output");	

	input.getline(buffer,50);
	int numTest = atoi(buffer);

	double C,X,F;

	output << fixed << setprecision(8);
	cout << fixed << setprecision(6);

	for(int test = 0;test<numTest;test++)
	{
		input.getline(buffer,50);
		sscanf(buffer,"%lf %lf %lf",&C,&F,&X);
		cout << C << '\t' << F << '\t' << X << '\n';

		double d = 2.0;
		double t_prev = X/d;
//		cout << t_prev << '\n';

		while(1)
		{
			double t_new = t_prev - (X/d) + (C/d) + (X/(d+F));
			d = d + F;
			if(t_new > t_prev)
				break;

			t_prev = t_new;
//			cout << t_prev << '\n';
		}

		output << "Case #" << test+1 << ": " << t_prev << '\n';
//		cout << "\n\n";
	}

	input.close();
	output.close();

	return 0;
}


