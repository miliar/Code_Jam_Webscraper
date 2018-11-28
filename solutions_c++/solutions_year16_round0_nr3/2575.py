#include <vector>
#include <gmp.h>
#include <gmpxx.h>
#include <iostream>

using namespace std;

typedef unsigned long long int ui;
typedef mpz_class LL;


const int N = 32;
const int J = 500;
//const LL BOUND("1000000", 2);
//const LL BOUND("10000000000000000", 2);
const LL BOUND("100000000000000000000000000000000", 2);
const LL PBOUND("10000000", 10);



/*
 * Miller-Rabin primality test, iteration signifies the accuracy
 */
LL mulmod(LL a, LL b, LL mod)
{
	LL x = 0,y = a % mod;
	while (b > 0)
	{
		if (b % 2 == 1)
			x = (x + y) % mod;
		y = (y * 2) % mod;
		b /= 2;
	}
	return x % mod;
}

LL modulo(LL base, LL exponent, LL mod)
{
	LL x = 1;
	LL y = base;
	while (exponent > 0)
	{
		if (exponent % 2 == 1)
			x = (x * y) % mod;
		y = (y * y) % mod;
		exponent = exponent / 2;
	}
	return x % mod;
}

bool Miller(LL p, int iteration)
{
	if (p < 2)
		return false;
	if (p != 2 && p % 2 == 0)
		return false;

	LL s = p - 1;
	while (s % 2 == 0)
		s /= 2;

	for (int i = 0; i < iteration; i++)
	{
		LL a = rand() % (p - 1) + 1, temp = s;
		LL mod = modulo(a, temp, p);
		while (temp != p - 1 && mod != 1 && mod != p - 1)
		{
			mod = mulmod(mod, mod, p);
			temp *= 2;
		}
		if (mod != p - 1 && temp % 2 == 0)
			return false;
	}
	
	return true;
}


bool isPrime(LL x)
{
	return Miller(x, 15);
}



vector<LL> certificat;

// Test prime-proof
bool primeproof(LL x)
{
	certificat.clear();

	for(int b = 2; b <= 10; b++)
	{
		LL z = x;
		LL y = 0;
		LL c = 1;
		for(int i = 0; i < N; i++)
		{
			y += c*(z % 2);
			c *= b;
			z /= 2;
		}
		
		if(isPrime(y))
			return false;
		else
		{
			if((y % 2) == 0)
			{
				certificat.push_back(2);
				continue;
			}
		
			bool ok = true;
			for(LL i = 3; i <= PBOUND && ok; i += 2)
			{
				if((y % i) == 0)
				{
					certificat.push_back(i);
					ok = false;
				}
			}
			
			if(ok)
				return false;
		}
	}
	
	return true;
}





int main()
{	
	cout << "Case #1:" << endl;
	int k = 0;
	for(LL x = BOUND/2 + 1; x < BOUND; x += 2)
	{
			if(primeproof(x))
			{
			
				LL z = x;
				vector<int> dec;
				for(int i = 0; i < N; i++)
				{
					dec.push_back(((z % 2) == 0)? 0 : 1);
					z /= 2;
				}
				for(int i = 0; i < N; i++)
					cout << dec[N-i-1];
				
				for(int i = 0; i < 9; i++)
					cout << " " << certificat[i];
				cout << endl;
				k++;
			}
			
			if(k >= J)
				return 0;
	}

}
