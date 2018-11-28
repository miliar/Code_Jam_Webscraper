#include<iostream>
using namespace std;
int main()
{
	int t,t1,n,i,a,nop,req,count;	
	cin>>t;
	t1=t;
	while(t--)
	{
		nop=req=count=0;		
		cin>>n;
		char s[n+1];
		cin>>s;
		for(i=0;i<=n;i++)
		{
			a=s[i]-48;
			req=i-nop;
			if(req/1>0)
			{
				count=count+req;
				nop=nop+req+a;
			}	
			else
			nop=nop+a;		
		}
		cout<<"Case #"<<t1-t<<": "<<count<<"\n";
	}
}

			
