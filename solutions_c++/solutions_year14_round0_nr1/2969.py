#include<iostream>
using namespace std;
int main()
{
	int t,p1,p2,r1[4][4],r2[4][4],z[100],ans[100],i,j,k,x,y;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>p1;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				cin>>r1[x][y];
			}
		}
		cin>>p2;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				cin>>r2[x][y];
			}
		}
		z[i]=0;
		for(x=0;x<4;x++)
		{
			for(y=0;y<4;y++)
			{
				if(r1[p1-1][x]==r2[p2-1][y])
				{
				z[i]++;
				ans[i]=r1[p1-1][x];
				}
			}
		}
		

		
	}
	for(i=0;i<t;i++)
	{
		if(z[i]==1)
		{
			cout<<"Case #"<<(i+1)<<": "<<ans[i]<<endl;
		}
		else
		{
			if(z[i]==0)
			{
				cout<<"Case #"<<(i+1)<<": "<<"Volunteer cheated!"<<endl;
			}
			else
			{
				cout<<"Case #"<<(i+1)<<": "<<"Bad magician!"<<endl;
			}
		}
	}
}
