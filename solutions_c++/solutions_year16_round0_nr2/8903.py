#include<bits/stdc++.h>
#define SIZE 100
using namespace std;
int main()
{
	int t,i,j,l,x,z,y,flag;
	char d[101];
	cin>>t;
	for(x=1;x<=t;x++)
	{
		cin>>d;
		l=strlen(d);
		flag=1;
		z=0;
		for(i=0;i<l-1;i++)
		{
			if(d[i]!=d[i+1])
			{
				flag=0;
				break;
			}
		}
		
		if(flag && d[0]=='+' || (l==1 && d[0]=='+'))
		{
			cout<<"Case #"<<x<<": 0"<<endl;		
		}
		else  if(l==1)
                         cout<<"Case #"<<x<<": 1"<<endl;

		else if(flag && d[0]=='-')
			cout<<"Case #"<<x<<": 1"<<endl;

		else
		{
			flag=0;
			while(flag==0)
			{
				flag=1;
				++z;
				for(i=0;i<l-1;i++)
				{
					if(d[i]!=d[i+1])
						break;
				}
				y=i;
				for(i=0;i<=y;i++)
				{
					if(d[i]=='+')
						d[i]='-';
					else
						d[i]='+';
				}
				for(i=0;i<l-1;i++)
		                {
                		        if(d[i]!=d[i+1])
                        		{
                                		flag=0;
                                		break;
                        		}
				}
                	}
		
			if(flag && d[0]=='-')
                        	cout<<"Case #"<<x<<": "<<z+1<<endl;
			else
				cout<<"Case #"<<x<<": "<<z<<endl;	
		}
	}
	return 0;
}	
