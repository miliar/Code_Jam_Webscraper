#include <cmath>
#include <iostream>

using namespace std;

// TEST
// const int n = 6;
// const int j = 3;

// SMALL
const int n = 16;
const int j = 50;

// LARGE
// const int n = 32;
// const int j = 500;

int main() {
	unsigned long long coeffs[n][9];

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < 9; ++j)
		{
			coeffs[i][j] = pow(j+2,i);
			// cout << i << " " << j << " " << coeffs[i][j] << endl;
		}
	}

	cout << "Case #1:" << endl;

	int count = 0;
	int total_count = 1;

	bitset<n> b = bitset<n>(pow(2,n-1)+1);

	while (count < j) {
		unsigned long long factors[9] = {0,0,0,0,0,0,0,0,0}; 
		unsigned long long nums[9] = {0,0,0,0,0,0,0,0,0}; 
		int fc = 0;
		for (int i = 0; i < 9; ++i)
		{
			unsigned long long num = 0;
			for (int j = 0; j < n; ++j)
			{
				num += b[j] * coeffs[j][i];
			}
			nums[i] = num;
			for (int j = 2; j < sqrt(num); ++j)
			{
				if (num % j == 0) {
					factors[i] = j;
					fc++;
					break;
				}
			}
		}
		if (fc == 9) {
			cout << b << " ";
			for (int i = 0; i < 9; ++i)
			{
				cout << factors[i] << " ";	
			}
			cout << endl;
			count++;
			// for (int i = 0; i < 9; ++i)
			// {
			// 	cout << i+2 << ": " << nums[i] << " " << nums[i] % factors[i] << " " << nums[i] / factors[i] << endl;
			// }
		}
		// cout << total_count << '\r';
		b = bitset<n>(b.to_ulong()+2);
		total_count++;
	}

	return 0;
}