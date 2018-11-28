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


int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin>>test;
	for(int testcase = 0; testcase<test; ++testcase)
	{

		int n;
		cin>>n;
		vector<string> v(n);
		vector<string> vv(n);
		int cnt=0;
		for(int i=0; i<n; ++i)
		{
			cin>>v[i];
			vv[i]=v[i][0];
			for(int j=1; j<v[i].size(); ++j)
			{
				if(v[i][j]!=v[i][j-1])
					vv[i]+=v[i][j];
				else
					cnt++;
			}
		}
		bool wrong=0;
		for(int i=1; i<n; ++i)
		{
			if(vv[i] != vv[i-1])
			{
				wrong = 1;
				break;
			}
		}
		if(wrong)
		{
			cout<<"Case #"<<(testcase+1)<<": ";
			cout<<"Fegla Won";
			cout<<"\n";
			continue;
		}
		int sz = vv[0].size();
		vector<int> ptr(n,1);
		vector<int> count(n,0);
		int res = 0;
		for(int i=0; i<sz; ++i)
		{
			count.assign(n,0);
			int mid = 0;
			for(int j=0; j<n; ++j)
			{
				while(ptr[j] < v[j].size() && v[j][ptr[j]] == v[j][ptr[j]-1])
				{
					count[j]++;
					ptr[j]++;
				}
				count[j]++;
				ptr[j]++;
				mid+=count[j];
			}
			mid = floor(((double)mid/n+0.5));
			for(int j=0; j<n; ++j)
			{
				res+=abs(mid-count[j]);
			}
		}

		cout<<"Case #"<<(testcase+1)<<": ";
		cout<<res;
		cout<<"\n";
	}

	return 0;
}