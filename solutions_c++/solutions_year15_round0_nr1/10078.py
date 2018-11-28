#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	long long t,sum,k,req,done,sz,p,t_r;
	char c;
	
	cin>>t;
	c=getchar();
	k=0;
	while(k!=t)
	{	k++;
	    
		cin>>sz;
		c=getchar();
		
		p=0;
		sum=0;
		t_r=0;
		while((c=getchar())!='\n')
		{	
		    if(c==48)
		    req=0;
		    else
		    req=p;
		    
			done=req-sum;
		
			if(done<=0)
			sum+=c-48;
			else
			{	sum+=done+(c-48);
			    t_r+=done;
			}
			
			p++;
		}
		cout<<"Case #"<<k<<": "<<t_r<<endl;
		
	}
	return 0;
}
