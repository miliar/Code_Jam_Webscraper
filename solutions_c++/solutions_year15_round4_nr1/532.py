#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <limits>
#include <string>
#include <future>
#include <functional>
using namespace std;

const int Dx[] = {1, -1, 0, 0};
const int Dy[] = {0, 0, 1, -1};
const string IMPOSSIBLE = "IMPOSSIBLE"; 

struct TestCase
{
	int n, m;
	int data[128][128];
	int answer;

	void input()
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
		{
			string a;
			cin >> a;
			for (int j = 0; j < m; j++)
			{
				if (a[j] == '^')
				{
					data[i][j] = 1;
				}
				else if (a[j] == '>')
				{
					data[i][j] = 2;
				}
				else if (a[j] == '<')
				{
					data[i][j] = 3;
				}
				else if (a[j] == 'v')
				{
					data[i][j] = 0;
				}
				else 
				{
					data[i][j] = -1;
				}
			}
		}
	}

	bool check(int i, int j, int dx, int dy)
	{
		i += dx;
		j += dy;
		while (1)
		{
			if (i < 0 || j < 0 || i >= n || j >= m)
			{
				return false;
			}
			if (data[i][j] >= 0)
			{
				return true;
			}
			i += dx;
			j += dy;
		}
	}

	void process()
	{
		answer = 0;

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (data[i][j] >= 0)
				{
					if (check(i, j, Dx[data[i][j]], Dy[data[i][j]]) == false)
					{
						int d;
						for (d = 0; d < 4; d++)
						{
							if (data[i][j] == d)
							{
								continue;
							}
							if (check(i, j, Dx[d], Dy[d]))
							{
								answer++;
								break;
							}
						}
						if (d < 4)
						{
							continue;
						}
						answer = -1;
						return;
					}
				}
			}
		}
	}
	void output()
	{
		if (answer < 0)
		{
			cout << IMPOSSIBLE;
			return;
		}
		cout << answer;
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
