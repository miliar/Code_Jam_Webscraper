#include <iostream>
#include <iomanip>

using namespace std;

double solve(double C, double F, double X)
{
	double result = ( (C/2) + (X/(2+F)) );
	double currentSpeed = 2;
	double time;
	double min = X/2;
	double current = 0;
	
	while (result < min)
	{
		time = (C/currentSpeed); 
		current += time;
		currentSpeed += F;
		result = (current + ((C/currentSpeed)) + (X/(currentSpeed+F) ) );
		min = (current + (X/currentSpeed));	 	
	}
	
	return min;
}

int main()
{
	unsigned int i;
	unsigned int T;
	double C;
	double F;
	double X;
	cin >> T;
	std::cout << std::setprecision(7) << std::fixed;
	for (i = 1; i <= T; i++)
	{
		cin >> C >> F >> X;
		cout << "Case #" << i << ": " << solve(C,F,X) << endl;	
	}
	return 0;
}
