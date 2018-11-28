#include <iostream>
#include <fstream>

using namespace std;

int isPrime(long long n)
{
	if(n == 1)
		return -1;
	
	for(long long i = 2; i*i<=n; i++)
	{
		if(n%i == 0)
			return i;
	}
	return -1;
}

long long getD(long long n)
{
	for(long long i = 2; i < n; i++)
	{
		if(n%i == 0)
			return i;
	}
	return -1;
}

int main()
{
	long long max = 16383;
	
	ifstream read;
	read.open("C-small-attempt0.in");

	ofstream write;
	write.open("output.txt");

	int T;
	read >> T;
	
	for(int i = 0; i < T; i++)
	{
		write << "Case #" <<i+1 <<":" <<endl;
		int N, J;

		read >> N >> J;
		long long shifter = 0;
		int counter = 0;
		long long value;
		long long divisors[11];
		int binaries[16];
		while(counter < J )
		{
			value = (shifter << 1) | 0x8001;
			for (int l = 0; l < 16; l++)
			{
				int x = (value >> l);
				x = x%2;
				binaries[l] = x;
			}

			for(int b = 2; b <= 10; b++)
			{
				//compute value;
				long long value_base = 0;
				for(int j = 0; j < 16; j++)
				{
					int y = binaries[15 - j];
					value_base = value_base*b + y;
				}

				//check if prime
				long long div = isPrime(value_base);
				if(div != -1)
				{
					divisors[b] = div;
				}
				else break;
				
				if(b == 10)
				{
					//write first the binary
					for(int k = 0; k < 16 ; k++)
					{
						write << binaries[15 - k];
					}
					write << " ";
					for(int k = 2; k <=10; k++)  
					{
						write << divisors[k] << " ";
					}
					counter++;
					write << endl;
				}
			}
			shifter++;
		}

	}
	return 0;
}