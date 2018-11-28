#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.in","w",stdout);
	int t,k,j,i,n,sum,count;
	char b[1002];
	int a[1002]={0};
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n;
		cin>>b;
		for(i=0;i<n+1;i++)
		a[i]=b[i]-48;
		 sum=0;
		 count=0;
		for(i=0;i<n+1;i++)
		{
			if(i<=sum){
			sum+=a[i];
			//cout<<"i="<<i<<"sum="<<sum<<endl;
			}
			else
			{
				count+=(i-sum);
				sum+=a[i]+(i-sum);
				
			//cout<<"i="<<i<<"sum="<<sum<<endl;
			}
			//cout<<sum<<" and "<<endl;
			
		}
		cout<<"Case #"<<j<<": "<<count<<endl;
		//j++;		
	}
	return 0;
}
