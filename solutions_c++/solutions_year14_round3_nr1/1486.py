#include<bits/stdc++.h>
using namespace std;
#define i64 long long

/* Recursive Standard C Function: Greatest Common Divisor */
i64 gcd ( i64 a, i64 b )
{
  if ( a==0 ) return b;
  return gcd ( b%a, a );
}

int main()
{
	freopen("A-large.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	i64 tt,t,p,q,i;
	cin>>t;
	tt=0;
	string pq;
	while(t--)
	{
		tt++;
		cin>>pq;
		
		p=0;
		for(i=0;;i++)
		{
			if(pq[i]=='/')
			 break;
			
			else
			p=(p*10+(pq[i]-'0'));
		}
		
		q=0;
		i=i+1;
		
		for(;i<pq.length();i++)
		{
			
			q=(q*10+(pq[i]-'0'));
		}
			 
		i64 fac=gcd(p,q);
		p=p/fac;
		q=q/fac;	 
		
		cout<<"Case #"<<tt<<": ";
		
		if((long double)p /(long double)q> 1.0 )
		{
			cout<<"impossible"<<endl;
			
		}
		
		else
		{
			i64 gen=0,flag=0;
			
			for(i=1;i<=q;i*=2)
			{
				if(q==i)
				 flag=1;
			}
			
			if(flag==0)
			{ 
			 cout<<"impossible"<<endl;	 
			 	
			}
			
			
			else
			{ 
				//cout<<(double)p/(double)q<<" ";
				while( (long double)p/(long double)q <1.0)
				{
                   p=p*2;
                   gen++;
                   
                }  					
				 
				 cout<<gen<<endl;
				
		    }
			
		
		
		}		
	 }
	 
	 return 0;
}	 		
