#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <time.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> getDigits(long long n)
{
	if (n == 0) return { 0 };
	vector<int> digits;
	while (n)
	{
		digits.push_back(n % 10);
		n /= 10;
	}
	return digits;
}

string solve(int n)
{
	return "ololo";
}

long long brute_solve(int n)
{
	if (n == 0) return -1;

	set<int> seen;
	long long i;
	for (i = 1; seen.size() < 10; ++i)
	{
		for (int digit : getDigits(i * n))
		{
			seen.insert(digit);
		}

		if (i > 1e2)
		{
			cerr << "Warning!!! " << i << '*' << n << endl;
		}
	}
	return (i - 1) * n;
}

void test()
{
	cout << brute_solve(1) << endl;
	return;

	long long max_value = 0;
	double max_time = 0;
	for (int n = 0; n <= 1000000; ++n)
	{
		double start = clock();
		long long answer = brute_solve(n);
		double finish = clock();

		double duration = (finish - start) / CLOCKS_PER_SEC;

		if (duration > max_time)
		{
			max_time = duration;
			cout << n << ": " << answer << endl;
			cout << "Time is " << max_time << "sec" << endl;
		}

		if (answer < 0) 
			cout << n << ": " << answer << endl;
		max_value = max(max_value, answer);
	}
	cout << "Max value: " << max_value << endl;
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	// test();
	// return 1;

	int T; 
	cin >> T;
	double global_start = clock();
	for (int test = 1; test <= T; ++test)
	{
		double start = clock();
		int n;
		cin >> n;
		long long answer = brute_solve(n);
		cout << "Case #" << test << ": ";
		if (answer < 0)
			cout << "INSOMNIA";
		else
			cout << answer;
		cout << endl;
		double finish = clock();
		cerr << (finish - start) / CLOCKS_PER_SEC << "s" << endl << endl;
	}
	cerr << "Total time: " << (clock() - global_start) / CLOCKS_PER_SEC << "s" << endl;

	return 0;
}

