#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;


typedef long long ll;
ll cnt = 0;
double eps = 1e-9;
const ll mod = 1e9+7;

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	

	ll test;
	cin>>test;
	for(ll testcase = 0; testcase<test; ++testcase)
	{
		int n;
		cin>>n;
		vector<string> v(n);
		for(int i=0; i<n; ++i)
		{
			cin>>v[i];
			for(int j=0; j<v[i].size(); ++j)
				v[i][j]-='a';
		}
		for(int i=0; i<n; ++i)
		{
			string tmp;
			tmp+=v[i][0];
			for(int j=1; j<v[i].size(); ++j)
			{
				if(v[i][j]!=tmp[tmp.size()-1])
					tmp+=v[i][j];
			}
			v[i] = tmp;
		}
		vector<int> per(n);
		for(int i=0; i<n; ++i)
		{
			per[i] = i;
		}
		ll res = 0;

		bool fl = 0;
		string tmp;
		for(int i=0; i<n; ++i)
		{
			tmp+=v[per[i]];
		}
		vector<int> used(30,0);
		int ptr = 0;
		while(ptr<tmp.size())
		{
			if(used[tmp[ptr]] == true)
			{
				fl = 1;
				break;
			}
			used[tmp[ptr]] = true;
			int c = tmp[ptr];
			while(ptr < tmp.size() && tmp[ptr] == c)
				ptr++;
		}
		if(fl == 0)
			res++;
		
		while(next_permutation(per.begin(), per.end()))
		{
			bool fl = 0;
			string tmp;
			for(int i=0; i<n; ++i)
			{
				tmp+=v[per[i]];
			}
			used.assign(30,0);
			int ptr = 0;
			while(ptr<tmp.size())
			{
				if(used[tmp[ptr]] == true)
				{
					fl = 1;
					break;
				}
				used[tmp[ptr]] = true;
				int c = tmp[ptr];
				while(ptr < tmp.size() && tmp[ptr] == c)
					ptr++;
			}
			if(fl == 0)
				res++;
			if(res >= mod)
				res-=mod;
		}

		cout<<"Case #"<<(testcase+1)<<": ";
		cout<<res;
		cout<<"\n";
	}
	return 0;
}