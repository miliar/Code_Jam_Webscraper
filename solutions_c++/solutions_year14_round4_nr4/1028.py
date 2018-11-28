#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <iomanip>
#include <string>
#include <string.h>
#include <cstdlib>
#include <bitset>
#include <cmath>

#define X first
#define Y second
#define ll long long
#define mp make_pair
#define pb push_back

using namespace std;


string a[11];
int n, m;
int wh[20];
int ans=0, mx=0;
int check()
{
	/*for (int i=1; i<=m; i++)
		cout<<wh[i]<<" ";
	cout<<endl;
	cout<<"--"<<endl;*/
	set<string>s[11];
	for (int i=1; i<=m; i++)
	{
		string h="";
		for (int j=0; j<a[i].length(); j++)
		{
			h+=a[i][j], s[wh[i]].insert(h);
			//cout<<h<<endl;
		}
	}
	int sum=0;
	for (int i=1; i<=n; i++)
	{
		//cout<<s[i].size()<<" ";
		sum+=s[i].size();
		if ( s[i].empty() ) sum=-(1<<20);
	}
	//cout<<endl;
	return sum+n;
}
void rec(int t)
{
	if ( t==m+1 )
	{
		int res=check();
		if ( res==mx ) ans++;
		if ( res>mx ) mx=res, ans=1;
	}
	else
	{
		for (int i=1; i<=n; i++)
			wh[t]=i, rec(t+1);
	}
}
int solve()
{
	mx=0; ans=0;
	cin>>m>>n;
	for (int i=1; i<=m; i++)
		cin>>a[i];
	rec(1);
	cout<<mx<<" "<<ans<<endl;
}
int main()
{	
	freopen("dsmall.in", "r", stdin);
	freopen("dsmall.out", "w", stdout);
	int test;
	cin>>test;
	for (int i=1; i<=test; i++)
		printf("Case #%d: ", i), solve();
	return 0;    
}

