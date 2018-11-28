#pragma comment(linker, "/STACK:268435456")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <queue>
#include <iomanip>
#include <assert.h>
#include <stack>
#include <deque>
#include <limits.h>
#include <memory.h>
#include <time.h>
//#include <unordered_map>
//#include <unordered_set>
using namespace std;

void prepare(string q)
{
#ifdef _DEBUG
	//system("color F0");
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#else
	if (q.size()!=0)
	{
		freopen((q+".in").c_str(),"r",stdin);
		freopen((q+".out").c_str(),"w",stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	cin.tie(false);
}

typedef long double ld;

void solve() 
{
	int n;
	cin>>n;
	for (int ii=1; ii<=n; ++ii)
	{
		int m;
		cin>>m;
		vector <ld> h(m),g(m);
		set <ld> o,oo;
		for (int i=0; i<m; ++i)
		{
			cin>>h[i];
			oo.insert(h[i]);
		}
		//sort(h.begin(),h.end());
		for (int i=0; i<m; ++i)
		{
			cin>>g[i];
			o.insert(g[i]);
		}
		//sort(g.begin(),g.end());
		int d=0,w=0;
		for (int i=0; i<m; ++i)
		{
			set <ld> :: iterator it=o.lower_bound(h[i]);
			if (it==o.begin())
				o.erase(*o.rbegin());
			else
			{
				--it;
				o.erase(it);
				++d;
			}
		}
		for (int i=0; i<m; ++i)
		{
			o.insert(g[i]);
		}
		for (int i=0; i<m; ++i)
		{
			set <ld> :: iterator it=o.lower_bound(h[i]);
			if (it!=o.end())
			{
				o.erase(it);
			}
			else
				++w;
		}
		cout<<"Case #"<<ii<<": "<<d<<' '<<w<<endl;
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}