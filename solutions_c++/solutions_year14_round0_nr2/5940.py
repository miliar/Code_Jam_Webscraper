#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

double CheckResult(double C, double F, double X)
{
	double rest = X - C;
	double speed = 2;
	double time_rest1;
	double time_rest2;
	double time_pass = C / 2;
	if (X < C)
	{
		return X / 2;
	}
	while (1)
	{
		time_rest1 = rest / speed;
		time_rest2 = X / (speed + F);
		if (time_rest1 <= time_rest2)
		{
			return time_pass + time_rest1;
		}
		else
		{
			speed += F;
			time_pass += C / speed;
		}
	}
}

int main(void)
{
	int case_num;
	double result;
	double C;
	double F;
	double X;
	ifstream input("B-large.in");
	ofstream output("ResultB_large.out");
	
	input >> case_num;
	input.get();
	for (int i = 0; i < case_num; i++)
	{
		input >> C;
		input >> F;
		input >> X;
		input.get();
		result = CheckResult(C, F, X);
		output.precision(7); 
		output << fixed;
		output << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}
