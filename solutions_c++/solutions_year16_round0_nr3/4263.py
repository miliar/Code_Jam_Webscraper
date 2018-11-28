#include <string>
#include <iostream>
#include <math.h>

using namespace std;


int main()
{
	int success = 0;
	bool number[16];
	
	number[0] = 1;
	number[15] = 1;
	long long results[9];
	long long divisors[9];
	int iteration = 0;
	int iteration_helper;
	bool is_prime = 0;
	
	
	
	
	cout << "Case #1: " << endl;

	while (success < 50)
	{
		int i = 1;
		while (i<15)
		{
			number[i] = 0;
			i++;
		}
		
		iteration_helper = iteration;
		int j = 14;
		while (iteration_helper > 0)
		{
			number[j] = iteration_helper % 2;
			iteration_helper = iteration_helper / 2;
			j--;
		}


		int b = 2;
		while (b < 11)
		{
			long long summe = 0;
			int i = 0;
			while (i < 16)
				{
					summe += number[i] * pow(b, 15 - i);
					i++;
				}

			 is_prime = 1;
			int upper_bound = sqrt(summe);
			int teiler = 2;
				while (teiler <= upper_bound)
				{
					if (summe%teiler == 0)
					{
						divisors[b - 2] = teiler;
						is_prime = 0;
						break;
					}

					teiler++;
				}
				if (is_prime) break;

			


			b++;
		}
		if (!is_prime)
		{
			int k = 0;
			while (k < 16)
			{
				cout << number[k];
				k++;
			}

			int l = 0;
			while (l < 9)
			{
				cout <<" "<< divisors[l];
				l++;
			}
			cout << endl;
			success++;
		}
		

		iteration++;
	}
	
	return 0;
}