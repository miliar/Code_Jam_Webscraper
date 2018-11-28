#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,i,l,k,c;
	
	//freopen("1.txt","r",stdin);
    //freopen("3.txt","w",stdout);
    cin>>t;
	string s;
	for(k=1;k<=t;k++)
	{
		c=0;
		cin>>s;
		l=s.size();
		if(l==1)
		{
			if(s[0]=='+')
			cout<<"Case #"<<k<<": "<<0<<endl;
			else if(s[0]=='-')
			cout<<"Case #"<<k<<": "<<1<<endl;
		}
		else
		{
			for(i=0;i<(l-1);i++)
			{
				if(s[i]!=s[i+1])
				{
					c++;
				}
			}
			if(s[i]=='-')
			c++;
			cout<<"Case #"<<k<<": "<<c<<endl;
		}
		
	}
}
