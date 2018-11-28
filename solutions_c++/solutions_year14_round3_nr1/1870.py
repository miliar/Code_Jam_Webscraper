#include <iostream>
#include <fstream>
//#include <stdint.h>
#include <string>
#include <cmath>
#include <climits>
#include <cstdio>
#include <algorithm>
#include <list>

using namespace std;

#define NOPOW 100

typedef long long ll;

ll pow2(ll n)
{
	for(ll i = 0; i < 42;i++)
	{
		if((1 << i) == n)
			return i;
	}
	return NOPOW;
}

ll maxPow2(ll n)
{
	ll i;
	for(i = 41L; (i >= 0L) && ((1L << i) & n) == 0; i--);
	return i;
}

ll gcd(ll a, ll b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}

int main(int argc, char* argv[])
{
	int t;
	char c;
	ll p, q, gcdPQ, qp, pp;
	cin >> t;
	for (int ti = 1; ti <= t; ti++)
	{
		cin >> p >> c >> q;
		gcdPQ = gcd(p, q);
		p = p/gcdPQ;
		q = q/gcdPQ;
		// cout << "p = " << p << "\n";
		// cout << "q = " << q << "\n";

		qp = pow2(q);
		// cout << "qp = " << qp << "\n";
		pp = maxPow2(p);
		// cout << "pp = " << pp << "\n";
		
		cout << "Case #" << ti << ": ";
		if(qp == NOPOW)
		{
			cout << "impossible\n";
		}
		else
		{
			cout << qp-pp << "\n";
		}
	}
	
	return 0;
}