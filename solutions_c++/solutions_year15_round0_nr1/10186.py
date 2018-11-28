#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		char str[1100];
		int a[1100];
		int s,c=0,sum=0;
		cin>>s;
		cin>>str;
		for(int i=0;i<=s;i++)
		a[i]=str[i]-48;
		//cout<<a[0];
		//cout<<str;
		for(int i=0;i<=s;i++)
		{
        //cout<<a[i];		
		if(i==0)
		{
		sum=sum+a[0];
		
		//continue;
		}
		else
		{
			
		if(a[i]!=0)
		{
			
			if(sum<i)
			{
				//cout<<"Se";
				
				int y=i-sum;
				c=c+y;
			    sum=sum+y+a[i];
			}
			else
		{
			sum=sum+a[i];
		}
		}
		
		}
		}
	cout<<"Case #"<<j<<": "<<c<<"\n";	
	}
	// your code goes here
	return 0;
}
