#include<iostream>
#include<stack>
#include<map>
#include<utility>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<map>
#include<fstream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<cstring>
using namespace std;
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
int main()
{
    int t,a[100][100];
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
	int n,m;
	bool f[100][100]={0};
	cin>>n>>m;
	map<int,bool> e;
	map<int,bool> :: iterator it;
	for(int i=0;i<n;i++)
	{
	    for(int j=0;j<m;j++)
	    {
		cin>>a[i][j];
		e[a[i][j]]=1;
	    }
	}
	bool flag=0;
	for(it=e.begin();it!=e.end();it++)
	{
	    int cur = (*it).f;
	    for(int i=0;i<n;i++)
	    {
		int c=0;
		for(int j=0;j<m;j++)
		{
		    if(a[i][j]<=cur)
			c++;
		}
		if(c==m)
		{
		    for(int j=0;j<m;j++)
			f[i][j]=1;
		}
	    }
	    for(int j=0;j<m;j++)
	    {
		int c=0;
		for(int i=0;i<n;i++)
		{
		    if(a[i][j]<=cur)
			c++;
		}
		if(c==n)
		{
		    for(int i=0;i<n;i++)
			f[i][j]=1;
		}
	    }
	    for(int i=0;i<n;i++)
	    {
		for(int j=0;j<m;j++)
		{
		    if(a[i][j]<=cur && (!f[i][j]))
		    {
			cout<<"Case #"<<tt<<": "<<"NO"<<endl;
			flag=1;
			break;
		    }
		}
		if(flag)
		    break;
	    }
	    if(flag)
		break;
	}
	if(!flag)
	    cout<<"Case #"<<tt<<": "<<"YES"<<endl;
    }
    return 0;
}
