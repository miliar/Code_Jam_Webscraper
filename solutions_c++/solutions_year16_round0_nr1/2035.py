#include <bits/stdc++.h>

using namespace std;

ifstream fin("A.in");
ofstream fout("output.out");

// #define fin cin
// #define fout cout

set<int> digits;

void GetDigits(long long int x)
{
	while (x > 0)
	{
		digits.insert(x % 10);
		x /= 10;
	}
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	fin >> t;
	int u = 0;
	while (u++ < t)
	{
		digits.clear();
		long long int n;
		long long int x = 0;
		fin >> n;
		if (n == 0) x = -1;
		else
		{
			while (digits.size() < 10)
			{
				x += n;
				GetDigits(x);
			}
		}
		fout << "Case #" << u << ": ";
		if (x == -1) fout << "INSOMNIA" << endl;
		else fout << x << endl;
	}
	return 0;
}