#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
using namespace std;

int main(int argc, char const *argv[])
{
	int num;
	cin >> num;

	for (int i = 0; i < num; ++i)
	{
		int low;
		cin >> low;
		int sqrt_low = sqrt(low);
		int temp_low = sqrt_low+1;
		if (temp_low * temp_low <= low){
			sqrt_low++;
		}
		int hi;
		cin >> hi;
		int sqrt_hi = sqrt(hi);
		int temp_hi = sqrt_hi+1;

		int rtval = 0;
		for (int j = sqrt_low; j <= sqrt_hi; ++j)
		{
			if (j*j < low)
			{
				continue;
			}
			// Compute palindrome on j
			int rev = 0;
			int temp = j; // Copy of j
			while (temp > 0){
				int dig = temp % 10;
				rev = rev * 10 + dig;
				temp = temp / 10;
			}
			if (j == rev)
			{
				int rev_sq = 0;
				int temp_sq = j*j; // Copy of j
				while (temp_sq > 0){
					int dig = temp_sq % 10;
					rev_sq = rev_sq * 10 + dig;
					temp_sq = temp_sq / 10;
				}
				if ((j*j) == rev_sq)
				{
					rtval ++;
				}
			}
		}
		printf("Case #%d: %d\n", i+1, rtval);
	}
	return 0;
}