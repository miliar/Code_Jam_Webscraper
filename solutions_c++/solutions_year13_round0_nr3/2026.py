// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

bool IsPalindrome(long long n)
{
	long long temp = n;
	long long invn = 0;
	while (temp)
	{
		invn = 10 * invn + temp % 10;
		temp /= 10;
	}
	if (n == invn)
		return true;
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifstr("C-large-1.in");
	ofstream ofstr("C-large-1.out");

	vector<long long> sqpalis;
	for (long long n = 1; n < 10000000; ++n)
	{
		if (IsPalindrome(n) && IsPalindrome(n * n))
			sqpalis.push_back(n * n);
	}

	int T;
	ifstr >> T;
	for (int t = 0; t < T; ++t)
	{
		long long A, B;
		ifstr >> A >> B;
		int count = upper_bound(sqpalis.begin(), sqpalis.end(), B) - lower_bound(sqpalis.begin(), sqpalis.end(), A);
		ofstr << "Case #" << t + 1 << ": " << count << endl;
	}

	return 0;
}

