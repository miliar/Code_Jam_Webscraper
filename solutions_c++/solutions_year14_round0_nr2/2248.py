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
		ld c,f,x,v=2,s=0,t=0;
		cin>>c>>f>>x;
		while (1)
		{
			if ((x-s)/v<x/(v+f))
			{
				t+=(x-s)/v;
				break;
			}
			if (s==0)
			{
				s=c;
				t+=c/v;
			}
			else
			{
				v+=f;
				s=0;
			}

		}
		cout<<fixed<<setprecision(7)<<"Case #"<<ii<<": "<<t<<endl;
	}
}

int main()
{
	prepare("");
	solve();
	return 0;
}