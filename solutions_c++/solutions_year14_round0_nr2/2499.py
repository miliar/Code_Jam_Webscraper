#include <iostream>
#include <vector>
#include <algorithm>
#include <istream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(void)
{
	double C =0.0;
	double F = 0.0;
	double X = 0.0;
	double currentRate = 2.0;
	ifstream read("input.txt");
	ofstream write("output.txt");
	write.precision(7);
	write.setf( std::ios::fixed);
	int T;
	read>>T;
	for(int i=0;i<T;i++)
	{
		double time = 0.0;
		double left = 0.0;
		double goingwithNewRate = 0.0;
		double right = 0.0;
		currentRate = 2.0;

		read>>C>>F>>X;
		while(1)
		{
			left = time + X/currentRate;
		
			goingwithNewRate = X/(currentRate+F);
			right = time+ C/currentRate + goingwithNewRate;
			if(right<left)
			{
				time += C/currentRate;
				currentRate +=F;
			}
			else
				break;
		}
		write<<"Case #"<<i+1<<": "<<left<<endl;
	}
	return 0;
}

