#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int arr[5][5],brr[5][5],f,s,k,i,j,ans,flag[17],count,test;
	cin>>test;
	for(k=1;k<=test;k++)
	{
		memset(flag,0,sizeof flag);
		count=0;
		cin>>f;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>arr[i][j];
			}
		}
		for(j=1;j<=4;j++)
		{
			flag[arr[f][j]]=1;
		}
		cin>>s;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>brr[i][j];
			}
		}
		for(j=1;j<=4;j++)
		{
			if(flag[brr[s][j]]==1)
			{
				ans=brr[s][j];
				count++;
			}
				
		}
		if(count==1)
		{
			cout<<"Case #"<<k<<": "<<ans<<endl;
		}
		else if(count>1)
		{
			cout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
		}
			
	}
	return 0;
}