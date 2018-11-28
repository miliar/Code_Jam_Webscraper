#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

vector<long long> v[300];

const int english = 0, france = 1;

long long to_longlong(string x)
{
	long long cur = 1, ret = 0;
	for(int i = 0; i < x.size(); ++i)
	{
		ret += cur * (x[i] - 'a' + 1);
		cur = cur * 27;
	}
	return ret;
}

map<long long, int> s;

bool eng[100000], fra[100000];

int main()
{
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas)
	{
		int n, tot = 0;
		scanf("%d", &n);
		s.clear();
		for(int i = 0; i < n; ++i)
		{
			v[i].clear();
			while(true)
			{
				string x;
				cin >> x;
				long long p = to_longlong(x);
				v[i].push_back(p);
				if(!s.count(p))
					s[to_longlong(x)] = tot++;
				if(getchar() == '\n') break;
			}
		}
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < v[i].size(); ++j)
				v[i][j] = s[v[i][j]];
		int ans = 0x3f3f3f3f;
		for(int i = 0; i < (1 << (n)); ++i)
		{
			if((i & 1) != english || ((i >> 1) & 1) != france)
				continue;
			for(int j = 0; j < v[0].size(); ++j)
				eng[v[0][j]] = true;
			for(int j = 0; j < v[1].size(); ++j)
				fra[v[1][j]] = true;
			for(int j = 2; j < n; ++j)
			{
				if(((i >> j) & 1) == english)
					for(int k = 0; k < v[j].size(); ++k)
						eng[v[j][k]] = true;
				else
					for(int k = 0; k < v[j].size(); ++k)
						fra[v[j][k]] = true;
			}
			
			int res = 0;
			for(int i = 0; i < tot; ++i)
			{
				if(eng[i] && fra[i])
					res++;
				eng[i] = fra[i] = false;
			}
			
			ans = min(ans, res);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
