#include <iostream>
using namespace std;

int main() {
	long long int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		long long int n,total,ans=0,i,temp;
		cin>>n;
		long long int b[n+100];
		char a[n+100];
		cin>>a;
		for(i=0;i<=n;i++)
		{
			b[i]=a[i]-48;
			//cout<<b[i]<<" ";
		}
		//cout<<endl;
		total=b[0];
		for(i=1;i<=n;i++)
		{
			if(total<i)
			{
				ans=ans+(i-total);
				temp=(i-total);
			total=total+b[i]+temp;
			}
			else
			total=total+b[i];
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
		
	}
	// your code goes here
	return 0;
}