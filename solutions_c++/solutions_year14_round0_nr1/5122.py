#include <iostream>
#include<cstdio>
using namespace std;
int ar[5][5],br[5][5];
int main() 
{
	int i,j,n,t,a,b,flag,c,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		flag=0;
		cin>>a;
		cout<<"Case #"<<k<<": ";
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			cin>>ar[i][j];
		}
		cin>>b;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			cin>>br[i][j];
		}
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(ar[a][i]==br[b][j])
				{
					if(flag==0)
					{
						flag=1;
						c=ar[a][i];
					}
					else if(flag==1)
					{
						flag=2;
						break;
					}
				}
			}
		}
		if(flag==0)
		cout<<"Volunteer cheated!\n";
		else if (flag==1)
		cout<<c<<endl;
		else if (flag==2)
		cout<<"Bad magician!\n";
	}
	
	return 0;
}