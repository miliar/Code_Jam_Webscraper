#include<bits/stdc++.h>
using namespace std;
int main()
{
	 
	 int t;
	 unsigned long long temp,i,n;
	 cin>>t;
	 int bitmask,j;
	 j=t;
	 while(t--)
	  {
                  //n=t;
	  	 cin>>n;
	  	 //n=t;
	  	 if(n==0)
	  	  cout<<"Case #"<<j-t<<": "<<"INSOMNIA\n";
	  	 else
	  	 {
		   bitmask=0;
		   unsigned long long i=1;
	  	   while(1)
	  	  {	
	  	    	if(bitmask==1023)
	  	    	  {
					break;
				  }
	  	        temp=n*i;
	  	        while(temp>0)
	  	         {
	  	            bitmask=bitmask|(1<<(temp%10));
				    temp=temp/10;	
				 }
			    i++;
			    //cout<<bitmask<<endl;
		  }
		  cout<<"Case #"<<j-t<<": "<<n*(i-1)<<endl;
	    }
	  }
	 return 0;	 
}