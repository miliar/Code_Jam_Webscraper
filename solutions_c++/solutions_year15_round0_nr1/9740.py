#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int t,i,n,j,z;
	string s;
	cin>>t;
	     for(z=1;z<=t;z++)
		{
			
			cin>>n;
			cin>>s;
			
			long long int a[n];
			
			long long int sum=0,count=0;
			
			for(i=0;i<n;i++)
			{
				sum=sum+(s[i]-48);
				a[i]=sum;
				
			}
			
			for(i=1;i<=n;i++)
			{
				if(a[(i-1)]<i)
				{
					sum=(i-a[i-1]);
					count=count+sum;
					for(j=i;j<n;j++)
					a[j]=a[j]+sum;
				}
			}
			
			cout<<"Case"<<" "<<"#"<<z<<":"<<" "<<count<<endl;
			
		}
	return 0;
}