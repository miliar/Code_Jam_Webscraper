#include <iostream>
#include <vector>
using namespace std;

long long gcd(long long a, long long b)
{
	if(a == 0)
		return b;
	else
		return gcd(b%a, a);
}

int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		long long P, Q;
		char _;
		cin >> P >> _ >> Q;

		long long c = gcd(P,Q);
		P /= c;
		Q /= c;

		cout << "Case #" << t << ": ";
		if(__builtin_popcountll(Q) != 1)
			cout << "impossible" << endl;
		else
		{
			P *= (2LL<<40)/(Q);

			cout << __builtin_clzll(P)-22 << endl;
		}
	}
}
