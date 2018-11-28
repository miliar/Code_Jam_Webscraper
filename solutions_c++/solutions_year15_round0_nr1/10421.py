#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	ll t,n,i,j,p,count;
	char a[1001];
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		p=0;
		scanf("%s",a);
		count=a[0]-'0';
		p=0;
		for(i=1;i<=n;i++)
		if(count<i)
		{
			p+=i-count;
			count+=i-count;
			count+=a[i]-'0';
			
			
		}
		else
		{
			count+=a[i]-'0';
		}
		printf("Case #%lld: %lld\n",j,p);
		
		
		
	}
	
	return 0;
	
}