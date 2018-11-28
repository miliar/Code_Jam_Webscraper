#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<queue>
using namespace std;
typedef long long LL;
const double pi=acos(-1.0);
int n,m;
int a[100][100];
bool haslarge(int x,int y)
{
	bool heng=false,shu=false;
	for(int i=0;i<n;i++)
	{
		if(a[i][y]>a[x][y]) heng=true;
	}
	for(int i=0;i<m;i++)
	{
		if(a[x][i]>a[x][y]) shu=true;
	}
	return heng && shu;
}
bool work()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(haslarge(i,j)) return false;
		}
	}
	return true;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		cin>>n>>m;
		for(int i=0;i<n;i++)for(int j=0;j<m;j++)cin>>a[i][j];
		if(work()) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	fclose(stdout);
	return 0;
}
