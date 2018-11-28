#include<iostream>
#include<bits/stdc++.h>
#define ll long long
#define st string
using namespace std;
int main()
{
	int t,g=0;
	cin>>t;
	while(t--)
	{
		g++;
		ll x,ans=0;
		cin>>x;
		st s;
		cin>>s;
		
		ll check=0;
		check = s[0]-48;
		
		for(int i=1;i<s.size();i++)
		{
			if(i>check)
			{
				
				ans = ans+i-check;
				check = i;
			}
			
			check+=s[i]-48;
			
		}
		cout<<"Case #"<<g<<": "<<ans<<endl;
	}
}
