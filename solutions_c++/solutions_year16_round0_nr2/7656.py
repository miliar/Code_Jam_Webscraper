#include <bits/stdc++.h>
using namespace std;
 
int main()
{
	long int x,l,ans=0,k,t,m,y;
	string s;
	char c,d;
	cin>>t;
 
	for(x=1;x<=t;x++)
	{
		cin>>s;
		ans=0;
 
		k=0;
 
		l=s.size();
 
		if(l==1)
		{
			if(s[0]=='+')
			ans=0;
			else
			ans=1;
		}
		else
		{
		while(k<=l-2)
		{
			c=s[k];
			d=s[k+1];
			if(c!=d)
			{
				if(d=='+'){
				ans=ans+1;}
				else{
				ans=ans+2;}
				m=0;
				for(y=k+1;y<=l-2;y++)
				{
					if(s[y]==s[y+1])
					m++;
					else 
					break;
				}
 				k=k+m;
				s[k+1]='+';
 
 				if(s[y]=='-')
 				ans=ans+2;
			}
			
			k++;
		}
		}
		if(ans == 0 && s[0]=='-')
		ans=1;
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
	}