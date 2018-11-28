#include <iostream>
using namespace std;

int main() {
	long long int t,j;
	cin>>t;
	
	
	for(j=1;j<=t;j++)
	{
	    long long int n,total=0,i,x,digit;
	    cin>>n;
	    bool hash[10];
	    for(i=0;i<10;i++)
	    hash[i]=0;
	    if(n==0)
	    {
	        cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
	        
	    }
	    else
	    {
    	    for(i=1;;i++)
    	    {
    	      x=i*n;
    	      
    	      while(x)
    	      {
    	        digit=x%10;
    	        x=x/10;
    	        if(hash[digit]==0)
    	        {
    	            hash[digit]=1;
    	            total+=1;
    	        }
    	      }
    	      if(total==10)
    	      break;
    	    }
    	   
	    
	         cout<<"Case #"<<j<<": "<<i*n<<endl;
	    }
	}
}

