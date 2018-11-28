#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


int check(string s)
{
	for(int i=0;i<s.size();i++)
	{
		if(s[i]=='-') return 0;
	}
	return 1;
}

ll fun(string s)
{
	ll count=0;
	while(check(s)==0) 
	{
		count++;
		if(s.size()==1) return count;
		char ch=s[0];
		int i=0;
		for(i=1;i<s.size();i++)
		{
			if(ch!=s[i])
			{
				break;
			}
		}
		i--;
		for(ll j=0;j<=i/2;j++)
		{
			char temp=s[j];
			s[j]=s[i-j]=='+'? '-':'+';
			s[i-j]=temp=='+'? '-':'+';
		}		
	}
	return count;
}
	



int main()
{
	ll t;
	cin>>t;
	for(ll tt=1;tt<=t;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		string s;
		cin>>s;
		cout<<fun(s)<<endl;
	}
	return 0;
}
