#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<set>
#include<map>
#include<queue>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

#define rep(i,k,n) for(int i=(k);i<=(n);i++)
#define rep0(i,n) for(int i=0;i<(n);i++)
#define red(i,k,n) for(int i=(k);i>=(n);i--)
#define sqr(x) ((x)*(x))
#define clr(x,y) memset((x),(y),sizeof(x))
#define pb push_back
#define mod 1000000007
int r,p,s;
string gao(int n,char x)
{
	if(n==1)
	{
		if(x=='R')
		{
			return "RS";
		}
		else if(x=='S')
		{
			return "PS";
		}
		else 
			return "PR";
	}
	string ret="",s1,s2;
	if(x=='R')
	{
		s1=gao(n-1,'R');
		s2=gao(n-1,'S');

	}
	else if(x=='S')
	{
		s1=gao(n-1,'P');
		s2=gao(n-1,'S');
	}
	else
	{
		s1=gao(n-1,'P');
		s2=gao(n-1,'R');
	}
	if(s1<s2)ret=s1+s2;
	else ret=s2+s1;
	return ret;
}

bool check(string ss)
{
	int R=0,S=0,P=0;
	for(int i=0;i<ss.length();i++)
	{
		if(ss[i]=='R')R++;
		if(ss[i]=='S')S++;
		if(ss[i]=='P')P++;
	}
	return R==r && s==S && p==P;
}

void upd(string &x,string y)
{
	if(x.length()==0)x=y;
	else x=min(x,y);
}

int main()
{
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++cas);
		int n;
		scanf("%d%d%d%d",&n,&r,&p,&s);
		string ans="";

		string ss=gao(n,'P');
		if(check(ss))upd(ans,ss);
		
		ss=gao(n,'R');
		if(check(ss))upd(ans,ss);
		
		ss=gao(n,'S');
		if(check(ss))upd(ans,ss);
		
		if(ans.length()==0)puts("IMPOSSIBLE");
		else cout<<ans<<endl;
	}
	
	return 0;
}
