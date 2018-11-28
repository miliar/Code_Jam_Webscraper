#include <bits/stdc++.h>
using namespace std;

int n, server, onServer[1111], ans, ways;
string s[1111];
int next[100100][26], trieNode;

int newNode()
{
	for (int i = 0; i < 26; i++) next[trieNode][i] = -1;
	return trieNode++;
}

void traverse(int node, string s, int id)
{
	if (id == s.size()) return;
	int ch = s[id] - 'A';
	if (next[node][ch] < 0) next[node][ch] = newNode();
	traverse(next[node][ch], s, id + 1);
}

int calc()
{
	int res = 0;
	
	for (int i = 1; i <= server; i++)
	{
		trieNode = 0;
		newNode();
		for (int j = 0; j < n; j++)
			if (onServer[j] == i)
				traverse(0, s[j], 0);
		
		res += trieNode;
	}
	return res;
}

void att(int i, int used)
{
	if (i == n)
	{
		if (used < server) return;
		int nodes = calc();
		if (nodes == ans) ways++;
		else 
			if (nodes > ans) ans = nodes, ways = 1;
		return;
	}
	
	for (int j = 1; j <= used; j++) 
	{
		onServer[i] = j;
		att(i + 1, used);
	}
	
	if (used < server)
	{
		onServer[i] = used + 1;
		att(i + 1, used + 1);
	}
}

int main()
{
	freopen("d.in", "r", stdin); 
	freopen("d.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		cin >> n >> server;
		for (int i = 0; i < n; i++) cin >> s[i];
		onServer[0] = 1;
		ans = ways = 0;
		att(1, 1);
		
		for (int i = 2; i <= server; i++) ways *= i;
		
		printf("Case #%d: %d %d\n", noTest, ans, ways);
	}
}
