#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
	    long long n,r,n2,flag=0;
	    cin>>n;
	    long long c[10]={0};
	    long long n1=n;
	    if(n==0)
	    cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
	    else
	    {
	    for(long long i=1;i<=1000;i++)
	    {
	        n=n1*i;
	        n2=n;
	        while(n>0)
	        {
	           r=n%10;
	           c[r]++;
	           //cout<<r<<" "<<c[r]<<endl;
	           n=n/10;
	        }
	        for(long long j=0;j<10;j++)
	        if(c[j]>=1)
	        { flag++; 
	        //cout<<"value:"<<j<<" "<<c[j]<<" "<<flag<<endl; 
	            
	        } 
	        if(flag==10)
	        goto ch;
	        else flag=0;
	        
	    }
	    ch:
	    cout<<"Case #"<<k<<": "<<n2<<endl;
	    }
	}
	return 0;
}
