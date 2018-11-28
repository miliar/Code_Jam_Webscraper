#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	ll t;
	cin>>t;
	ll p=0;
	while(t--){
		p++;
		string s;
		cin>>s;
		ll i=0;
		ll count=0;
		while(i<s.length())
		{
			if(s[i]=='+')
				i++;
			else
			{
				ll temp=i;
				while(s[i]=='-')
						i++;
				if (temp!=0)
					count+=2;
				else count+=1; 
			}
		}
		cout<<"Case #"<<p<<": "<<count<<endl;
	}
}
