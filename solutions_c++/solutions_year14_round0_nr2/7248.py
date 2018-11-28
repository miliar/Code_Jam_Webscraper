#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<string>

using namespace std;

void main()
{

	
	int loop;
	double C, F, X;
	double t; // the pseudo time variable
	double rate = 2.0;
	double time = 0.0;
	ifstream  infile;
	infile.open("new.txt");


	ofstream outfile;
	outfile.open("out.txt");
	
	infile >> loop;

	for (int h = 0; h < loop; h++)
	{

		double rate = 2.0;
		double time = 0.0;
		infile >> C;
		infile >> F;
		infile >> X;


		while (true)
		{
			t = C / rate;
			if ((X / (rate + F)) > ((X / rate) - (t)))
			{
				time += (X / rate);
				break;
			}
			else
			{
				time += t;
				rate += F;
			}

		}

		//std::cout.precision(10);
		outfile << "Case #" << h + 1 << ": ";
		outfile << fixed << setprecision(7) << time << endl;

	}



}