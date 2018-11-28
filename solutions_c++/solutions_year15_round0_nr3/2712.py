#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
using namespace std;

map<pair<char,char>,pair<char,long long> > M;
char cp[10002],inv[10002],sgn[10002];
long long ii;
string s,s1;

void build()
{
	long long i,j;
	pair<char,long long> val;
	for(i=0;i<=s.size();i++)
	sgn[i]=1;
	cp[0]=s[0];
	for(i=1;i<=s.size();i++)
	{
		val=M[make_pair(cp[i-1],s[i])];
		cp[i]=val.first;
		sgn[i]=val.second;
	}
	for(i=1;i<=s.size();i++)
	sgn[i]=sgn[i]*sgn[i-1];
	for(i=1;i<=s.size();i++)
	if(sgn[i]<0)
	cp[i]=cp[i]-32;
	for(i=0;i<s.size();i++)
	if(cp[i]>=97)
	inv[i]=cp[i]-32;
	else
	inv[i]=cp[i]+32;
}

int main() 
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long T,t,i,j,n,sum,ans,l,sig,m;
	pair<char,long long> val;
	char x,y;
	for(i='i';i<='k';i++)
	{
		M[make_pair('x',i)]=M[make_pair(i,'x')]=make_pair(i,1);
		M[make_pair(i,i)]=make_pair('x',-1);
	}
	M[make_pair('x','x')]=make_pair('x',1);
	
	M[make_pair('i','j')]=make_pair('k',1);
	M[make_pair('i','k')]=make_pair('j',-1);
	
	M[make_pair('j','i')]=make_pair('k',-1);
	M[make_pair('j','k')]=make_pair('i',1);
	
	M[make_pair('k','i')]=make_pair('j',1);
	M[make_pair('k','j')]=make_pair('i',-1);
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>l>>m;
		cin>>s1;
		s.clear();
		sig=1;
		ii=0;
		while(m--)
		s+=s1;
		build();
		/*
		for(i=0;i<s.size();i++)
		cout<<cp[i]<<" ";
		cout<<endl;
		for(i=0;i<s.size();i++)
		cout<<inv[i]<<" ";
		cout<<endl;
		*/
	//	cout<<cp[3]<<" "<<inv[1]<<endl;
		if(cp[s.size()-1]!='X')
		{
			cout<<"Case #"<<t<<": "<<"NO\n";
			continue;
		}
		ii=s.size();
		for(i=0;i<s.size();i++)
		if(cp[i]=='i')
		ii=min(ii,i);
	//	cout<<s.size()<<endl;
		for(i=1;i<s.size()-1;i++)
		if(cp[i]=='k')
		{
		//	cout<<i<<endl;
			x=cp[s.size()-1];y=inv[i];
			if(x<97)
			{sig=-1;x=x+32;}
			if(y<97)
			{sig=sig*(-1);y=y+32;}
			val=M[make_pair(y,x)];
		//	cout<<val.first<<" "<<val.second<<" "<<sig<<"\n";
			if((val.first=='k' && val.second*sig==1)||(val.first=='K' && val.second*sig==-1))
			{
				//cout<<"YO\n";
				if(ii<i)
				{
					cout<<"Case #"<<t<<": "<<"YES\n";
					i=100000;
				}
			}
		}
		
		if(i<100000)
		cout<<"Case #"<<t<<": "<<"NO\n";
	}
	return 0;
}
