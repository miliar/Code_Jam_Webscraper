/*
 *	Compiled and tested with GCC/G++ 4.8.2 on Linux x86_64,
 *	using redirection for input - output:
 *		program < inputfile > outputfile
 */

#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	double C, F, X;
	double result, new_result;
	double partial_sum, new_part;

	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cin >> C >> F >> X;
		// C is the price of a farm
		// F is the production rate (per second) of a farm
		// X is the target amount of cookies
		// the initial production rate is 2 cookies per second 

		// if N farms are bought, the optimal time is:
		// 		C/2 + C/(2+F) + ... + C/(2+(N-1)*F) + X/N
		// = 	Sum[ C/(2+n*F), n=0..N-1] + X/(2+N*F)

		// the problem can be solved by testing for N=0 upwards and and stop 
		// when the resulting time increases
		
		partial_sum = C/2;
	   	new_result = result = X/2; // current result, starting with N=0
		double A = X/C;
		int n = 1;
		while(new_result <= result)
		{
			result = new_result;
			new_part = C/(2+n*F);
			new_result = partial_sum + A*new_part; // Sum[...] + X/(2+N*F)
			partial_sum += new_part;
			n++;
		}
		cout << "Case #" << t << ": ";
		cout << result << setprecision(7) << fixed << endl;
	}
	return 0;
}
