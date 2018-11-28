#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

#define FORALL(c,i) for(auto i = (c).begin(); i != (c).end(); ++i)
#define ALL(c) (c).begin(),(c).end() 
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

int nall;
map<ll,int> ef[2];
int theres;
int sum[2];

ll makehash(string &s)
{
	ll h = 0;
	ll d = 32;
	for(int i=0; i<s.size(); ++i)
		h = h*d + s[i]-'a'+1;
	if(h < 0)
		cerr << "!!!!!!!!\n";
	return h;
}

void solve1(vector< vector<ll> > &a, int n, int depth)
{
	if(depth == n)
	{
		//int sum1=0, sum2=0;

		//FORALL(ef[0], it)
		//	if(it->second)
		//		++sum1;

		//FORALL(ef[1], it)
		//	if(it->second)
		//		++sum2;

		//int x = sum1 + sum2 - nall;
		int x = sum[0] + sum[1] - nall;
		theres = min(x, theres);
		return;
	}

	for(int i=0; i<2; ++i)
	{
		if(depth < 2 && i != depth)
			continue;
		
		for(int j=0; j<a[depth].size(); ++j)
		{
			if(ef[i][a[depth][j]] == 0)
				++sum[i];
			++ef[i][a[depth][j]];
		}

		solve1(a, n, depth+1);

		for(int j=0; j<a[depth].size(); ++j)
		{
			--ef[i][a[depth][j]];
			if(ef[i][a[depth][j]] == 0)
				--sum[i];
		}
	}
}

int solve0(vector< vector<string> > &a, int n)
{
	int res = 999999;

	for(int mm=0; mm<(1<<(n-2)); ++mm)
	{
		set<string> ef[2];
		int m = 4*mm + 1;

		for(int i=0; i<n; ++i)
		{
			int k = (m >> i) & 1;

			for(int j=0; j<a[i].size(); ++j)
				ef[k].insert(a[i][j]);
		}

		int x = ef[0].size() + ef[1].size() - nall;
		res = min(x, res);
	}

	return res;
}

int main() {
	int t;
	char line[99999];

	gets(line);
	sscanf(line, "%d", &t);
	//cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		set<string> all;

		int n;
		gets(line);
		sscanf(line, "%d", &n);
		vector< vector<ll> > a(n);
		for(int i=0; i<n; ++i)
		{
			gets(line);
			stringstream sinput(line);
			while(!sinput.eof())
			{
				string str;
				sinput >> str;
				a[i].push_back( makehash(str) );
				all.insert(str);
			}
		}

		nall = all.size();

		//int res = solve1(a, n);

		theres = 999999;
		sum[0] = sum[1] = 0;
		solve1(a, n, 0);
		int res = theres;

		
		cout << "Case #" << tt << ": " << res << "\n";
	}

	return 0;
}
