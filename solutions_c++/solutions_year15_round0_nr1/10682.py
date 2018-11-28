#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		int n;
		cin>>n;
		int a[n+1];
		char c;
		for(int i=0;i<=n;i++)
		{
			cin>>c;
			a[i]=c-'0';
		}
		
		int sum=0,ans=0;
		for(int i=0;i<=n;i++)
		{
			if(sum < i && a[i]!=0)
			{
				ans+=(i-sum);
				sum=i+a[i];
			}
			else	sum+=a[i];
		}
		
		cout<<"Case #"<<(j+1)<<": "<<ans<<endl;
	}
	return 0;
}