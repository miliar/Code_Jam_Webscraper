#include <iostream>
#include<string.h>
using namespace std;

unsigned long long pow_my[][16] = { { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 },
{ 1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907 },
{ 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824 },
{ 1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625, 1220703125, 6103515625, 30517578125 },
{ 1, 6, 36, 216, 1296, 7776, 46656, 279936, 1679616, 10077696, 60466176, 362797056, 2176782336, 13060694016, 78364164096, 470184984576 },
{ 1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, 282475249, 1977326743, 13841287201, 96889010407, 678223072849, 4747561509943 },
{ 1, 8, 64, 512, 4096, 32768, 262144, 2097152, 16777216, 134217728, 1073741824, 8589934592, 68719476736, 549755813888, 4398046511104, 35184372088832 },
{ 1, 9, 81, 729, 6561, 59049, 531441, 4782969, 43046721, 387420489, 3486784401, 31381059609, 282429536481, 2541865828329, 22876792454961, 205891132094649 },
{ 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000, 1000000000000, 10000000000000, 100000000000000, 1000000000000000 }
};

unsigned long long basex(int num, int base)
{
	unsigned long long ret = 0;
	int count = 1;
	while (num)
	{
		if (num & 1)
		{
			ret += pow_my[base-2][count];			
		}
		count++;
		num >>= 1;
	}

	return ret;
}
bool isPrime(unsigned long long number,unsigned long long &div){

	if (number < 2) return false;
	if (number == 2) return true;
	if (number % 2 == 0)
	{
		div = 2;
		return false;
	}
	for (int i = 3; (i*i) <= number; i += 2)
	{
		if (number % i == 0)
		{
			div = i;
			return false;
		}
	}
	return true;
}


int main()
{	
	unsigned long long div;
	
	int T;
	cin >> T;

	unsigned  long long bases[11];
	for (int t = 1; t <= T; t++)
	{
		int N, J;
		cin >> N >> J;
		memset(bases, 0, sizeof(bases));

		for (unsigned short b = 2; b <= 10; b++)
		{
			bases[b] = 1 + pow_my[b - 2][N - 1];
		}

		int max = pow_my[0][N - 2] - 1;  // (N-2)*(N-1)/2;

		unsigned int n1 = 0; int j_temp = 0;
		cout << "Case #" << t << ":" << endl;
		for (; n1 <=max; n1++)
		{
			unsigned int divs[11];

			bool bsuccess = false;
			for (unsigned short b = 2; b <= 10; b++)
			{
				unsigned long long new_value = bases[b] + basex(n1,b);
				unsigned long long div = 0;
				
				if (isPrime(new_value,div)) // is a prime combination 
				{
					break;
				}
				else
				{
					divs[b] = div;
				}
				
				if (b == 10)
				{
					bsuccess = true;
					break;
				}
			}
			
			if (bsuccess)
			{				
				cout << "1";
				int max1 = pow_my[0][N - 3];
				while (max1)
				{
					if (max1&n1) cout << "1"; else cout << "0";
					max1 >>= 1;
				}
				cout << "1 ";
				for (unsigned short b = 2; b <= 10; b++)
				{
					cout << divs[b] << " ";
				}
				cout << endl;
				j_temp++;
				if (j_temp >= J) break;
			}
			
		}
	}
	
	return 0;
}
