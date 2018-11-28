#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int nrOfCases;
	cin >> nrOfCases;
	for (int i = 1; i <= nrOfCases; ++i)
	{
		long long r, t;
		cin >> r >> t;
		
		long long n = 0;
		while (2 * r * n - n + 2 * n * n <= t)
		{
			++n;
		}
		cout << "Case #" << i << ": " << (n - 1) << endl;
	}
}
