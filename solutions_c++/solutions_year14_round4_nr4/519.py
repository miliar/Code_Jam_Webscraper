#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int calculateTrieSize(const vector<string> & v)
{
	set<string> trie;
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 1; j <= v[i].size(); j++)
		{
			trie.insert(v[i].substr(0, j));
		}
	}
	return trie.size() + 1;
}

int my_pow(int n, int p)
{
	int res = 1;
	for (int i = 0; i < p; i++)
		res *= n;
	return res;
}

vector<string> v;
vector<vector<string> > splitAccording(int i, int n) {
	vector<vector<string> > res(n);
	for (int j = 0; j < v.size(); j++)
	{
		res[i % n].push_back(v[j]);
		i /= n;
	}
	return res;
}

bool thereIsEmpty(const vector<vector<string> >& tmp)
{
	for (int i = 0; i < tmp.size(); i++)
	{
		if (tmp[i].size() == 0)
			return true;
	}
	return false;
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int m, n;
		cin >> m >> n;
		v.clear();
		v.resize(m);
		for (int i = 0; i < m; i++)
			cin >> v[i];

		int maxm = 0;
		int count = 0;
		int lim = my_pow(n, m);
		for (int i = 0; i < lim; i++)
		{
			vector<vector<string> > tries = splitAccording(i, n);
			if (thereIsEmpty(tries))
			{
				continue;
			}

			int res = 0;
			for (int i = 0; i < tries.size(); i++)
			{
				res += calculateTrieSize(tries[i]);
			}
			if (res > maxm)
			{
				maxm = res;
				count = 1;
			} else if (res == maxm)
				count++;
		}
		cout << maxm << " " << count << endl;
	}
	return 0;
}
