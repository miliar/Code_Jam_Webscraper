#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,n,j,a,i;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int ipl[3001];
		for(i=0;i<=3000;i++)
		{
			ipl[i]=0;
		}
		cin>>n;
		for(i=0;i<(2*n-1);i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>a;
				ipl[a]++;
			}
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<=3000;i++)
		{
			if(ipl[i]%2==1)
			{
				cout<<i<<" ";
			}
 
		}
		cout<<endl;
	}
 
}