#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <bitset>

typedef unsigned long long int ull;

#define N_MAX 1000005

int composite[N_MAX]={0};

void init_prime ()
{
    // For every number k from 2 to sqrt(N)
    for (int k=2; k<=sqrt(N_MAX); k++)
    {
        // If k is not marked as composite
        if (composite[k]==0)
        {
            // Mark every number km where m >= k and km < N as composite
            for (int m=k; k*m<=N_MAX; m++)
            {
                composite[k*m]=1;
            }
        }
    }
}

vector<int> prime_vec;

void init_prime_vec ()
{
	prime_vec.push_back (2);
	for (int i=3; i<N_MAX; i+=2)
	{
		if (!composite[i])
		{
			prime_vec.push_back(i);
		}
	}
}

ull base_value (string s, int base)
{
	reverse (s.begin(), s.end());
	ull sum=0;
	ull multiplier=1;
	for (int i=0; i<s.length(); i++)
	{
		if (s[i]=='1')
			sum+=multiplier;
		multiplier*=base;
	}
	return sum;
}

int main() {
	
	int t;
	cin >> t;
	
	for (int i=0; i<t; i++)
	{
		int n,j;
		cin >> n >> j;
		printf ("Case #%d:\n", i+1);
	}
	
	init_prime();
	init_prime_vec ();
	//for (int i=33; i<=63; i+=2)
	int count=0;
	for (int i=32769; i<=65535; i+=2)
	{
		bitset<16> binary=i;
		string binary_string = binary.to_string();
		bool is_jamcoin=true;
		for (int j=2; j<=10; j++)
		{
			ull bv = base_value(binary_string,j);
			if ((bv<=N_MAX) && (composite[bv]==0))
			{
				is_jamcoin=false;
				break;
			}
			else
			{
				bool found=false;
				for (int k=0; prime_vec[k]<prime_vec.size(); k++)
				{
					if (bv%prime_vec[k]==0)
					{
						found=true;
						break;
					}
				}
				if (!found)
				{
					is_jamcoin=false;
					break;
				}
			}
		}
		if (is_jamcoin)
		{
			count++;
			cout << binary;
			for (int j=2; j<=10; j++)
			{
				ull bv = base_value(binary_string,j);
				for (int k=0; prime_vec[k]<bv; k++)
				{
					if (bv%prime_vec[k]==0)
					{
						printf (" %d",prime_vec[k]);
						break;
					}
				}
			}
			cout << endl;
			if (count==50)
				break;
		}
	}
}
