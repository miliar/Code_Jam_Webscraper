#include <iostream>
#include <cmath>
#include <list>
#include <fstream>

using namespace std;


int main()
{
	int T, count;
	double r, t;
	double area = 0;
	double radius = 0;
	ifstream infile;
	ofstream outfile;
	infile.open("C:\\Users\\Riham\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Bullseye\\Bullseye\\A-small-attempt0.in");
	outfile.open("C:\\Users\\Riham\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Bullseye\\Bullseye\\output.txt");
	infile>>T;

	for(int j=1; j<=T; j++)
	{
		count = 0;
		area = 0;
		radius = 0;
		double b_area = 0;
		infile>>r>>t;
		while(t > 0)
		{
			area = pow(r,2);
			radius = r + 1;
			b_area = pow(radius,2) - area;

			if(!(b_area > t))
			{
				count ++;
				t -= b_area;
				r += 2;
			}
			else
				t = 0;
		}
		outfile<< "Case #"<<j<<": "<<count<<endl;
	}
}