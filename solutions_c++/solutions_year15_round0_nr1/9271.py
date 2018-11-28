#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
	int t;
	int l=1;
	scanf("%d",&t);
	while(t--)
	{
		int s;
		scanf("%d",&s);
		char b[s+1];
		cin>>b;
		int a[s+1];
		for(int i=0;i<=s;++i)
		{
			a[i]=b[i]-'0';
		}
		ll count=0;
		ll sum=0;
		for(int i=0;i<=s;++i)
		{
			if(sum>=i)
			sum+=a[i];
			else if(a[i]!=0)
			{
				count+=(i-sum);
				sum+=a[i]+i-sum;
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
		l++;
	}
	return 0;
}
