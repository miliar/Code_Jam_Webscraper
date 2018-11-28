#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

typedef long long ll;

class Interpreter
{
public:
	Interpreter()
	{
		for (int i = 0; i < 9; ++i)
		{
			interpretations[i] = divisors[i] = 0;
		}
	}

	void reset()
	{
		rep.clear();
		for (int i = 0; i < 9; ++i)
		{
			interpretations[i] = divisors[i] = 0;
		}
	}

	bool init(ll n, int w)
	{
		reset();
		num = n;
		ll i = 1;
		int shift = 0;
		bool keepChecking = true;
		while (shift < w && keepChecking)
		{
			int bit = n & (i << shift);
			if (bit)  
				rep.append("1"); 
			else 
				rep.append("0");

			if (bit)
			{
				for (int i = 0; i < 9; ++i)
				{
					interpretations[i] =  pow(i + 2, shift) + interpretations[i];
				}
			}

			shift++;
		}

		int pass = 0;
		for (int i = 0; i < 9; ++i)
		{
			ll factor;
			if (prime(interpretations[i], factor) == true)
			{
				keepChecking = false;
				return false;
			}
			else
			{
				divisors[i] = factor;
				pass++;
			}
		}

		if (pass == 9)
		{
			// this case is valid.
			reverse(rep.begin(), rep.end());
			return true;
		}
		else
		{
			return false;
		}
	}

	bool prime(ll num, ll& factor)
	{
		ll limit = pow(num, 0.5) + 1;
		for (ll i = 2; i < limit; ++i)
		{
			if (num % i == 0)
			{
				factor = i;
				return false;
			}
		}

		return true;
	}


	ll interpretations[9];
	
	ll divisors[9];
	ll num;
	string rep;
};

int main(void)
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		int n, j;

		cin >> n >> j;

		ll start = (1 << (n - 1)) + 1;
		Interpreter ip;
		
		cout << "Case #" << i + 1 << ":" << endl;
		while (j)
		{
			if (ip.init(start, n))
			{
				j--;
				cout << ip.rep;
				for (int idx = 0; idx < 9; idx++)
				{
					cout << " " << ip.divisors[idx];
				}
				cout << endl;
			}
			start += 2;
		}
		
	}
	return 0;
}
