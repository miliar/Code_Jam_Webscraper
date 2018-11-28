#include<iostream>
using namespace std;
int Run(int a[4][4],int b[4][4],int k1,int k2,int T);
int main()
{
	int T,i,j,k;
	int a[4][4];int b[4][4];
	cin>>T;
	for(i=1;i<=T;i++)
	{
		int k1,k2;
		cin>>k1;
		for(j=1;j<=4;j++)
			for(k=1;k<=4;k++)
			{
				cin>>a[j-1][k-1];
			}
		cin >>k2;
		for(j=1;j<=4;j++)
                        for(k=1;k<=4;k++)
                        {
                                cin>>b[j-1][k-1];
                        }
		Run(a,b,k1-1,k2-1,i);
	}
	return 0;
}
int Run(int a[4][4],int b[4][4],int k1,int k2,int T)
{
	int i,j,flag=0,ans;
	for(i=0;i<4&&flag<=1;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a[k1][i]==b[k2][j])
			{
				flag+=1;
				ans=a[k1][i];
			}
		}
	}
	if(flag==0)
	{
		cout<<"Case #"<<T<<": "<<"Volunteer cheated!"<<endl;
	}
	if(flag==1)
	{
		cout<<"Case #"<<T<<": "<<ans<<endl;
	}
	if(flag>1)
	{
		cout<<"Case #"<<T<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}
