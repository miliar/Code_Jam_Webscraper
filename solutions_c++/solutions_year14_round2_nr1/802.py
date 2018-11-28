#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define REP(it,v,cont) for(cont::iterator (it)=(v).begin();(it)!=(v).end();++(it)) 
#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define MOD 1000003 
#define INF 1000000000
typedef long long  ll;
typedef unsigned long long  ull;
typedef pair<int,int> pii;

vector <int> adj[128];

string convert(string x, int idx)
{
	string res = "";
	int cnt;
	for(int i = 0; i < x.size(); i ++)
	{
		if(i == 0)
		{
			res += x[i];
			cnt = 1;
		}
		else if(x[i] != res[res.size()-1])
		{
			adj[idx].push_back( cnt );
			
			cnt = 1;
			res += x[i];
		}
		else
		{
			cnt ++;
		}
	}
	adj[idx].push_back( cnt );
	return res;
}

string s[128];
string cc[128];

int main()
{
	// freopen("input.txt", "r", stdin);
	
	int test;
	int n;
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		
		cin >> n;
		for(int i = 0; i < n; i ++)
			adj[i].clear();
			
		set <string> all;
		for(int i = 0; i < n; i ++)
		{
			cin >> s[i];
			cc[i] = convert( s[i], i );
			// cout << s[i] << endl;
			// for(int j = 0; j < adj[i].size(); j ++)
				// cout << adj[i][j] << " ";
			// cout << endl;
			
			all.insert( cc[i] );
		}
		
		printf("Case #%d: ", cas);
		if(all.size() != 1)
		{
			cout << "Fegla Won" << endl;
		}
		else
		{
			int res = 0;
			for(int j = 0; j < adj[0].size(); j ++)
			{
				int mn = 1000000;
				for(int sz = 1; sz <= 100; sz ++)
				{
					int now = 0;
					for(int i = 0; i < n; i ++)
					{
						now += abs( adj[i][j] - sz );
					}
					mn = min(mn, now);
				}
				res += mn;
			}
			cout << res << endl;
		}
	}
	
	return 0;
}














