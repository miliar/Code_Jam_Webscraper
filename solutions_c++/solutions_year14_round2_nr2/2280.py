#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <bitset>

using namespace std;

typedef unsigned long long num;
typedef long double flt;

int main ()
{
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int testCases;
	cin >> testCases;

	for (int testCase = 0; testCase < testCases; ++testCase)
	{
		cout << "Case #" << testCase+1 << ": ";

		num A,B,K;

		cin >> A;
		cin >> B;
		cin >> K;

	unsigned counter = 0;
	for (num a = 0; a<A; ++a)
	{
		for (num b = 0; b < B; ++b)
		{
			if ((a&b) < K) ++counter;
		}
	}

	cout << counter <<"\n";
}
cerr<<"done";
}