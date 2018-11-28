#include<iostream>

using namespace std;

int main()
{
	int t,k=0,i,j;
	cin>>t;
	t;
	int ans=0,ans1,ans2,ans3;
	int a[4][4],b[4][4];
	int c[17]={0};
	while(k<t)
	{
		ans=0;
		for(i=0;i<17;i++)
		c[i]=0;
		cin>>ans1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			c[a[ans1-1][i]]++;
		}
		cin>>ans2;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			c[b[ans2-1][i]]++;
		}
		
		for(i=1;i<17;i++)
		{
			if(c[i]==2 && ans==0)
			{ans++; ans3=i; }
			else if(c[i]==2 && ans == 1)
			ans=-1;
		
		}
		
		if(ans==1)
		{
			cout<<"Case #"<<k+1<<": "<<ans3;
		}
		if(ans==-1)
		{
			cout<<"Case #"<<k+1<<": Bad magician!";
		}
		if(ans==0)
		{
			cout<<"Case #"<<k+1<<": Volunteer cheated!";
		}
		cout<<endl;
		k++;
	}
	return 0;
}
		
