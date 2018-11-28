// Problem B. Cookie Clicker Alpha
// Qualification Round 2014
// George Vafiadis

#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

double solve(double C, double F, double X);

bool isApproxEqual(double x, double y, double epsilon = 1e-6)
{
	double d = x - y; 

	if( (-epsilon <= d) && (d <= epsilon) )
	{
    	return true;
    }

    if(  (-epsilon <= x && x <= epsilon) && (-epsilon <= y && y <= epsilon) )
    {
    	return false;
    }

    double fx = (x - y) / x;
    double fy = (x - y) / y;

    return (-epsilon <= fx && fx <= epsilon) || 
    	   (-epsilon <= fy && fy <= epsilon);
}

int main(int argc, char* argv[])
{
	int T;

	cin >> T;

	for(int ti = 1; ti <= T; ++ti)
	{
		double C, F, X;

		cin >> C >> F >> X;

		cout << "Case #" << ti << ": " 
			 << std::fixed 
			 << std::setprecision(7) << solve(C, F, X) << endl;
	}

	return 0;
}

double solve(double C, double F, double X)
{
	double t = 0.0;
	double cps = 2.0;
	double cookies = 0.0;

	while( !isApproxEqual(cookies, X) )
	{
		double remaining = fabs(X - cookies);
		double remainingTime = 	remaining / cps;
		double tNextFarm = C / cps;

		if( remainingTime <= tNextFarm + X / (cps + F) )
		{
			t += remainingTime;
			cookies += remainingTime * cps;
			break;
		}

		cps += F;
		cookies = 0.0;
		t += tNextFarm;
	}

	return t;
}




