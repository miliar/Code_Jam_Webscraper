#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int tc;	// number of test cases
	int cc=1;	// current case
	long double c, f, x;
	long double cpc;	// cookies per second
	long double sum;	// cumulative sum
	long double result, nresult;

	cin >> tc;
	cout << fixed << setprecision(7);

	while(tc--)
	{
		cin >> c;
		cin >> f;
		cin >> x;
		cpc = 2.0;
		sum = 0.0;
		nresult = x / cpc;

		cout << "Case #" << cc++ << ": ";
		do
		{
			result = nresult;
			sum += (c / cpc);
			cpc += f;
			nresult = sum + (x / cpc);
		}while(result > nresult);
		cout << result << endl;
	}
	return 0;
}
