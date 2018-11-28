#include<iostream>
#include<conio.h>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<stack>
#include<queue>
#include<cctype>
#include<iomanip>
using namespace std;
#define sz 10000000
#define ull unsigned long long
int c,d,v;
int ddd[10000];
int demo[1000];
int done=0;
int cre(int x)
{
//	cout<<"part "<<x<<endl;
	if(x==0)
	{
		return 1;
	}
	else if(x<0)
	{
		return 1;
	}
	else
	{
		for(int i=1;i<=v;i++)
		{
			if(demo[i]==0)
			{
				continue;
			}
			if(i>x)
			{
//				cout<<"failded ";
				return 0;
			}
			demo[i]=0;
//			cout<<"rem "<<i<<endl;
			if(cre(x-i)==1)
			{
				demo[i]=1;
				return 1;
			}
			demo[i]=1;
		}
	}
	return 0;
}
void sol()
{
//	for(int i=1;i<=v;i++)
//	{
//		cout<<demo[i]<<" ";
//	}
	for(int x=1;x<=v;x++)
	{
//		cout<<"solving "<<x<<endl;
		if(cre(x)==0)
		{
			return ;
		}
//		cout<<"passed"<<endl;
	}
	done=1;
	return ;
}
void permi(int l)
{
//	cout<<"done "<<done;
	if(done==1)
	{
		return;
	}
	if(l==0)
	{
//		cout<<"added";
		sol();
	}
	else
	{
		if(done==1)
		{
			return;
		}
		for(int i=1;i<=v;i++)
		{
			if(demo[i]==1)
			continue;
			demo[i]=1;
//			cout<<"ad "<<i<<endl;
			permi(l-1);
			demo[i]=0;
			if(done==1)
			{
				return;
			}
		}
	}
}
void solve()
{
	cin>>c>>d>>v;
	for(int i=0;i<=(v+100);i++)
	demo[i]=0;
	for(int i=0;i<d;i++)
	{
		cin>>ddd[i];
		demo[ddd[i]]=1;
	}
	done=0;
	for(int i=0;i<=(v-d);i++)
	{
//		cout<<"i "<<i<<" : ";
		permi(i);
		if(done==1)
		{
			cout<<i;
			return ;
		}
//		cout<<endl;
	}
}
int main()
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}
