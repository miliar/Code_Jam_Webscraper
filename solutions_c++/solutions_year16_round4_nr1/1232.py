#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include<iomanip>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <bitset>
using namespace std;
#define MOD 1000000007
int n,r,p,s;
string re;
string cal(int nn,string ss)
{
	string news;
	int l,i,j;
	while(nn!=n)
	{
		news="";
		l=ss.size();
		for(i=0;i<l;i++)
		{
			if(ss[i]=='P')
				news+="PR";
			else if(ss[i]=='R')
				news+="RS";
			else
				news+="SP";
		}
		ss=news;
		nn++;
	}
	l=ss.size();
	int np=0,ns=0,nr=0;
	for(i=0;i<l;i++)
	{
		if(ss[i]=='P')
			np++;
		else if(ss[i]=='R')
			nr++;
		else
			ns++;
	}
	//cout<<ss<<endl;
	//cout<<np<<' '<<ns<<' '<<nr<<endl;
	if((np!=p)||(ns!=s)||(nr!=r))
		return "";
	string re;
	string s1,s2;
	for(i=1;i<l;i*=2)
	{
		re="";
		for(j=0;j<l;j+=i*2)
		{
			s1=ss.substr(j,i);
			s2=ss.substr(j+i,i);
			if(s1>s2)
			{
				re+=s2;
				re+=s1;
			}
			else
			{
				re+=s1;
				re+=s2;
			}
		}
		ss=re;
	}
	return re;
}
int main(void){
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	std::ios::sync_with_stdio(false);cin.tie(0);
	int t,T;
	string temp;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n>>r>>p>>s;
		re="";
		temp=cal(0,"P");
		if(temp!="")
			re=temp;
		temp=cal(0,"R");
		if(temp!="")
		{
			if(re=="")
				re=temp;
			re=min(re,temp);
		}
		temp=cal(0,"S");
		if(temp!="")
		{
			if(re=="")
				re=temp;
			re=min(re,temp);
		}
		if(re=="")
			re="IMPOSSIBLE";
		cout<<"Case #"<<t<<": "<<re<<'\n';
	}
	system("pause");
	return 0;
}