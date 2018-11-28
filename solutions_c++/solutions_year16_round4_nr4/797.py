#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int a[4][4],b[4][4],c[4];
int n;
int fnnn()
{
	int i,j,k;
	int d[4];
	for(i=0;i<n;i++)d[i]=1;
	for(i=0;i<n;i++)
	{
		if(b[i][c[i]])d[c[i]]=0;
	}
	for(i=0;i<n;i++)
	{
		if(!b[i][c[i]])
		{
			for(j=0;j<n;j++)
			{
				if(b[i][j]&&d[j])break;
			}
			if(j==n)return 1;
		}
	}
	return 0;
}
int fnn(int p)
{
	int i,j,k;
	if(p==n)
	{
		if(fnnn())return 1;
		return 0;
	}
	for(i=p;i<n;i++)
	{
		k=c[i];
		c[i]=c[p];
		c[p]=k;
		if(fnn(p+1))return 1;
		k=c[i];
		c[i]=c[p];
		c[p]=k;
	}
	return 0;
}
int fn()
{
	int i,j,k;
	for(i=0;i<n;i++)c[i]=i;
	if(!fnn(0))return 1;
	return 0;
}
int fun(int r,int c,int m)
{
	if(m==0)return fn();
	if(c==n)
	{
		r++;
		c=0;
	}
	if(r>=n)return fn();
	if(b[r][c])return fun(r,c+1,m);
	if(fun(r,c+1,m))return 1;
	b[r][c]=1;
	int k=fun(r,c+1,m-1);
	b[r][c]=0;
	return k;
}
int main()
{
	int t,i,j,k,cs,css;
	char s[10];
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>s;
			for(j=0;j<n;j++)
			{
				a[i][j]=s[j]-'0';
			}
		}
		cout<<"Case #"<<cs<<": ";
		for(i=0;i<=16;i++)
		{
			for(j=0;j<n;j++)for(k=0;k<n;k++)b[j][k]=a[j][k];
			if(fun(0,0,i))break;
		}
		cout<<i<<endl;
	}
	return 0;
}
