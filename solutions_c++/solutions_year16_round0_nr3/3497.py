
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
//official solution

using namespace std;

ifstream fin("..//C-small-attempt0.in");
ofstream fout("..//C-small-attempt0.out");

int T;
int S;
long long fist_result;
long long result_list[11] = { 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000 };



long long Isprime(long long a)
{
	for (long long i = 2; i*i <= a; i += 1)
	if (!(a%i))return i;
	return 0;
}

int main()
{
	fin >> T;
	
	for (int i = 1; i <= T; i++)
	{
		fout << "Case #" << i << ":" << endl;
		int result_count = 0;
		int N, J;
		fin >> N >> J;
		for (long long j = 0; j < pow(2, N - 2); j++)
		{
			bool prim_flag = 0;
			long long bin_value = pow(2, N-1) + j*2 + 1;
//			if (Isprime(bin_value)) continue;
			for (int base = 2; base <= 10; base++)
			{ 
				int bin_value2 = bin_value;
				long long value=0;
				for (int k = 0; k < N; k++)
				{
					value = value + (bin_value2 % 2)*pow(base,k);
					bin_value2 = bin_value2 / 2;
				}
				long long now_base_divide_value;
				now_base_divide_value = Isprime(value);
//				if (result_list[base]>now_base_divide_value)
//				{
					result_list[base] = now_base_divide_value;
//				}
				if (!now_base_divide_value)
				{
					prim_flag = 1;
					break;
				}
				if (base == 10)
				{
					fist_result = value;
				}
			}
			if (!prim_flag)
			{
				fout << fist_result;
				for (int q = 2; q <= 10; q++)
				{
					fout << " " << result_list[q];
				}
				fout << endl;
				result_count++;
			}
			if (result_count == J)
				break;
		}

		
		
	}
	

	return 0;
}




