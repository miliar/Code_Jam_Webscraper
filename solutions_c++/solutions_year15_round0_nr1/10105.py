#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int g=1;g<=t;g++)
	{
		int n,sum=0,ans=0;char a[1002];int b[1001];
		cin>>n;
		cin>>a;
		for(int i=0;i<=n;i++)
			b[i]=a[i]-'0';
		sum+=b[0];
		for(int i=1;i<=n;i++)
		{
			if(sum<i&&b[i]!=0){ans+=(i-sum);sum+=ans;}
			sum+=b[i];
		}
		cout<<"Case #"<<g<<": "<<ans<<endl;
	}
	return 0;
}
