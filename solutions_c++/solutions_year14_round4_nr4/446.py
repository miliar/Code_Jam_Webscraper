#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int n, m;
vector <string> data;
int ans, maxNode;

struct Node
{
	int child[26];
	Node() { memset(child, -1, sizeof(child)); }
};

int getCost(const vector <string> &left)
{
	vector <Node> trie;
	trie.push_back(Node());

	for(const auto &str: left)
	{
		int ind = 0;
		for(char ch: str)
		{
			if(trie[ind].child[ch - 'A'] == -1)
			{
				trie[ind].child[ch - 'A'] = trie.size();
				trie.push_back(Node());
			}

			ind = trie[ind].child[ch - 'A'];
		}
	}

	return trie.size();
}

void backtr(int level, int cost, vector <string> left)
{
	if(level == m - 1)
	{
		cost += getCost(left);
		if(cost > maxNode) { maxNode = cost; ans = 1; }
		else if (cost == maxNode) ans++;
		return;
	}

	for(int i = 0; i < (1 << left.size()); i++)
	{
		vector <string> cur, next;
		for(int j = 0; j < left.size(); j++)
			if(i & (1 << j)) cur.push_back(left[j]);
			else next.push_back(left[j]);

		if(cur.size() == 0 || next.size() == 0) continue;
		backtr(level + 1, cost + getCost(cur), next);
	}
}

int main(void)
{
	int T;
	cin >> T;
	for(int kase = 1; kase <= T; kase++)
	{
		cin >> n >> m;
		data.resize(n);
		for(int i = 0; i < n; i++) cin >> data[i];

		maxNode = 0;
		backtr(0, 0, data);

		printf("Case #%d: %d %d\n", kase, maxNode, ans);
		fprintf(stderr, "Case #%d: %d %d\n", kase, maxNode, ans);
	}

	return 0;
}
