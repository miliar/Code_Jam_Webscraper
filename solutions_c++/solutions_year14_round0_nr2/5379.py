#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

double solve(long double c, long double f, long double x)
{
	long double d = 0;
	long double ans = x/2;

	for (int i = 1; i <= x; i++)
	{
		d += c / (2 + (i - 1)*f);
		ans = min(ans, d + x / (2 + i*f));
	}

	return ans;
}

int main(int argc, char* argv[])
{
	FILE* fin = NULL;
	FILE* fout = NULL; 

	fin = freopen("input.txt", "r", stdin);
	fout = freopen("output.txt", "w", stdout);

	cout.precision(16);

	int T; cin >> T;
	for (int test = 1 ; test<= T; test++)
	{
		long double c, f, x;
		cin >> c >> f >> x;

		printf("Case #%d: ", test);
		cout << solve(c, f, x) << endl;
	}

	if (fin) fclose(fin);
	if (fout) fclose(fout);

	return 0;
}

