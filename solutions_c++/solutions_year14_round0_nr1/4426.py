#include<iostream>
using namespace std;
int main()
{
	int c[4],d[4],a[4][4],b[4][4];
	int t;
	cin>>t;
	int k=1;
	int item;
	while(k<=t)
	{
		
		int n;
		cin>>n;
		for(int i=0;i<4;i++)
		{
			cin>>a[i][0]>>a[i][1]>>a[i][2]>>a[i][3];
		}
		for(int i=0;i<4;i++)
		{
			c[i]=a[n-1][i];
		}
		int p;
		cin>>p;
		for(int i=0;i<4;i++)
		{
			cin>>b[i][0]>>b[i][1]>>b[i][2]>>b[i][3];
		}
		for(int i=0;i<4;i++)
		{
			d[i]=b[p-1][i];
		}
		int find=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(c[i]==d[j])
				{
					find=find+1;
					item=c[i];
				}
			}
		}
		switch(find)
		{
			case 0:cout<<"Case #"<<k<<": Volunteer cheated!\n";
				break;
			case 1:cout<<"Case #"<<k<<": "<<item<<"\n";
				break;
			case 2: case 3: case 4:cout<<"Case #"<<k<<": "<<"Bad magician!\n";
		}
		k++;
		
	}
	return 0;
}
