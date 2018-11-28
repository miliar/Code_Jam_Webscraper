#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;


bool IsPalin(long long x)
{
	stringstream ss;
	ss << x;
	string s = ss.str();

	int len = s.size();
	for (int i=0; i<len/2; i++)
	{
		if (s[i] != s[len-i-1])
			return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);

	int T;
	cin >> T;
	for (int t=0; t<T; t++)
	{
		long long A, B;
		cin >> A >> B;
		long long ra, rb;
		ra = sqrt(A);
		rb = sqrt(B);

		long long count = 0;
		for (long long r = ra-1; r<rb+1; r++)
		{
			if (!IsPalin(r))
				continue;
			long long sr = r * r;
			if (sr >= A && sr <= B && IsPalin(sr))
				count ++;
		}
		cout << "Case #" << t+1 << ": " << count << endl;
	}

	return 0;
}
			
