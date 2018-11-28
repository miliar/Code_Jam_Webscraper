#include<iostream>
#include<stdio.h>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	int test, index;
	double c, f, x,total,cookies,rate;

	fstream fp("B-small-practice.in", ios::in);
	fstream op("B-small-practice.out", ios::out);

	op << fixed << showpoint;
	op << setprecision(7);

	index = 0;
	fp >> test;
	while (test--)
	{

		fp >> c >> f >> x;
		total = 0.0;
		cookies = 0;
		rate = 2.0;

		while (cookies < x)
		{
			if ( (x / rate)>((c / rate) + (x / (rate + f))) )
			{
				total+= (c / rate);
				rate += f;
			}
			else
			{
				total += (x / rate);
				break;
			}



		}


		index++;
		//setprecision(6);
		op << "Case #" << index << ": "<<total << endl;
		
	}

}