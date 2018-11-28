#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int count(vector<int> p,int move)
{
	if(p[p.size()-1] < 4)
	{
		return move+p[p.size()-1];
	}
	int a = 1000000;
	vector<int> c = p;
	for (int i = 1; i <= p[p.size()-1]/2; ++i)
	{
		if(i > 1)
		{
			int x = min(i,p[p.size()-1]-i);
			int y = max(i,p[p.size()-1]-i);
			p.pop_back();
			p.push_back(x);
			p.push_back(y);
			sort(p.begin(),p.end());
		}
		else {for (int j = 0; j < p.size(); ++j)if(p[j] > 0)p[j]--;}
		a = min(a,count(p,move+1));
		p = c;
	}
	return a;
}

int main()
{
	freopen("B-small-attempt3.in","r",stdin);
	freopen("Output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; ++i)
	{
		vector<int> p;
		int d;
		scanf("%d",&d);
		for (int j = 0; j < d; ++j)
		{
			int dummy;
			scanf("%d",&dummy);
			p.push_back(dummy);
		}
		sort(p.begin(),p.end());
		int maks = p[p.size()-1];
		printf("Case #%d: %d\n",i+1,min(maks,count(p,0)));
	}
	return 0;
}