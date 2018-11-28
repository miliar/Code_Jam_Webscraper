#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <time.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");
#define cin in
#define cout out
/**/
// rock paper scissors

double mx = 0;

double dfs2(int n, vector<double> & cur)
{
	double ans = 0;
	for(int i = 0; i < (1<<n); ++i)
	{
		int c = 0;
		for(int j = 0; j < n; ++j)
			if(i & (1<<j))
				++c;
		if(c != n/2)
			continue;
		double t = 1;
		for(int j = 0; j < n; ++j)
		{
			if(i & (1<<j))
				t *= cur[j];
			else
				t *= 1-cur[j];
		}
		ans += t;
	}
	return ans;
}
vector<double> v;

void dfs(int n, int k, int last, vector<double> & cur)
{
	if(cur.size() == k)
	{
		mx = max(mx, dfs2(k, cur));
		return;
	}
	for(;last < n; ++last)
	{
		if(n-cur.size()-1 >= n-last-1)
		{
			cur.push_back(v[last]);
			dfs(n,k,last+1,cur);
			cur.pop_back();
		}
	}
}

int main()
{
	int test;
	cin >> test;
	for(int _ = 1; _ <= test; ++_)
	{
		int n,k;
		cin >> n >> k;
		v.assign(n,0);
		for(int i = 0; i < n; ++i)
			cin >> v[i];
		vector<double> cur;
		dfs(n,k, 0, cur);
		cout.precision(12);
		cout << fixed << "Case #" << _ << ": " << mx << endl;
		mx = 0;
	}
	return 0;
}

/*
1 245
2 13
3 25
4 1
5 13

3 2 1 2 1

*/