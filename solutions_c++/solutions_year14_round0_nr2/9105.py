#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include "fstream"

using namespace std;

ifstream fin("B-small-attempt1.in");



int main()
{
	FILE *file;
	file = fopen("B-small-attempt1.out", "w");
	int t;
	double c, f, x, y;
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fin >> c >> f >> x;		
		y = 0;
		double total = 0;
		double rate = 2;
		if ( c > x )
		{
			y = x / rate;
			fprintf(file, "Case #%d: %1.7f\n", i, y);
			continue;
		}
		while(true)
		{			
			double n = c / rate;			

			double withoutForm = x / rate ; //اگه فارم نخری بقیه اش چقدر طول میکشه؟
			double withForm = x / (rate + f) + n;
			
			if (withForm < withoutForm)
			{
				y += n;
				rate += f;
			}
			else
			{
				y += withoutForm;
				break;
			}
		}
		fprintf(file, "Case #%d: %1.7f\n", i, y);
	}
	
	return 0;
}