#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;

	int number_of_test;
	double rate=2.0;
	double total_time=0.0;
	double C,F,X;

	input.open("B-large.in");
	output.open("output");

	input>>number_of_test;
	
	for (int i=0; i<number_of_test; i++)
	{
		input>>C>>F>>X;

		while (1)
		{
			if ( C/rate + X/(rate+F) < X/rate )
			{
				total_time+=C/rate;
				rate+=F;
			}

			else
			{
				total_time+=X/rate;
				break;
			}
		}
		
		output<<"Case #"<<i+1<<": "<<setprecision(15)<<total_time<<endl;

		rate=2.0;
		total_time=0.0;
	}

	input.close();
	output.close();

	system("PAUSE");
	return 0;
}