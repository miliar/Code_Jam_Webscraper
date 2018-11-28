#include <iostream>
using namespace std;

int main() {
	int t=0;
	cin>>t;
	int i=0;
	for(i=0;i<t;i++)
	{
		int n=0;
		cin>>n;
	
		int j=0;
		char a[10];
		int b[10];
		
		 	cin>>a;
	
		int sum=0;
		int flag=0;
		for(j=0;j<=n;j++)
		{
			b[j]=a[j]-48;
		
		}
	    for(j=0;j<=n;j++)
	    {
	    	sum=sum+b[j];
	    	if(sum<(j+1))
	    	{
	    		b[j]+=1;
	    		sum+=1;
	    		flag++;
	    	}
	    }
		cout<<"Case #"<<(i+1)<<": "<<flag<<"\n";
	}
	
	return 0;
}