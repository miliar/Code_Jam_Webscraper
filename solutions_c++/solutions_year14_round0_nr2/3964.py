#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <algorithm>

using namespace std;

void solve(double a, double b, double c, double* x1, double* x2)
{
	double D = b*b - 4 * a*c;
	if (D >= 0)
	{
		*x1 = (-b - sqrt(D)) / (2 * a);
		*x2 = (-b + sqrt(D)) / (2 * a);
	}
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");


	unsigned long T;
	input >> T;
	//	cout << "T = "<<T << endl;

	long double time,C,F,X,sp;
//	unsigned temp, numb, ans;
	output << setprecision(9);
	for (unsigned t = 0; t<T; ++t)
	{
		time = 0;
		sp = 2;
		input >> C>>F>>X;
		
		//while (1)
		//{
		//	if ((X / sp)>(C/sp + X / (sp + F)))
		//	{
		//		time += (C / sp);
		//		sp += F;
		//	}
		//	else
		//	{
		//		time += (X / sp);
		//		break;
		//	}
		//}

		int n;
/*		double x1, x2;
		solve((F*F* (1 - (1 - C / X)*(1 - C / X))), (F* (4 - 2 * F - 4 * (1 - C / X)*(1 - C / X))), 
			(F - 2)*(F - 2) - 4 * (1 - C / X)*(1 - C / X),   &x1, &x2);
		if (x1 > 0)
		{
			n = (int)x1;
		}
		else if (x2 > 0)
		{
			n = (int)x2;
		}
		else
		{
			n = 0;
		}*/
//		n++;

		n = (int)(X / C - 2.0 / F);
		for (int i = 0; i < n ; i++)
		{
			time += (C / (2 + i*F));
		}
		time += (X / (2 + max(n,0)*F));

		output << "Case #" << t + 1 << ": "<<time;
		
		output << "\n";

	}




	input.close();
	output.close();
	//	system("pause");
	return 0;
}
