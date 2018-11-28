/*
jai shree ram _/\_
A hacker from NITP
*/

#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int,char> msi;
typedef pair<int,int> pa;
typedef long long int ll;

ll x,r,c;
int main()
{
	freopen("dsmall.in", "r", stdin);
  	freopen("dans.out", "w", stdout);
  	int t,p=1;
	cin>>t;
	while(t--)
	{
		cin>>x>>r>>c;
		if((r*c)%x!=0 || max(r,c)<x)
		{
			cout<<"Case #"<<p++<<": "<<"RICHARD\n";
			continue;
		}
		if(x==1 || x==2)
		{
			cout<<"Case #"<<p++<<": "<<"GABRIEL\n";
			continue;
		}
		if(x==3)
		{
			if(r*c==3)
			{
				cout<<"Case #"<<p++<<": "<<"RICHARD\n";
				continue;
			}
			if(r*c==6 || r*c==9 || r*c==12)
			{
			cout<<"Case #"<<p++<<": "<<"GABRIEL\n";
			continue;
			}
		}
		if(x==4)
		{
			if(r*c==4 || r*c==8)
			{
				cout<<"Case #"<<p++<<": "<<"RICHARD\n";
				continue;
			}
			if(r*c==12 || r*c==16)
			{
			cout<<"Case #"<<p++<<": "<<"GABRIEL\n";
			continue;
			}
		}
	}
	return 0;
}


