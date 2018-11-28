#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,n,i,r,last,j,m,x;
	int arr[10];
	cin>>t;
	for(x=1;x<=t;x++)
	{
		cin>>n;
		if(n==0)
		cout<<"Case #"<<x<<": INSOMNIA"<<endl;
		else
		{
			for(i=0;i<10;i++)
		arr[i]=0;
		j=1;
		while(1)
		{
			m=n*j;
			last=n*j;
			while(m>0)
			{
				r=m%10;
				m=m/10;
				if(arr[r]==0)
				arr[r]++;
			}
			j++;
			int flag=0;
			for(i=0;i<10;i++)
			{
				if(arr[i]==0)
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				cout<<"Case #"<<x<<": ";
				cout<<last<<endl;
				break;
			}
		}
		
	}
		}
}
