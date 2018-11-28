#include<iostream>
#include<string>
using namespace std;
int aa[1001];
int main()
{
	int i1=0,t;
	cin>>t;
	while( (++i1) <=t)
	{
		int ans=0,i,j,k,l,m,n,sum=0;
		cin>>n;
		for(i=0;i<=n;i++)
		{
			char ch;
			cin>>ch;
			j=ch-'0';
			ans=max(i-sum,ans);
			sum=sum+j;
		}
		aa[i1]=ans;
	}
	for(i1=1;i1<=t;i1++)
	cout<<"Case #"<<i1<<": "<<aa[i1]<<endl;
}
