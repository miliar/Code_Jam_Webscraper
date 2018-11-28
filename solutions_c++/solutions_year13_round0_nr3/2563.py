#include <iostream>
#include <sstream>

#include <algorithm>
#include <vector>

using namespace std;

#define ALL(c) (c).begin(), (c).end()

const long long
	MAXSQR = 10000000LL;

vector< long long > nums;

bool isPalindrome(long long n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	string t = s;
	reverse(ALL(s));
	return s == t;
}

void precalc()
{
	for (long long n = 1; n <= MAXSQR; ++n)
	{
		if (isPalindrome(n))
		{
			long long n2 = n * n;
			if (isPalindrome(n2))
				nums.push_back(n2);
		}
	}
}

int main()
{
	precalc();

	int testCount;
	cin >> testCount;

	for (int test = 1; test <= testCount; ++test)
	{
		long long A, B;
		cin >> A >> B;

		int answer = upper_bound(ALL(nums), B) - lower_bound(ALL(nums), A);

		cout << "Case #" << test  << ": " << answer << endl;
	}

	return 0;
}
