#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

struct node
{
	int size;
	long long ans; // # ways to maximize node count with color domain [1, min(size, m)]
	int children[26];
	
	node()
	{
		size = 0;
		fill(children, children + 26, -1);
	}
};

const long long mod = 1000000007;

int main()
{
	int caseN;
	cin >> caseN;
	for (int caseI = 1; caseI <= caseN; caseI++)
	{
		int n, m;
		cin >> n >> m;
		
		vector<string> str(n);
		for (int i = 0; i < n; i++)
			cin >> str[i];
		
		vector<node> nodes;
		nodes.push_back(node());
		
		set<int> leaves;

		for (int i = 0; i < n; i++)
		{
			int id = 0;
			nodes[id].size++;
			for (int j = 0; j < str[i].size(); j++)
			{
				int e = str[i][j] - 'A';
				if (nodes[id].children[e] == -1)
				{
					nodes[id].children[e] = nodes.size();
					nodes.push_back(node());
				}
				id = nodes[id].children[e];
				nodes[id].size++;
			}
			
			leaves.insert(id);
		}
		
		
		int max_nodes = 0;
//		for (int i = 0; i < nodes.size(); i++)
//			max_nodes += min(nodes[i].size, m);
		
		int total = 1;
		for (int i = 0; i < n; i++)
			total *= m;
		
		int ways = 0;
		for (int s = 0; s < total; s++)
		{
			vector<set<int> > colors(nodes.size());
			int ss = s;
			for (set<int>::iterator it = leaves.begin(); it != leaves.end(); it++)
			{
				int id = *it;
				colors[id].insert(ss % m);
				ss /= m;
			}
			
			int cur_nodes = 0;
			for (int i = nodes.size() - 1; i >= 0; i--)
			{
				for (int j = 0; j < 26; j++)
					if (nodes[i].children[j] != -1)
					{
						int id = nodes[i].children[j];
						colors[i].insert(colors[id].begin(), colors[id].end());
					}
				
				cur_nodes += colors[i].size();
			}
			
			if (cur_nodes > max_nodes)
			{
				max_nodes = cur_nodes;
				ways = 0;
			}
			
			if (cur_nodes == max_nodes)
				ways++;
		}
/*		vector<long long> factorial(1, 1);
		for (int i = 0; i < n; i++)
			factorial.push_back((factorial[i] * (long long)(i + 1)) % mod);
		
		vector<vector<long long> > binom(1, vector<long long>(1, 1));
		for (int i = 1; i <= n; i++)
		{
			binom.push_back(vector<long long>(i + 1));
			binom[i][0] = binom[i][i] = 1;
			for (int j = 1; j < i; j++)
				binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % mod;
		}
		
		for (int i = nodes.size() - 1; i >= 0; i--)
		{
			if (nodes[i].size <= m)
			{
				nodes[i].ans = factorial[nodes[i].size];
				continue;
			}
			
			vector<vector<long long> > dp(27);
			dp[0] = vector<long long>(1, 1);
			
			int max_size = 0;
			int sum_size = 0;
			for (int j = 0; j < 26; j++)
			{
				if (nodes[i].children[j] == -1)
				{
					dp[j + 1] = dp[j];
					continue;
				}
				
				int id = nodes[i].children[j];
				int cur_size = min(nodes[id].size, m);
				
				int new_max = max(max_size, cur_size);
				int new_sum = min(m, sum_size + cur_size);
				
				dp[j + 1] = vector<long long>(new_sum + 1, 0);
				
				for (int k = new_max; k <= new_sum; k++)
				{
					for (int l = max_size; l <= min(sum_size, k); l++)
					{
						long long delta = 1;
						delta = (delta * binom[k][l]) % mod;
						delta = (delta * dp[j][l]) % mod;
						delta = (delta * binom[l][l + cur_size - k]) % mod;
						delta = (delta * nodes[id].ans) % mod;
						dp[j + 1][k] = (dp[j + 1][k] + delta) % mod;
					}
				}
				
				max_size = new_max;
				sum_size = new_sum;
			}
			
			nodes[i].ans = dp[26][m];
		}*/
		
		
		cout << "Case #" << caseI << ": " << max_nodes << " " << ways << endl;
	}
	
	return 0;
}
