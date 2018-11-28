#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 

#define pb push_back 
#define mp make_pair 
#define float long double 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 

int n, m, ans, y;

int c[8], d[4];

set<string> st[4];

string str[8];

void solve()
{
	for(int i = 0; i < n; i++)
		st[i].clear();
	for(int i = 0; i < m; i++)
	{
		for(int j = 0; j <= str[i].length(); j++)
		{
			st[c[i]].insert(str[i].substr(0, j));
		}
	}
	int cur = 0;
	for(int i = 0; i < n; i++)
		cur += st[i].size();
	if (cur == ans) {
		y++;
	} else {
		if (cur > ans) {
			ans = cur;
			y = 1;
		}
	}
}

void rec(int k)
{
	if (k == m)
	{
		for(int i = 0; i < n; i++)
			d[i] = 0;
		for(int i = 0; i < m; i++) {
			d[c[i]] = 1;
		}
		for(int i = 0; i < n; i++)
			if (d[i] == 0)
				return;
		solve();
		return;
	}
	for(int i = 0; i < n; i++)
	{
		c[k] = i;
		rec(k + 1);
	}
}

int main(){ 
	int T;
	cin >> T;
	for(int test = 0; test < T; test++)
	{
		cerr << test << endl;
		printf("Case #%d: ", test + 1);
		cin >> m >> n;
		for(int i = 0; i < m; i++)
			cin >> str[i];
		ans = 0;
		rec(0);
		
		cout << ans << " " << y << endl;
		
		
	}
	
	
	
	return 0; 
} 
