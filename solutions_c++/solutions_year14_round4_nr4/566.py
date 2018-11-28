#include <iostream>
#include <map>
#include <string>
using namespace std;

const char lend = '\n';
const int N = 8;

struct Trie
{
	map<char, Trie> m;
};

int m, n, maior;
string str[N];

Trie root[N];
map<int, int> cnt;

void insere(Trie& t, const char* str)
{
	if (str[0] == 0) return;
	insere(t.m[str[0]], str+1);
}

int conta(Trie& t)
{
	int c = 1;
	for (typeof(t.m.begin()) it = t.m.begin(); it != t.m.end(); ++it)
		c += conta(it->second);
	return c;
}

void solve(int p)
{
	if (p == m)
	{
		for (int i = 0; i < n; ++i)
			if (root[i].m.empty()) return;
		int c = 0;
		for (int i = 0; i < n; ++i)
			c += conta(root[i]);
		cnt[c]++;
		maior = max(maior, c);
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		Trie tmp = root[i];
		insere(root[i], str[p].c_str());
		solve(p+1);
		root[i] = tmp;
	}
}

int main() 
{
	ios::sync_with_stdio(0);
	int t;
	cin >> t;
	
	for (int caso = 1; caso <= t; ++caso)
	{
		cout << "Case #" << caso << ": ";
		cin >> m >> n;
		for (int i = 0; i < m; ++i)
			cin >> str[i];
		cnt.clear();
		maior = 0;
		solve(0);
		cout << maior << ' ' << cnt[maior] << lend;
	}
}
