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

int r, c;

int change(vector<string> &a, int x, int y)
{
	int sum=0;

	char ch = a[y][x];
	if(ch == '.')
		return 0;

	if(ch == '<')
	{
		for(int i=0; i<x; ++i)
			if(a[y][i] != '.')
				return 0;
	}
	if(ch == '>')
	{
		for(int i=x+1; i<c; ++i)
			if(a[y][i] != '.')
				return 0;
	}
	if(ch == 'v')
	{
		for(int i=y+1; i<r; ++i)
			if(a[i][x] != '.')
				return 0;
	}
	if(ch == '^')
	{
		for(int i=0; i<y; ++i)
			if(a[i][x] != '.')
				return 0;
	}

	for(int i=0; i<r; ++i)
		if(a[i][x] != '.')
			++sum;

	for(int i=0; i<c; ++i)
		if(a[y][i] != '.')
			++sum;

	if(sum == 2)
		return -1; // impossible
	if(2 < sum)
		return 1;
	cerr << "!!!!!!\n";
	return 0;
}

int main() {
	int t;

	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		cin >> r >> c;
		vector<string> a(r);
		for(int y=0; y<r; ++y)
			//for(int x=0; x<c; ++x)
				cin >> a[y];

		int res = 0;

		bool ok = true;
		for(int y=0; y<r && ok; ++y)
			for(int x=0; x<c && ok; ++x)
			{
				int q = change(a, x, y);
				//print3(x, y, q);
				if(q < 0)
					ok = false;
				else
					res += q;

			}

		if(!ok)
			cout << "Case #" << tt << ": " << "IMPOSSIBLE\n";
		else
			cout << "Case #" << tt << ": " << res << "\n";
	}

	return 0;
}
