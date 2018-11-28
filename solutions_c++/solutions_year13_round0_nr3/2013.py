#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

bool isPalindrome(long long n)
{
	long long t = n;
	long long c = 0;
	
	while( n > 0 )
	{
		c *= 10;
		c += n % 10;
		n /= 10;
	}
	
	return c == t;
}

using namespace std;

int main()
{
	freopen("C-large-1.in", "r", stdin);
	freopen("outputLargeC.txt", "w", stdout);
	
	vector<long long> V;
	long long top = 1e14;
	
	for(long long i = 1; i * i <= top; ++i)
		if( isPalindrome(i) && isPalindrome( i * i ) )
			V.push_back( i * i );
			
	int TC;
	cin >> TC;
	
	for(int j = 0; j < TC; ++j)
	{
		long long A, B;
		cin >> A >> B;

		int posB = upper_bound(V.begin(), V.end(), B) - V.begin();
		int posA = lower_bound(V.begin(), V.end(), A) - V.begin();
		
		cout << "Case #" << j + 1 << ": "  << posB-posA << endl;
	}
	
	return 0;
}
