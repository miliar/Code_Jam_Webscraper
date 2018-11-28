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

void solve() 
{
	int n;
	cin>>n;
	for (int ii=0; ii<n; ++ii)
	{
		int a;
		cin>>a;
		--a;
		vector <vector <int> > h(4,vector <int> (4));
		for (int i=0; i<4; ++i)
			for (int j=0; j<4; ++j)
				cin>>h[i][j];
		int b;
		cin>>b;
		--b;
		vector <vector <int> > g(4,vector <int> (4));
		for (int i=0; i<4; ++i)
			for (int j=0; j<4; ++j)
				cin>>g[i][j];
		int ans=0;
		int res;
		for (int i=0; i<4; ++i)
		{
			for (int j=0; j<4; ++j)
				if (h[a][i]==g[b][j]) 
				{
					++ans;
					res=h[a][i];
				}
		}
		cout<<"Case #"<<ii+1<<": ";
		if (!ans)
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		if (ans==1)
		{
			cout<<res<<endl;
		}
		if (ans>1)
		{
			cout<<"Bad magician!"<<endl;
		}
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}