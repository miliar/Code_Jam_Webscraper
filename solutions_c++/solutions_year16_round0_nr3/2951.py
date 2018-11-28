#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

unsigned long long interpretation(unsigned long long x, unsigned int base)
{
	int cnt = 0;
	unsigned long long retval = 0;
	while (x)
	{
			retval = pow(base,cnt)*(x&0x01)+retval;
			cnt++;
			x = x >> 1;
	}
	return retval;
}

bool isprime(unsigned long long x,unsigned long long & divisor)
{
	if (x < 2)
		return false;
	
	if (x == 2)
		return true;
	
	if((x & 0x1) == 0) {
		divisor = 2;
		return false;
	}
	
	for(unsigned long long i = 3; i <= sqrt(x); i += 2)
	{
		if((x % i) == 0) {
			divisor = i;
			return false;
		}
	}
	return true;
}

void print (unsigned int x)
{
	if (x != 0) {
		print (x >> 1);
		if (x & 0x1 == 1)
			cout << 1;
		else
			cout << 0;
	}
}

int main()
{
	
		int cases;
		unsigned int J, N;
		unsigned long long  val = 1;
		unsigned long long divisor[11] ;
		bool stay ;
		cin >> cases;
		//cout << interpretation(4294967295, 3);
			//cout << x << " " << isprime(x, K) << endl;
		for (int x = 1; x <= cases; x++)
		{
			cout << "Case #" << x << ":" << endl;
			cin >> N >> J;
			val = 1;
			val = val << (N-1);
			val = val | 0x1;
			//val = 9;
			for (int temp = 1; temp <= J; temp++) 
			{
				stay = true;
				while (stay) 
				{
					if (!isprime(interpretation(val, 2),divisor[2]) && 
						!isprime(interpretation(val, 3),divisor[3]) && 
						!isprime(interpretation(val, 4),divisor[4]) && 
						!isprime(interpretation(val, 5),divisor[5]) &&
						!isprime(interpretation(val, 6),divisor[6]) &&
						!isprime(interpretation(val, 7),divisor[7]) &&
						!isprime(interpretation(val, 8),divisor[8]) &&
						!isprime(interpretation(val, 9),divisor[9]) &&
						!isprime(interpretation(val, 10),divisor[10])) 
						{
							print (val);
							for (int temp = 2 ; temp < 11; temp++)
							{
								//cout << " temp " << temp << " " << divisor[temp] << " " << interpretation(val, temp);
								cout <<  " " << divisor[temp];
							}
							cout << endl;
							stay = false;
						}
						val = val + 2;
					}
			}
		}
		return 0;
}

