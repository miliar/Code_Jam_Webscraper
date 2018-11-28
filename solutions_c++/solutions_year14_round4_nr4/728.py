#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

long long choose(int n, int k)
{
	long long ret = 1;
	for(int i = 2; i <= n; i++)
	{
		ret = ((ret * i) % 1000000007);
	}

	for(int i = 2; i <= n - k; i++)
	{
		ret = ((ret / i) % 1000000007);
	}

	for(int i = 2; i <= k; i++)
	{
		ret = ((ret / i) % 1000000007);
	}

	return ret;
}


pair<int, long long> compute_in_tree(vector<string>& v, int N)
{
	vector<int> value;
	vector< map<char, int> > children;

	value.push_back(0);
	children.push_back(map<char, int>());

	// build a prefix tree
	for(int i = 0; i < v.size(); i++)
	{
		int ptr = 0;
		for(int j = 0; j < v[i].size(); j++)
		{
			if(value[ptr] < N) value[ptr]++;
			if(children[ptr].count(v[i][j]) == 0)
			{
				value.push_back(0);
				children.push_back(map<char, int>());
				children[ptr][v[i][j]] = value.size() - 1;
			}
			ptr = children[ptr][v[i][j]];
		}
		value[ptr]++;
	}

	pair<int, long long> sol = pair<int, long long>(-v.size(), 1);

	for(int i = 0; i < value.size(); i++)
	{
		sol.first += value[i];

		if(children[i].size() == 0) continue;
		int max_value = 0;
		for(map<char, int>::iterator it = children[i].begin(); it != children[i].end(); it++)
		{
			if(max_value < value[it->second]) max_value = value[it->second];
		}

		int sign = 1;

		long long level_cumul = 0;
		for(int j = value[i]; j >= max_value; j--)
		{
			long long cumul = choose(value[i], j);
			for(map<char, int>::iterator it = children[i].begin(); it != children[i].end(); it++)
			{
				// j choose value[it->second]
				cumul = ((cumul * choose(j, value[it->second])) % 1000000007);
			}
			level_cumul += (sign * cumul);
			level_cumul = (level_cumul % 1000000007);
			sign *= -1;
		}
		sol.second = ((sol.second * level_cumul) % 1000000007);
	}

	return sol;
}


int main(int argc, char** argv)
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; i++)
	{
		int M, N;
		vector<string> v;

		cin >> M >> N;
		v.resize(M);
		for(int j = 0; j < M; j++)
		{
			cin >> v[j];
			v[j] = v[j] + " ";
		}

		pair<int, long long> sol = compute_in_tree(v, N);

		cout << "Case #" << i << ": " << sol.first << " " << sol.second << endl;
	}
	return 0;
}

