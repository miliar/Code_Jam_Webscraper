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
int R,P,S,N;
char s[10];
int fn(int l)
{
	int i,j,k=l;
	char ss[10];
	for(i=0;i<l;i++)ss[i]=s[i];
	ss[l]='\0';
	s[l]='\0';
//	cout<<s<<endl;
	for(k=0;k<N;k++)
	{
		for(i=0,j=0;i<l;i+=2,j++)
		{
			if(ss[i]==ss[i+1])return 0;
			if(ss[i]=='P')
			{
				if(ss[i+1]=='R')ss[j]='P';
				else ss[j]='S';
			}
			else if(ss[i]=='R')
			{
				if(ss[i+1]=='P')ss[j]='P';
				else ss[j]='R';
			}
			else
			{
				if(ss[i+1]=='P')ss[j]='S';
				else ss[j]='R';
			}
		}
		l/=2;
	}
	return 1;
}
int fun(int p,int r,int ss,int c)
{
//	cout<<p<<r<<ss<<endl;
	if((p+r+ss)==0)
	{
		return fn(c);
	}
	if(p)
	{
		s[c]='P';
		if(fun(p-1,r,ss,c+1))return 1;
	}
	if(r)
	{
		s[c]='R';
		if(fun(p,r-1,ss,c+1))return 1;
	}
	if(ss)
	{
		s[c]='S';
		if(fun(p,r,ss-1,c+1))return 1;
	}	
	return 0;
}
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>N>>R>>P>>S;
		cout<<"Case #"<<cs<<": ";
		if(fun(P,R,S,0))
		{
			cout<<s<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}
