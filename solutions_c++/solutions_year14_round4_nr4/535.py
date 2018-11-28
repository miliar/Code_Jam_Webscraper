#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <functional>

using namespace std;

const int NMAX = 10000;
int n, m;
int max_ans, num_ans;
vector<int> P[4];
vector <string> S;

struct vertex {
	int next[30];
};

vertex t[NMAX+1];
int sz;

void add_string (const string & s) {
	int v = 0;
	for (size_t i=0; i<s.length(); ++i) {
		char c = s[i]-'A'; // в зависимости от алфавита
		if (t[v].next[c] == -1) {
			memset (t[sz].next, -1, sizeof t[sz].next);
			t[v].next[c] = sz++;
		}
		v = t[v].next[c];
	}
}

int build_tries()
{
	int res = 0;
	for(int i = 0; i < n; ++i)
	{
		memset (t[0].next, -1, sizeof t[0].next);
		sz = 1;
		for(int j = 0; j < P[i].size(); ++j)
			add_string(S[P[i][j]]);
		res += sz;
	}
	return res;
}

void rec(int cur)
{
	if(cur == m)
	{
		for(int i = 0; i < n; ++i)
			if(P[i].size() == 0)
				return;
		int tmp = build_tries();
		if(tmp > max_ans)
		{
			max_ans = tmp;
			num_ans = 1;
		}
		else if(tmp == max_ans)
		{
			num_ans++;
		}
		return;
	}

	for(int i = 0; i < n; ++i)
	{
		P[i].push_back(cur);
		rec(cur + 1);
		P[i].pop_back();
	}
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
  
	int T;
	cin >> T;

	for(int t = 1; t <= T; ++t)
	{
		cin >>  m >> n;
		S.clear();
		S.resize(m);
		for(int i = 0; i < m; ++i)
			cin >> S[i];

		max_ans = 0;
		num_ans = 0;
		rec(0);


		cout << "Case #" << t << ": " << max_ans << " " << num_ans << endl;
	}

    return 0;
}