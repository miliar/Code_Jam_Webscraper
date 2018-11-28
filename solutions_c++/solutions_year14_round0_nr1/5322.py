#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include<set>
#include <map>
#include <time.h>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for(int cas = 1; cas<=t; ++cas)
	{
		int a1,a2;
		cin>>a1;
		set<int> s1,s2;
		for(int i=0; i<4; ++i)
		{
			int a,b,c,d;
			cin>>a>>b>>c>>d;
			if(i == a1-1)
			{
				s1.insert(a);
				s1.insert(b);
				s1.insert(c);
				s1.insert(d);
			}
		}
		cin>>a2;
		vector<int> res;
		for(int i=0; i<4; ++i)
		{
			int a,b,c,d;
			cin>>a>>b>>c>>d;
			if(i!=a2-1)
				continue;
			if(s1.find(a) != s1.end())
				res.push_back(a);
			
			if(s1.find(b) != s1.end())
				res.push_back(b);
			
			if(s1.find(c) != s1.end())
				res.push_back(c);
			
			if(s1.find(d) != s1.end())
				res.push_back(d);
		}
		if(res.size() == 1)
			cout<<"Case #"<<cas<<": "<<res[0]<<'\n';
		if(res.size() == 0)
			cout<<"Case #"<<cas<<": "<<"Volunteer cheated!\n";
		if(res.size() > 1)
		{
			cout<<"Case #"<<cas<<": "<<"Bad magician!\n";
		}
	}
	return 0;
}