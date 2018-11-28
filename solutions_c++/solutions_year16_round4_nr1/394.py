#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;
string str,ans;
int n,r,p,s,T;
string pd(char ch,int i)
{
	int rr,pp,ss;
	if (i==1)
	{
		if (ch=='P')
			return "PR";
		if (ch=='R')
			return "RS";
		if (ch=='S')
			return "PS";
	}
	string l="";
	string r="";
	if (ch=='P')
	{
		l=pd('P',i-1);
		r=pd('R',i-1);
	}
	if (ch=='R')
	{
		l=pd('R',i-1);
		r=pd('S',i-1);
	}
	if (ch=='S')
	{
		l=pd('P',i-1);
		r=pd('S',i-1);
	}
	if (l>r)
		return r+l;
	else
		return l+r;
}
bool count(string q)
{
	int rr,ss,pp;
	rr=0;
	ss=0;
	pp=0;
	for(int i=0;i<q.size();i++)
	{
		if (q[i]=='R')
			rr++;
		if (q[i]=='S')
			ss++;
		if (q[i]=='P')
			pp++;
	}
	if (rr==r && ss==s && pp==p)
		return true;
	return false;
}
int main()
{
	freopen("t.in","r",stdin);
	freopen("t.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d %d %d %d",&n,&r,&p,&s);
		printf("Case #%d: ",tt);
		ans="ZZZZZZ";
		str=pd('P',n);
		if (count(str))
			if (str<ans)
				ans=str;
		str=pd('R',n);
		if (count(str))
				if (str<ans)
					ans=str;
		str=pd('S',n);
		if (count(str))
				if (str<ans)					
					ans=str;
			if (ans!="ZZZZZZ")
				cout<<ans<<endl;
			else
				cout<<"IMPOSSIBLE"<<endl;

	}
}