#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
#define MOD 1000000007
ull modPow(ull a, ull x, ull p) {
    //calculates a^x mod p in logarithmic time.
    ull res = 1;
    while(x > 0) {
        if( x % 2 != 0) {
            res = (res * a) % p;
        }
        a = (a * a) % p;
        x /= 2;
    }
    return res;
}
 
ull modInverse(ull a, ull p) {
    //calculates the modular multiplicative of a mod m.
    //(assuming p is prime).
    return modPow(a, p-2, p);
}
ull modBinomial(ull n, ull k, ull p) {
// calculates C(n,k) mod p (assuming p is prime).
 
    ull numerator = 1; // n * (n-1) * ... * (n-k+1)
    for (int i=0; i<k; i++) {
        numerator = (numerator * (n-i) ) % p;
    }
 
    ull denominator = 1; // k!
    for (int i=1; i<=k; i++) {
        denominator = (denominator * i) % p;
    }
 
    // numerator / denominator mod p.
    return ( numerator* modInverse(denominator,p) ) % p;
}
bool split(long long a, bool *arr)
{
	while (a)
	{
		arr[a%10] = 1;
		a /= 10;
	}
	for (int i = 0; i < 10; ++i)
	{
		if (arr[i] == 0)
			return 0;
	}
	return 1;
}
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin>>N;
		cout<<"Case #"<<t<<": ";
		if (N == 0)
		{
			cout<<"INSOMNIA\n";
		}
		else 
		{
			bool arr[10] = {0};
			int i;
			for (i = 1; ; ++i)
			{
				if (split((long long)N * i, arr))
				{
					break;
				}
			}
			cout<<N*i<<'\n';
		}
	}
}