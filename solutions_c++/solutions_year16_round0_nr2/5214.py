#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <time.h>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

string maneuver(const string &stack, int top)
{
	string result = stack;

	reverse(result.begin(), result.begin() + top);

	for (int i = 0; i < top; ++i)
	{
		if (result[i] == '+')
			result[i] = '-';
		else
			result[i] = '+';
	}
	return result;
}

string invert(const string stack)
{
	string result = stack;
	for (int i = 0; i < stack.size(); ++i)
	{
		if (result[i] == '+')
			result[i] = '-';
		else
			result[i] = '+';
	}
	return result;
}

int solve(const string &stack)
{
	const string target(stack.size(), '+');
	if (stack == target) return 0;

	if (stack.back() != '-')
		return solve(stack.substr(0, stack.find_last_of('-') + 1));

	return solve(invert(stack.substr(0, stack.find_last_of('+') + 1))) + 1;
}

int solve1(const string &stack)
{
	string state = stack;
	const string target(stack.size(), '+');
	const int n = stack.size();
	set<string> visited;
	visited.insert(stack);

	int answer = 0;
	while (state != target)
	{
		int max_value = -1;
		int max_i = 0;
		for (int i = 1; i <= n; ++i)
		{
			string candidate = maneuver(state, i);
			if (visited.find(candidate) != visited.end())
			{
				continue;
			}

			int pluses = count(candidate.begin(), candidate.end(), '+'), minuses = n - pluses;
			int score = abs(pluses - minuses);
			if (score > max_value)
			{
				max_value = score;
				max_i = i;
			}
		}

		state = maneuver(state, max_i);
		++answer;
		visited.insert(state);
	}
	return answer;
}

int brute_solve(const string &stack)
{
	queue<string> bfs;
	bfs.push(stack);
	map<string, int> dist;
	const string target(stack.size(), '+');
	dist[stack] = 0;

	while (dist.find(target) == dist.end())
	{
		string v = bfs.front();
		bfs.pop();

		for (int i = 1; i <= v.size(); ++i)
		{
			string candidate = maneuver(v, i);
			if (dist.find(candidate) == dist.end())
			{
				dist[candidate] = dist[v] + 1;
				bfs.push(candidate);
			}
		}
	}

	return dist[target];
}

void test()
{
	// cout << solve("--+--") << endl;

	cout << 100 << endl;
	for (int test = 0; test < 100; ++test)
	{
		int n = 100;
		string stack(n, '-');
		for (int i = 0; i < n; ++i)
		{
			if (rand() & 1)
			{
				stack[i] = '+';
			}
		}
		cout << stack << endl;
	}
}

void stress()
{
	//cerr << "TL tests" << endl;
	//double worst_time = 0;
	//for (int test = 0; test < 1000; ++test)
	//{
	//	int n = 100;
	//	string stack(n, '-');
	//	for (int i = 0; i < n; ++i)
	//	{
	//		if (rand() & 1)
	//		{
	//			stack[i] = '+';
	//		}
	//	}

	//	// cout << stack << endl;
	//	double start = clock();
	//	cout << solve(stack) << "\r";
	//	double finish = clock();

	//	double duration = (finish - start) / CLOCKS_PER_SEC;
	//	if (duration > worst_time)
	//	{
	//		worst_time = duration;
	//		cout << "Time: " << duration << "sec" << endl;
	//	}
	//}

	for (int n = 1; n <= 30; ++n)
	{
		cerr << "Input lenght is " << n << endl;
#pragma omp parallel for
		for (int state = 0; state < (1 << n); ++state)
		{
			string stack(n, '-');
			for (int i = 0; i < n; ++i)
			{
				if (state & (1 << i))
				{
					stack[i] = '+';
				}
			}

			// cerr << stack << endl;

			int ans1 = solve(stack);
			
			int ans2 = brute_solve(stack);

			if (ans1 != ans2)
			{
				cout << "WA!!!" << endl;
				cout << "Input: " << stack << endl;
				cout << "Solution: " << ans1 << endl;
				cout << "Currect: " << ans2 << endl;
				// return;
			}
		}
	}
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios_base::sync_with_stdio(false);
	srand(13);

	// test();
	// stress();
	// return 1;

	int T;
	cin >> T;
	double global_start = clock();
	for (int test = 1; test <= T; ++test)
	{
		double start = clock();
		string stack;
		cin >> stack;
		long long answer = solve(stack);
		cout << "Case #" << test << ": " << answer << endl;
		double finish = clock();
		cerr << (finish - start) / CLOCKS_PER_SEC << "s" << endl << endl;
	}
	cerr << "Total time: " << (clock() - global_start) / CLOCKS_PER_SEC << "s" << endl;

	return 0;
}

