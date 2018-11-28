#include<iostream>
using namespace std;
int main()
{
	int t,i,n1,n2,j,k,l,m,p;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n1;
		int a[4][4];
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
			cin>>a[j][k];
			}
		}
		cin>>n2;
		int b[4][4];
		for(l=1;l<=4;l++)
		{
			for(m=1;m<=4;m++)
			{
			cin>>b[l][m];
			}
		}
		int count=0;
		for(j=1;j<=4;j++)
		{
			for(k=1;k<=4;k++)
			{
				if(a[n1][j]==b[n2][k])
				{
					p=a[n1][j];
					count++;	
				}
			}
		}
		
		if(count==1)
		{
			cout<<"Case #"<<i<<": "<<p<<endl;
		}
		else if(count>1)
		{
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}