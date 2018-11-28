#include<bits/stdc++.h>

using namespace std;
#define ll long long 

ll comp(ll i, ll b)
{
	ll n =0,temp=1;
	while(i>0)
	{
		n=n+ temp*(i%10);
		i=i/10;
		temp=temp*b;
	}
	
   for(ll j=2;j*j<=n;j++)
   {
   	if( n%j ==0)return j;
	   }
	   	
	return 0;
}

int main()
{ 
   freopen("C-small-attempt0.in","r",stdin);
  freopen("output_3.txt","w",stdout);	 
	 ll t,n,j,i;
	 cin>>t;
	  for(int z=1;z<=t;z++)
	 { 
	   cout<<"Case #"<<z<<": "<<endl;
	    cin>>n>>j;
	   ll start=(1<<(n-1)) +1,count=0;
	   ll a[12],sum=0;
	   
	    
	    while(sum<j)
	    {  i=0,count=0;
	      
	    	ll k= start,temp=1;
	    	while(k>0)
	    	{
	    		i=i +temp*(k%2);
	    		k=k/2;
	    		temp=temp*10;	    		
			}
			//cout<<i<<endl;
			//cout<<"here2"<<endl;
	    	count=0;
	    	for(int p=2;p<11;p++)
	    	{
	    		temp=comp(i,p);
	    		//cout<<temp<<endl;
	    		if(temp==0){p=15;break;
				}
	    		else
	    		{
	    			count++;
	    			a[p]=temp;
				}
			}
			//cout<<"here"<<endl;
			if(count==9)
			{	sum++;
			   cout<<i<<"\t";
			   for(int q=2;q<=10;q++)
			     cout<<a[q]<<"\t";
			     
			     cout<<endl;
				
			}
	    	start=start+2;
	    	
		}	   
	 	
	  } 
}
