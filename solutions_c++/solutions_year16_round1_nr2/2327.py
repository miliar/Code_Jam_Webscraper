#include<bits/stdc++.h>
#define ll long long 

using namespace std;
ll  a[4000];
int main()
{
	
	ll t,k=1,i,n,j,x;
	cin>>t;
	
	while(t--)
	{

		for(i=0;i<4000;i++)
		a[i]=0;
		cin>>n;
		for(i=0;i<(2*n-1);i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>x;
				a[x]++;
			}
		}
		cout<<"Case #"<<k<<": ";
		
		for(j=0;j<=4000;j++)
		{
			
			if(a[j]%2==1)
			{
				cout<<j<<" ";
			}
 
		}
		k++;
		cout<<endl;
	}
 return 0;}
