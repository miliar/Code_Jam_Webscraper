#include <string>
#include <cstring>
#include <iostream>
#include <fstream>

using namespace std;

const int M = 10000000;

long long lmax = ((long long)M) * ((long long)M);

int tc, n;
long long lst[1000];

bool is_palindrome(long long a)
{
	string alpha = to_string(a);

	int l = alpha.length();

	for (int i=0; i<=l/2; i++)
		if (alpha[i] != alpha[l-i-1])
			return false;
	
	return true;
}

void init()
{
	n = 0;
	long long sqr;
	for (long long i=1; sqr = i*i, sqr <= lmax; i++)
		if (is_palindrome(i) && is_palindrome(sqr))
			lst[n++] = sqr;
}

int solve(long long a, long long b)
{
	int cnt = 0;

	for (int i=0; i<n; i++)
		if (a <= lst[i] && lst[i] <= b)
			cnt++;

	return cnt;
}

int main()
{
	ifstream fin("fairandsquare.txt");
	ofstream fout("fairandsquare.out");

	init();

	fin >> tc;
	long long a, b;

	for (int test=1; test<=tc; test++) {
		fin >> a >> b;
		// output
		fout << "Case #" << test << ": " << solve(a, b) << endl;
	}

	return 0;
}