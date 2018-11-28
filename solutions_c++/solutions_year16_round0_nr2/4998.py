#include<iostream>
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	ll t,cas=0;
	cin>>t;
	while(t--)
	{ cas++;
		string s;ll c=0;
		cin>>s;
		for(ll i=0;i<s.length()-1;i++){
			if(s[i]!=s[i+1])c++;
		}
		if(s[s.length()-1]=='-')c++;
		cout<<"Case #"<<cas<<": "<<c<<endl;
	}
}
