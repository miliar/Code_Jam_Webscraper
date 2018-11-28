
#include<iostream>
using namespace std;

int main()
{
	int t,i,j,n,x,b=1,l,c;
	char a[102];
	cin>>t;
	while(t--)
	{
		c=0;
		cin>>a;
		for(i=0;(a[i]=='-')||(a[i]=='+') ; i++) ;
		l=i;
		a[l]=3;
		//cout<<l;
			
		cout<<"Case #"<<b<<": ";
		//cout<<a;

		
		i=0;
		while(a[i]=='-')
		{
			i++;
		}
		if(i==l)
		{
			cout<<1<<endl;
			b++;
			continue;
		}
		
		i=0;
		while(a[i]=='+')
		{
			i++;
		}
		if(i==l)
		{
			cout<<0<<endl;
			b++;
			continue;
		}
		
		
		for(i=0;i<(l-1);)
		{
			if((a[i]=='-')&&(a[i+1]=='+'))
			{
				c++;
				i=i+1;
				continue;
			}
				
			if((a[i]=='+')&&(a[i+1]=='-'))
			{	
				c=c+2;
				j=i+1;
				while(a[j]=='-')
				{
					j++;
				}
				i=j;
				continue;
			}
			i++;
			
		}
		cout<<c<<endl;
		
		
		
		
		
		
		
		b++;
	}
	return 0;
	
}
