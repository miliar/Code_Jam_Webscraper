#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int n,m,i,j,temp;
		cin>>n;
		int a[4];
		for(i=0;i<4;i++)
		{	
			for(j=0;j<4;j++)
			{
				if(n==i+1)
					cin>>a[j];
				else
					cin>>temp;
			}
		}
		cin>>m;
		int b[4];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(m==i+1)
					cin>>b[j];
				else
					cin>>temp;
			}
		}
		int count=0,ans=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[i]==b[j])
				{
					ans=a[i];
					count++;
				}
			}
		}

		if(count==1)
			cout<<"Case #"<<k<<": "<<ans<<endl;
		else if(count>1)
			cout<<"Case #"<<k<<": Bad magician!"<<endl;
		else if(count==0)
			cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
	}
}