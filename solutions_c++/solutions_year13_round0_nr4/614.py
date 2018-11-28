#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#define sz(a) ((int)(a).size())
#define foreach(i, Type, v) for(Type::iterator i=v.begin(); i!=v.end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int compareTo(double a, double b) { return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

bool flags;
map<int, int> *f;
int N, type[30];
vector<int> ans, keys[30];

void dfs(int s)
{
	if( flags )
		return;
	if( __builtin_popcount(s) == N )
	{
		flags = true;
		return;
	}
	for(int i=0; i<N; i++)
		if( (s&(1<<i))==0 && f[s][type[i]]>0 )
		{
			int s1 = s|(1<<i);
			if( sz(f[s1]) != 0 )
				continue;
			ans.push_back(i);
			f[s1] = f[s];
			f[s1][type[i]]--;
			for(int j=0; j<sz(keys[i]); j++)
				f[s1][keys[i][j]]++;
			dfs(s1);
			if( flags )
				return;
			ans.pop_back();
		}
}

int main()
{
	int K, cas, t1, t2;
	ios::sync_with_stdio(0);
	freopen("aaa.in", "r", stdin);
	freopen("aaa.out", "w", stdout);

	cin>>cas;
	for(int c=1; c<=cas; c++)
	{
		cin>>K>>N;
		f = new map<int, int> [1<<N];
		ans.clear();
		flags = false;
		for(int i=0; i<K; i++)
		{
			cin>>t1;
			f[0][t1]++;
		}
		for(int i=0; i<N; i++)
		{
			cin>>type[i];
			cin>>t1;
			keys[i].clear();
			for(int j=0; j<t1; j++)
			{
				cin>>t2;
				keys[i].push_back(t2);
			}
		}
		dfs(0);
		printf("Case #%d:", c);
		if( flags )
			for(int i=0; i<sz(ans); i++)
				printf(" %d", ans[i]+1);
		else
			printf(" IMPOSSIBLE");
		printf("\n");
	}

	return 0;
}
