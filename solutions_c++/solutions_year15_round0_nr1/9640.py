#include <iostream>
using namespace std;

int main() {
	int t,n,i,j;
	char s[1001];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		cin>>s;
		int a[1001],ans,count;
		for(i=0;i<=n;i++)
		{
			a[i]=s[i]-48 ;
		}
		count=a[0];ans=0;
		for(i=1;i<=n;i++)
		{
			if(a[i]==0)
			   continue;
			if(count < i)
			{
			   ans+=i-count;
			   count+=a[i]+ans;
			}
			else
			   count+=a[i];
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	// your code goes here
	return 0;
}
