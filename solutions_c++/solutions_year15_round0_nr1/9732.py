#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int shymax;
		cin >> shymax;
		int num;
		cin >> num;
		int shyarr[shymax + 1];
		for (int k = shymax; k >= 0; k--)
		{
			shyarr[k] = num % 10;
			num = num / 10;
		}
		int friends = 0;
		int sum = 0;
		for (int k = 0; k <= shymax; k++)
 		{
			if (sum >= k);
			else if (shyarr[k] != 0)
			{
				friends += (k - sum);
				sum += friends;
			}
			sum += shyarr[k];
			
		}

				
		cout << "Case #" << i+1 << ": " << friends << "\n";
	}
	return 0;
}

