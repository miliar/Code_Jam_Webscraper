// #include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef long long S64;

bool isPalindrome(S64 x)
{
	ostringstream oss;
	oss << x;
	const string s = oss.str();
	for (size_t i = 0; i < s.size() / 2; ++i)
	{
		if (s[i] != s[s.size() - i - 1])
			return false;
	}
	return true;
}

bool isFairSquareRoot(S64 r)
{
	if (!isPalindrome(r))
		return false;
	S64 x = r*r;
	if (!isPalindrome(x))
		return false;
	return true;
}

S64 makeX1(S64 i)
{
	int n = 0;
	S64 x = i;
	while (i > 0)
	{
		++n;
		x *= 10;
		x += i % 10;
		i /= 10;
	}
	return x;
}
S64 makeX2(S64 i)
{
	int n = 0;
	S64 x = i;
	i /= 10; // Don't double up the center digit
	while (i > 0)
	{
		++n;
		x *= 10;
		x += i % 10;
		i /= 10;
	}
	return x;
}

int main()
{
	vector<S64> v;
	for (S64 i = 1; i <= 10000; ++i)
	{
		{
			const S64 x = makeX1(i);
			if (isFairSquareRoot(x))
			{
				v.push_back(x*x);
				// cerr << i << '\t' << x << '\t' << x * x << endl;
			}
		}
		{
			const S64 x = makeX2(i);
			if (isFairSquareRoot(x))
			{
				v.push_back(x*x);
				// cerr << i << '\t' << x << '\t' << x * x << endl;
			}
		}
	}
	/*
	sort(v.begin(), v.end());
	for (size_t i = 0; i < v.size(); ++i)
		cerr << v[i] << endl;
	*/

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		S64 a, b;
		cin >> a >> b;
		int ret = 0;
		for (auto it = v.begin(); it != v.end(); ++it)
		{
			if (*it >= a && *it <= b)
				++ret;
		}
		cout << "Case #" << (t+1) << ": " << ret << endl;
	}
	return 0;
}
