#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	freopen("C:\\Users\\Tarun\\Desktop\\ip.txt","r",stdin);
	freopen("C:\\Users\\Tarun\\Desktop\\op.txt","w",stdout);
	int i,j,t,k,x,y,a[5][5],b[5][5];
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		int count=0,num;
		cin>>x;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>a[i][j];
		cin>>y;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>b[i][j];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[x-1][i]==b[y-1][j])
					count++,num=a[x-1][i];
			}
		}
		if(count==0)
			cout<<"Volunteer cheated!\n";
		else if(count>1)
			cout<<"Bad magician!\n";
		else
			cout<<num<<endl;
	}
	return 0;
}