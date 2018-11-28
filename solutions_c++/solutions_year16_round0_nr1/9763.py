#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    long long int n,m,j=1,ans,count=0,a[10]={0};
	    cin>>n;
	    if(n==0)
	   cout<<"Case #"<<i<<": INSOMNIA"<<"\n";
	    else
	    {
	        while(count!=10){
	        m=j*n;ans=j*n;
	        while(m!=0)
	        {
	            int mod=m%10;
	            if(a[mod]==0)
	            {
	            a[mod]=1;
	            count++;
	            }
	            m=m/10;
	        }
	        j++;
	       }
	       cout<<"Case #"<<i<<": "<<ans<<"\n";
	    }
	    
	}
	return 0;
}
