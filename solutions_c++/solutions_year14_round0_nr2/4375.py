#include<iostream>
#include<iomanip>
#include<fstream>
#include<algorithm>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	fin.open("B_large.in");
	fout.open("b_large.out");
	
	int T = 0;
	double C = 0.0 , F = 0.0 , X = 0.0;
	double total , time1 , time2;
	double current_F = 0.0;
	int i , j , k , input , output;
	
	fin >> T;
	
	for( int t = 1 ; t <= T ; ++t )
	{
		fin >> C >> F >> X;

		total = 0.0;
		current_F = 2.0;
		
		time1 = X/current_F;
		time2 = C/current_F + X/(current_F+F);
		if( time1 <= time2 )
			total = X/current_F;
		else
			total = C/current_F;

		while( time2 < time1 )
		{
			current_F += F;
			time1 = X/current_F;
			time2 = C/current_F + X/(current_F+F);

			if( time1 <= time2 )
				total += X/current_F;
			else
				total += C/current_F;
		}
		
		fout << "Case #" << t << ": " << setprecision(7) << fixed << total << endl;
	}
	
	return 0;
}
