#include <bits/stdc++.h>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
	long long int t,i,j,k,l,m,n,o,p,g,b=1;
	cin>>t;
	while(t--)
	{
		p=0,g=0;
		
		string s;
		cin>>s;
		k=s.length();
		
		while(g==0)
		{
			j=-1;
			
			for(i=0;i<k;i++)
			{
				if(s[i]=='-')
				{
				j=i;
				break;
				}
			}
			
			if(j==-1)
			{
				cout<<"Case #"<<b++<<": "<<p<<"\n";
				g=1;
				break;
				
			}
			
			
			for(i=j;i<k;i++)
			{
				if(s[i]=='-' || i==k-1)
				{
					l=i;
					//s[i]='+';
				}
				
				else 
				break;
			}
			
			if(s[0]=='-')
			p++;
			
			else 
			p+=2;
			
			
			
			
			if(l==k-1)
			{
				cout<<"Case #"<<b++<<": "<<p<<"\n";
				g=1;
				break;
			}
			
			else
			{
				for(i=0;i<=l;i++)
				s[i]='+';
			}
			
			
		}
		
	}
}
