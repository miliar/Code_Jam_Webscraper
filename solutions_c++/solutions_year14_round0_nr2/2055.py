#include <iostream>
#include <iomanip>

using namespace std;

double calc(double r, double C, double F, double X)
{
	if (C >= X || (C/r + X/(r+F)) >= X/r)
        	return X/r;
    	else
        	return C/r + calc(r+F, C,F,X);

}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		double C,F,X;
		cin >> C >> F >> X;
		cout << "Case #" << (i+1) << ": " << fixed << setprecision(7) << calc(2.0, C,F,X) << endl;
	}
	return 0;
}
