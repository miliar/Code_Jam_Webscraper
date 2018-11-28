#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <limits>
#include <future>
#include <functional>
#include <iomanip>
using namespace std;

const string IMPOSSIBLE = "IMPOSSIBLE";

struct TestCase
{
	int n;
	double v, x;
	double r[256], c[256];
	double answer;

	void input()
	{
		cin >> n;
		cin >> v >> x;

		for (int i = 0; i < n; i++)
		{
			cin >> r[i] >> c[i];
		}
	}
	void process()
	{
		if (n == 1)
		{
			if (c[0] != x)
			{
				answer = -1;
				return;
			}
			answer = v / r[0];
			return;
		}
		if (n == 2)
		{
			if (x < c[0] && x < c[1])
			{
				answer = -1;
				return;
			}
			if (x > c[0] && x > c[1])
			{
				answer = -1;
				return;
			}
			if (c[0] == c[1])
			{
				if (c[0] != x)
				{
					answer = -1;
					return;
				}
				answer = v / (r[0] + r[1]);
				return;
			}
			double k = x * v;
			double v1 = v * (x - c[0]) / (c[1] - c[0]);
			double v0 = v - v1;
			double t1 = v1 / r[1];
			double t0 = v0 / r[0];
			answer = max(t1, t0);
			return;
		}
		answer = -1;
	}
	void output()
	{
		if (answer < 0)
		{
			cout << IMPOSSIBLE;
			return;
		}
		printf("%10.9lf", answer);
	}
};

int main()
{
	int t;
	cin >> t;
	vector<TestCase> testCases(t);
	vector<future<void>> futures;
	for (int i = 0; i < t; i++)
	{
		testCases[i].input();
	}
	for (int i = 0; i < t; i++)
	{
		futures.push_back(async(launch::async, [&](int p){ testCases[p].process(); }, i));
	futures[i].wait();
	}
	for (int i = 0; i < t; i++)
	{
		futures[i].wait();
	}
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		testCases[i].output();
		cout << endl;
	}
	return 0;
}
