#include <iostream>
#include <sstream>
#include <fstream>
#include <string.h>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	ifstream in;
	in.open ("B-large.in");
	
	ofstream out;
	out.open ("output_large.txt");
	
	int t;
	in >> t;
	
	double c;
	double f;
	double x;
	double time = 0.0;
	double chk_time = 0.0;
	double total_time = 0.0;
	double rate;
	
	out.precision(7);
	
	for (int i=0; i<t; i++)
	{
		time = 0.0;
		chk_time = 0.0;
		total_time = 0.0;
		
		in >> c;
		in >> f;
		in >> x;
		
		rate = 2;
		
		if (x <= c)
		{
			time = x/rate;
			//printf("Case #%d: %.7f\n", i+1, time);
			out << "Case #" << i+1 << ": " << fixed << time << endl;
		}
		else
		{
			for (int j=0; ; j++)
			{
				time = chk_time + (x/rate);
				
				chk_time = chk_time + (c/rate);
				rate = rate + f;
				
				total_time = chk_time + (x/rate);
				
				if (total_time > time)
				{
					//printf("Case #%d: %.7f\n", i+1, time);
					out << "Case #" << i+1 << ": " << fixed << time << endl;
					break;
				}
				
			}
		}
	}
	
	in.close();
	out.close();
	
	return 0;
}
