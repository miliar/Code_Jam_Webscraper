#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;

bool is_palin(const unsigned long long & n)
{
	char cs[30];
	unsigned length = sprintf(cs, "%lld", n);
	unsigned half = length/2;
	for(unsigned i = 0, j = 1; i < half; ++i, ++j)
	{
		if(cs[i] != cs[length - j]) return false;
	} 
	return true;
}

unsigned fsq(const unsigned long long & A, const unsigned long long & B)
{
	unsigned count = 0; 
	unsigned long long sB = static_cast<unsigned long long >(ceil(sqrt(B)));
	unsigned long long m = 0;
	for(unsigned i = 1; i <= sB; ++i)
	{
		m = i * i;
		if(m >= A)
		{
			if(m > B) return count;
			if(is_palin(i) && is_palin(m))
			{
				++count;
			}

		}		
	}
	return count;
}


void outp(const unsigned long long & A, const unsigned long long & B ,const unsigned & i)
{
	unsigned n = fsq(A, B);
	cout << "Case #" << i << ": " << n;
}



int main()
{
	unsigned T;
	unsigned long long A, B;
	cin >> T;
	unsigned ntl = T-1;
	for(unsigned i = 0; i < T; ++i)
	{
		cin >> A >> B;
		outp(A, B, i+1);
		if(i < ntl) cout << endl;
	}
	return 0;
}
