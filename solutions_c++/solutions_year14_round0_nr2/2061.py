#include <iostream>
#include <fstream>
#include <iomanip> 
#include <string>
using namespace std;
void main()
{
	//ifstream in ("input.in");
	//ofstream out("output.out");
	ifstream in ("inputLarge.in");
	ofstream out("outputLarge.out");
	int T;
	in>>T;
	string str;

	for(int Case = 1; Case<=T; Case++)
	{
		double C = 0;
		double F = 0;
		double X = 0;
		in >> C;
		in >> F;
		in >>X;
		//cout<<setprecision(9)<< C <<" ";
		//cout<<setprecision(9)<< F <<" ";
		//cout<<setprecision(9)<< X <<endl;

		double r = 2.0;
		double time = 0.0;
		while ( X/r > C/r + X/(r+F))
		{
			time += C/r;
			r +=F;
		}
		time +=X/r;
		out<< "Case #" << Case <<": "<< setprecision(9) << time << endl;
	}

	in.close();
	out.close();
	//getchar();
}