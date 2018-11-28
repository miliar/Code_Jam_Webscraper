#include <iostream>
using namespace std;

int main() {
	int t,i,j,u,a1,a2,ans,count,temp,z[20],y[20];
	cin>>t;
	for(u=1;u<=t;u++)
	{
		for(i=0;i<20;i++)
		{
			z[i]=0;
			y[i]=0;
		}
		count=0;
		cin>>a1;
		for(i=0;i<4;i++)
		{
			if(i==a1-1)
			{
				for(j=0;j<4;j++)
				{
					cin>>temp;
					z[temp]=1;
				}
			}
			else
			for(j=0;j<4;j++)
			cin>>temp;
		}
		cin>>a2;
		for(i=0;i<4;i++)
		{
			if(i==a2-1)
			{
				for(j=0;j<4;j++)
				{
					cin>>temp;
					y[temp]=1;
				}
			}
			else
			for(j=0;j<4;j++)
			cin>>temp;
		}
		for(i=1;i<17;i++)
		{
			if((y[i]==1)&&(z[i]==1))
			{
				count++;
				ans=i;
			}
		}
		if(count)
		{
			if(count==1)
			{
				cout<<"Case #"<<u<<":"<<" "<<ans<<endl;
			}
			else
			cout<<"Case #"<<u<<":"<<" "<<"Bad magician!"<<endl;
		}
		else
		cout<<"Case #"<<u<<":"<<" "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}