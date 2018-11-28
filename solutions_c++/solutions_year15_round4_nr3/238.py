#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int INF = (int)1e9;

map<string, int> ind;

int get_ind(string s)
{
	if (ind.count(s) == 0)
	{
		int c = ind.size();
		ind[s] = c;
	}
	return ind[s];
}

vector<string> split(string str)
{
	vector<string> res;
	string token;
	for (char c : str)
	{
		if (c == ' ')
		{
			if (!token.empty())
				res.push_back(token);
			token.clear();
		}
		else
			token.push_back(c);
	}
	return res;
}

void next_line()
{
	string s;
	getline(cin, s);
}

vector<int> scan()
{
	string str;
	getline(cin, str);
	str += " ";
	vector<string> list = split(str);
	vector<int> res;
	for (string s : list)
		res.push_back(get_ind(s));
	return res;
}

bool bit(int mask, int bit)
{
	return (mask & (1 << bit)) != 0;
}

void solve(int test)
{
	ind.clear();
	
	int n;
	cin >> n;
	next_line();
	vector<vector<int> > mx(n);
	for (int i = 0; i < n; i++)
		mx[i] = scan();
	
	int ans = INF;
	for (int _mask = 0; _mask < (1 << (n - 2)); _mask++)
	{
		vector<int> masks((int)ind.size());
		int mask = (_mask << 2);
		mask |= (1 << 1);

		for (int i = 0; i < n; i++)
		{
			for (int j : mx[i])
			{
				if (!bit(mask, i))
					masks[j] |= 1;
				else
					masks[j] |= 2;
			}
		}

		int cur_ans = 0;
		for (int i = 0; i < (int)ind.size(); i++)
		{
			if (masks[i] == 3)
				cur_ans++;
		}
		ans = min(ans, cur_ans);
	}
	
	printf("Case #%d: %d\n", test, ans);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
		solve(i + 1);

	return 0;
}
