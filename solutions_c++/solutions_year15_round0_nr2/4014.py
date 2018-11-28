#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
bool psbl ( int t, vi v)
{
	sort(v.begin(), v.end());
	int n = v.size();
	if(t==1)
	{
		return v[n-1]==1;
	}
	vi u;
	for(int i=0;i<n;i++)
		if(v[i]>1)u.push_back(v[i]-1);
	if(psbl(t-1,u))return 1;
	for(int x=1;x<v[n-1];x++)
	{
		vi u;
		for(int i=0;i<n-1;i++)
			u.push_back(v[i]);
		u.push_back(x);
		u.push_back(v[n-1]-x);
		if(psbl(t-1,u))return 1;
	}
	return 0;
}
int main()
{
	int test;
	cin>>test;
	for(int z=1;z<=test;z++)
	{
		int n;
		cin>>n;
		vi v ;
		for(int i=1;i<=n;i++)
		{
			int x;
			cin>>x;
			v.push_back(x);
		}
		int res = 1000;
		for(int i=1;i<=9;i++)
		{
			if(psbl(i,v)){res=i;break;}
		}
		cout<<"Case #"<<z<<": "<<res<<endl;
	}
}
