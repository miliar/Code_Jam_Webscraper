#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <iomanip>

using namespace std; 

int main()
{
	ifstream input_data;
	ofstream output_data;
	
	//input_data.open("B-small-attempt0.in");
	//output_data.open("B-small-attempt0.out");

	input_data.open("B-large.in");
	output_data.open("B-large.out");

	int T(0); // number of test cases
	input_data >> T;
	// loop through all test cases
	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		input_data >> C;
		input_data >> F;
		input_data >> X;
		double R = 2.0;
		double T_o(0);
		double Tn(0);
		double currT(0);
		int c = 1;
		T_o = X / R;
		currT = T_o;
		do
		{
			if (Tn > 0)
			{
				currT = Tn;
			}
			Tn = X / (R + c * F);
			for (int t = 0; t < c; t++)
			{
				Tn = Tn + (C / (R + t * F));
			}
			c++;
		} while (Tn < currT);
		// Print out the minimum time
		output_data << "Case #" << (i + 1) << ": " << setprecision(7) << fixed << currT << endl;
	}
	input_data.close();
	output_data.close();
	return 0;
}