#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int n,t,i,a[11]={0},ans,temp;
	cin>>t;
	for(int k=1;k<=t;k++)
	{    for(int j=0;j<=9;j++)
	             a[j]=0;
	    int f=0;
	     int i=1;
	     cin>>n;
	    if(n==0)
	       cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
	   else {    
	    while(f==0)
	    {    
	        ans=i*n;
	        temp=ans;
	        while(ans!=0)
	        {
	            a[ans%10]++;
	          //  cout<<ans%10<<endl;
	            ans/=10;
	        }
	        
	        for(int j=0;j<=9;j++)
	        {
	            if(a[j]==0)
	               {f=0; break;
	               }
	           else 
	             f=1;
	        }
	          
	        //cout<<temp<<endl;
	       i++; 
	    }
	    cout<<"Case #"<<k<<": "<<temp<<endl;
	    
	    
	   }
	}
	
	
	
	
	return 0;
}
