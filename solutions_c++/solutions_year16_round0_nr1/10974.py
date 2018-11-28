#include <iostream>
using namespace std;

int main() {
	// your code goes here
	bool hell[10];
long long	int t,n,count,temp,x=1,temp1,i;
	cin>>t;
	while(x<=t)
	{
	 for(i=0;i<10;i++)
	 hell[i]=0;
	    count=0;
	    cin>>n;
	    if(n==0)
	    {
	        cout<<"Case "<<"#"<<x<<": "<<"INSOMNIA"<<endl;
	    }
	    else{
	    temp=n;
	    while(count<10)
	    {
	        temp1=temp;
	         
	        while(temp1/10!=0)
	        {
	           
	            if(hell[temp1%10]==0)
	            {
	                hell[temp1%10]=1;
	                count++;
	            }
	            temp1=temp1/10;
	        }
	       if(temp1/10==0 && hell[temp1%10]==0)
	       {
	        hell[temp1%10]=1;
	        count++;
	       }
	           
	        if(count==10)
	        {
	        cout<<"Case "<<"#"<<x<<": "<<temp<<endl;
	        break;
             }
	        temp=temp+n;
	    }
	    }
	    x++;
	}
	return 0;
}
